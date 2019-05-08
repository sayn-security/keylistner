import Login as lg
import KeyListener as kls
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    lg.LOGIN = QtWidgets.QMainWindow()
    ui = lg.Ui_LOGIN()
    ui.setupUi(lg.LOGIN)
    Thread(target=lg.LOGIN.show()).run()
if __name__ == "__main__":
    main()
    #kls.keylis()