# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Registration(object):

    def next_button(self):
        from Secondary import  Ui_secondary
        self.window= QtWidgets.QMainWindow()
        self.ui=Ui_secondary()
        self.ui.setupUi(self.window)
        Registration.hide()
        self.window.show()


    def setupUi(self, Registration):
        Registration.setObjectName("Registration")
        Registration.resize(1350, 800)
        Registration.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(Registration)
        self.centralwidget.setObjectName("centralwidget")
        self.emailbox = QtWidgets.QLineEdit(self.centralwidget)
        self.emailbox.setGeometry(QtCore.QRect(360, 290, 311, 31))
        self.emailbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.emailbox.setObjectName("emailbox")

        self.usernametext = QtWidgets.QLabel(self.centralwidget)
        self.usernametext.setGeometry(QtCore.QRect(360, 340, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.usernametext.setFont(font)
        self.usernametext.setStyleSheet("color: rgb(32, 151, 255);")
        self.usernametext.setObjectName("usernametext")
        self.sayn = QtWidgets.QLabel(self.centralwidget)
        self.sayn.setGeometry(QtCore.QRect(570, 200, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.sayn.setFont(font)
        self.sayn.setAutoFillBackground(False)
        self.sayn.setStyleSheet("color: rgb(255, 255, 255);")
        self.sayn.setAlignment(QtCore.Qt.AlignCenter)
        self.sayn.setObjectName("sayn")
        self.emailtext = QtWidgets.QLabel(self.centralwidget)
        self.emailtext.setGeometry(QtCore.QRect(360, 260, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.emailtext.setFont(font)
        self.emailtext.setStyleSheet("color: rgb(32, 151, 255);\n"
"")
        self.emailtext.setObjectName("emailtext")
        self.usernamebox = QtWidgets.QLineEdit(self.centralwidget)
        self.usernamebox.setGeometry(QtCore.QRect(360, 370, 311, 31))
        self.usernamebox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.usernamebox.setObjectName("usernamebox")
        self.passtext_1 = QtWidgets.QLabel(self.centralwidget)
        self.passtext_1.setGeometry(QtCore.QRect(360, 420, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.passtext_1.setFont(font)
        self.passtext_1.setStyleSheet("color: rgb(32, 151, 255);")
        self.passtext_1.setObjectName("passtext_1")
        self.passbox_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.passbox_1.setGeometry(QtCore.QRect(360, 450, 311, 31))
        self.passbox_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.passbox_1.setObjectName("passbox_1")
        self.passtext_2 = QtWidgets.QLabel(self.centralwidget)
        self.passtext_2.setGeometry(QtCore.QRect(360, 500, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.passtext_2.setFont(font)
        self.passtext_2.setStyleSheet("color: rgb(32, 151, 255);")
        self.passtext_2.setObjectName("passtext_2")
        self.passbox_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.passbox_2.setGeometry(QtCore.QRect(360, 530, 311, 31))
        self.passbox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.passbox_2.setObjectName("passbox_2")
        self.passtext_3 = QtWidgets.QLabel(self.centralwidget)
        self.passtext_3.setGeometry(QtCore.QRect(360, 580, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.passtext_3.setFont(font)
        self.passtext_3.setStyleSheet("color: rgb(32, 151, 255);")
        self.passtext_3.setObjectName("passtext_3")
        self.passbox_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.passbox_3.setGeometry(QtCore.QRect(360, 610, 311, 31))
        self.passbox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.passbox_3.setObjectName("passbox_3")
        self.passbox_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.passbox_4.setGeometry(QtCore.QRect(710, 370, 311, 31))
        self.passbox_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.passbox_4.setObjectName("passbox_4")
        self.passbox_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.passbox_5.setGeometry(QtCore.QRect(710, 450, 311, 31))
        self.passbox_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.passbox_5.setObjectName("passbox_5")
        self.passtext_5 = QtWidgets.QLabel(self.centralwidget)
        self.passtext_5.setGeometry(QtCore.QRect(710, 420, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.passtext_5.setFont(font)
        self.passtext_5.setStyleSheet("color: rgb(32, 151, 255);")
        self.passtext_5.setObjectName("passtext_5")
        self.passtext_4 = QtWidgets.QLabel(self.centralwidget)
        self.passtext_4.setGeometry(QtCore.QRect(710, 340, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.passtext_4.setFont(font)
        self.passtext_4.setStyleSheet("color: rgb(32, 151, 255);")
        self.passtext_4.setObjectName("passtext_4")
        self.passbox_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.passbox_6.setGeometry(QtCore.QRect(710, 530, 311, 31))
        self.passbox_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.passbox_6.setObjectName("passbox_6")
        self.passtext_6 = QtWidgets.QLabel(self.centralwidget)
        self.passtext_6.setGeometry(QtCore.QRect(710, 500, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.passtext_6.setFont(font)
        self.passtext_6.setStyleSheet("color: rgb(32, 151, 255);")
        self.passtext_6.setObjectName("passtext_6")
        self.nextbutton = QtWidgets.QPushButton(self.centralwidget)
        self.nextbutton.setGeometry(QtCore.QRect(940, 610, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nextbutton.setFont(font)
        self.nextbutton.setStyleSheet("background-color: rgb(32, 151, 255);\n"
"color: rgb(255, 255, 255);")
        self.nextbutton.setObjectName("nextbutton")

        self.nextbutton.clicked.connect(self.next_button)


        self.image = QtWidgets.QPushButton(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(620, 50, 151, 131))
        self.image.setStyleSheet("border-radius: 60px;\n"
"background-color: rgb(255, 255, 255);\n"
"image: url(3.png);")
        self.image.setText("")
        self.image.setObjectName("image")
        Registration.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Registration)
        self.statusbar.setObjectName("statusbar")
        Registration.setStatusBar(self.statusbar)

        self.retranslateUi(Registration)
        QtCore.QMetaObject.connectSlotsByName(Registration)

    def retranslateUi(self, Registration):
        _translate = QtCore.QCoreApplication.translate
        Registration.setWindowTitle(_translate("Registration", "Registration"))
        self.usernametext.setText(_translate("Registration", "Enter Username"))
        self.sayn.setText(_translate("Registration", "SAYN SECURITIES"))
        self.emailtext.setText(_translate("Registration", "Enter E-mail"))
        self.passtext_1.setText(_translate("Registration", "Enter Password"))
        self.passtext_2.setText(_translate("Registration", "Re-enter Password"))
        self.passtext_3.setText(_translate("Registration", "Re-enter Password"))
        self.passtext_5.setText(_translate("Registration", "Re-enter Password"))
        self.passtext_4.setText(_translate("Registration", "Re-enter Password"))
        self.passtext_6.setText(_translate("Registration", "Re-enter Password"))
        self.nextbutton.setText(_translate("Registration", "Next"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Registration = QtWidgets.QMainWindow()
    ui = Ui_Registration()
    ui.setupUi(Registration)
    Registration.show()
    app.exec_()
