
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

        self.check = []
        self.delete = []

        self.read_tasks_from_database ()

        self.ui.add.clicked.connect (self.add_new_task)


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


    def add_new_task ( self ) :
        if self.ui.new_title.text() == "" :
            text = f"You haven't type any title for new task.\nPlease write the title and details first, and push the button at the end. \nThanks😇"
            message = QMessageBox (windowTitle = "❌Error!!❌" , text = text)
            message.exec_ ()
        
        else :
            title = self.ui.new_title.text ()
            description = self.ui.new_description.toPlainText ()
            date = self.ui.new_date.text ()
            time = self.ui.new_time.text ()
            if self.ui.priority.currentText () == "Low" :
                priority = 0
            
            elif self.ui.priority.currentText () == "Medium" :
                priority = 1
            
            elif self.ui.priority.currentText () == "High" :
                priority = 2

            
            feedback = self.database.add_new_task (title , description , date , time , priority)

            if feedback == True :
                self.read_tasks_from_database ()
                self.ui.new_title.setText ("")
                self.ui.new_description.setText ("")
                self.ui.new_date.setText ("")
                self.ui.new_time.setText ("")
                self.ui.priority.setCurrentText ("Low")

            else :
                text = f"New task couldn't be added.😒 \nPlease try again."
                message = QMessageBox (windowTitle = "❌Error!!❌" , text = text)
                message.exec_ ()


    def done_tasks ( self ) :
        ...

   
    def delete_tasks ( self ) :
        ...





if __name__ == "__main__" :
    app = QApplication ( sys.argv )
    window = Mainwindow ()
    window.show ()
    app.exec ()