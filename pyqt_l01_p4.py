import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QLabel, QPushButton, QDoubleSpinBox,
                             QVBoxLayout, QAction)
from PyQt5.QtCore import QObject

class Course(QObject):
    def get(self):
        return 30.0

class CurrencyConverter(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initUi()
        self.initLayouts()
        self.initSignals()

    def initUi(self):
        self.setWindowTitle('Currency Converter')

        self.rubLabel = QLabel("Sum in rubles", self)
        self.dolLabel = QLabel("Sum in dollars", self)

        self.rubAmount = QDoubleSpinBox(self)
        self.rubAmount.setMaximum(999999999)
        self.dolAmount = QDoubleSpinBox(self)
        self.dolAmount.setMaximum(999999999)
        # self.dolAmount.setReadOnly(True)

        self.convertBtn = QPushButton('translate', self)
        self.clearBtn = QPushButton('clear all', self)
        #self.convertBtn.setEnabled(False)
        # self.convertBtn.setDisabled(True)

    def initSignals(self):
        self.convertBtn.clicked.connect(self.onClick)
        self.clearBtn.clicked.connect(self.clearOnClick)

    def initLayouts(self):
        self.w = QWidget()

        self.mainLayout = QVBoxLayout(self.w)
        self.mainLayout.addWidget(self.rubLabel)
        self.mainLayout.addWidget(self.rubAmount)
        self.mainLayout.addWidget(self.dolLabel)
        self.mainLayout.addWidget(self.dolAmount)
        self.mainLayout.addWidget(self.convertBtn)
        self.mainLayout.addWidget(self.clearBtn)

        self.setCentralWidget(self.w)

    def onClick(self):

        value_rub = self.rubAmount.value()
        value_dol = self.dolAmount.value()

        if value_dol and value_rub:
            self.convertBtn.setEnabled(False)
        elif value_rub:
            self.dolAmount.setValue(value_rub / Course().get())
        elif value_dol:
            self.rubAmount.setValue(value_dol * Course().get())
        self.convertBtn.setEnabled(False)



    def clearOnClick(self):

        self.rubAmount.setValue(0.00)
        self.dolAmount.setValue(0.00)
        self.convertBtn.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    converter = CurrencyConverter()
    converter.show()

    sys.exit(app.exec_())