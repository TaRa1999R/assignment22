
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from todo_list_design import Ui_MainWindow
from todo_list_database import Database

class Mainwindow ( QMainWindow ) :

    def __init__ ( self ) :
        super().__init__() 
        self.ui = Ui_MainWindow ()
        self.ui.setupUi (self)

        self.database = Database ()
        self.tasks = self.database.get_tasks ()

        self.read_tasks_from_database ()
    

    def read_tasks_from_database ( self ) :
        for i in range (len(self.tasks)) :
            new_chckbox = QCheckBox ()
            new_label = QLabel ()
            new_button = QPushButton ()
            if self.tasks[i][5] == 0 :
                new_label.setStyleSheet ("background-color: rgb(0,255,127);")
            
            elif self.tasks[i][5] == 1 :
                new_label.setStyleSheet ("background-color: rgb(255,160,112);")

            
            elif self.tasks[i][5] == 2 :
                new_label.setStyleSheet ("background-color: rgb(255,61,103);")

            new_label.setText (self.tasks[i][1])
            new_button.setText ("🗑")
            new_button.setStyleSheet ("background-color: rgb(255,255,127);")
            new_chckbox.setSizePolicy (QSizePolicy.Maximum , QSizePolicy.Fixed)
            new_button.setSizePolicy (QSizePolicy.Maximum , QSizePolicy.Fixed)
            new_label.setFont (QFont ("Segoe UI" , 12))
            self.ui.task_section.addWidget (new_chckbox , i , 0)
            self.ui.task_section.addWidget (new_label , i , 1)
            self.ui.task_section.addWidget (new_button , i , 2)





if __name__ == "__main__" :
    app = QApplication ( sys.argv )
    window = Mainwindow ()
    window.show ()
    app.exec ()