from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget
from gui.NoteEditDialog import NoteEditDialog
# from PyQt5.uic import loadUi
from .ui.Ui_NotesWidget import Ui_Form

from core.NoteModel import NoteModel

class NotesWidget(QWidget, Ui_Form):  #Ui_Form

    selection_changed = pyqtSignal(list, name='selectionChanged')


    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__init_model(model)
        self.init_ui()
        self.__init_signals()

    def init_ui(self):
        # loadUi('gui/ui/notes_widget.ui', self)
        self.setupUi(self)

        self.notesView.setModel(self.__model)
        self.notesView.resizeColumnsToContents

    def __init_signals(self):
        self.notesView.doubleClicked.connect(self.edit_note)
        self.notesView.selectionModel().selectionChanged.connect(
            self.__on_selection_changed
        )

    def __on_selection_changed(self):
        self.selection_changed.emit(
            self.selected_rows()
        )

    def __init_model(self, model):
        if isinstance(model, NoteModel):
            self.__model = model
            self.__model.select()
        else:
            raise RuntimeError('The loaded model is not NoteModel')

    def __open_edit_dialog(self, row=None, title=None):
        d = NoteEditDialog(model=self.__model, row=row, parent=self)
        d.ready.connect(self.on__ready)

        if title:
            d.setWindowTitle(title)

        d.exec_()

    def on__ready(self, state, row):
        self.notesView.setCurrentIndex(
            self.__model.index(row, 0)
        )

        if state:
            self.notesView.resizeColumnsToContents()

    def add_new_note(self):
        self.__open_edit_dialog()

    def edit_note(self, index):
        self.__open_edit_dialog(row=index.row(), title=u'Edit note')

    def edit_selected_note(self):
        selected = self.selected_rows()

        if len(selected) == 1:
            self.edit_note(selected.pop()) #[0]

    def remove_notes(self, indices):
        indices.sort(reverse=True)

        for index in indices:
            self.__model.removeRow(index.row())

        self.__model.select()

    def remove_selected_notes(self):
        self.remove_notes(self.selected_rows())

    def selected_rows(self):
        return self.notesView.selectionModel().selectedRows()

