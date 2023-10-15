
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from todo_list_design import Ui_MainWindow

class Mainwindow ( QMainWindow ) :

    def __init__ ( self ) :
        super().__init__() 
        self.ui = Ui_MainWindow ()
        self.ui.setupUi (self)

if __name__ == "__main__" :
    app = QApplication ( sys.argv )
    window = Mainwindow ()
    window.show ()
    app.exec ()