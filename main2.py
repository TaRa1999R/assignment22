
import sys
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from todo_list_design import Ui_MainWindow
from todo_list_database import Database

class Mainwindow ( QMainWindow ) :
    
    def __init__ ( self ) :
        super().__init__ ()
        self.ui = Ui_MainWindow ()
        self.ui.setupUi (self)
        
        self.database = Database ()

    
    def read_tasks ( self ) : ...


    def add_task ( self ) : ...


    def check_task ( self ) : ...


    def remove_task ( self ) : ...


    def show_task_info ( self ) : ...


if __name__ == "__main__" :
    app = QApplication ( sys.argv )
    window = Mainwindow ()
    window.show ()
    app.exec ()