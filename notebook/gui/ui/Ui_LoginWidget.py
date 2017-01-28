# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_widget.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(40, 31, 221, 101))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loginLabel = QtWidgets.QLabel(self.widget)
        self.loginLabel.setObjectName("loginLabel")
        self.horizontalLayout.addWidget(self.loginLabel)
        self.loginEdit = QtWidgets.QLineEdit(self.widget)
        self.loginEdit.setObjectName("loginEdit")
        self.horizontalLayout.addWidget(self.loginEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.passwordLabel = QtWidgets.QLabel(self.widget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.horizontalLayout_2.addWidget(self.passwordLabel)
        self.passwordEdit = QtWidgets.QLineEdit(self.widget)
        self.passwordEdit.setObjectName("passwordEdit")
        self.horizontalLayout_2.addWidget(self.passwordEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.okButton = QtWidgets.QPushButton(self.widget)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout_3.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(self.widget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_3.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.loginLabel.raise_()
        self.passwordLabel.raise_()
        self.loginEdit.raise_()
        self.passwordEdit.raise_()
        self.okButton.raise_()
        self.cancelButton.raise_()
        self.okButton.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.loginLabel.setText(_translate("Form", "login"))
        self.loginEdit.setStatusTip(_translate("Form", "enter your login"))
        self.passwordLabel.setText(_translate("Form", "password"))
        self.passwordEdit.setStatusTip(_translate("Form", "enter your password"))
        self.okButton.setStatusTip(_translate("Form", "press OK after you filled everything"))
        self.okButton.setText(_translate("Form", "OK"))
        self.cancelButton.setStatusTip(_translate("Form", "press cancel if you want to exit the program"))
        self.cancelButton.setText(_translate("Form", "Cancel"))

