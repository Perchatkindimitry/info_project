# Form implementation generated from reading ui file 'c:\Users\Dimitry\Python programs\lab-infa\UI\start_screen.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(843, 309)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.code_button = QtWidgets.QPushButton(Form)
        self.code_button.setObjectName("code_button")
        self.menu = QtWidgets.QButtonGroup(Form)
        self.menu.setObjectName("menu")
        self.menu.addButton(self.code_button)
        self.verticalLayout.addWidget(self.code_button)
        self.decode_button = QtWidgets.QPushButton(Form)
        self.decode_button.setObjectName("decode_button")
        self.menu.addButton(self.decode_button)
        self.verticalLayout.addWidget(self.decode_button)
        self.about_button = QtWidgets.QPushButton(Form)
        self.about_button.setObjectName("about_button")
        self.menu.addButton(self.about_button)
        self.verticalLayout.addWidget(self.about_button)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.code_button.setText(_translate("Form", "прямая задача"))
        self.decode_button.setText(_translate("Form", "обратная задача"))
        self.about_button.setText(_translate("Form", "О нас"))
