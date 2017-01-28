
from PyQt5.QtWidgets import QWidget
from .ui.Ui_LoginWidget import Ui_Form

class LoginWidget(QWidget, Ui_Form):  #Ui_Form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        self.setupUi(self)

