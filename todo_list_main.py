
import sys
from functools import partial
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

        self.ui.add.clicked.connect (self.add_new_task)

        for i in range (len (self.check)) :
            self.check[i]["check"].clicked.connect (partial (self.check_tasks , self.check[i]["check"] , self.check[i]["id"] ,self.check[i]["label"] , self.check[i]["priority"])) 



    def read_tasks_from_database ( self ) :
        self.check = []
        self.delete = []
        for i in range (len(self.tasks)) :
            if self.tasks[i][6] == 0 :
                new_chckbox = QCheckBox ()
                new_label = QLabel ()
                new_button = QPushButton ()
                self.check.append ({"check" : new_chckbox , "id" : self.tasks[i][0] , "label" : new_label , "priority" : self.tasks[i][5]})
                self.delete.append (new_button)

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
    
        
        for i in range (len(self.tasks)) :
            if self.tasks[i][6] == 1 :
                new_chckbox = QCheckBox ()
                new_label = QLabel ()
                new_button = QPushButton ()
                self.check.append ({"check" : new_chckbox , "id" : self.tasks[i][0] , "label" : new_label , "priority" : self.tasks[i][5]})
                self.delete.append (new_button)
                
                new_label.setStyleSheet ("background-color: rgb(180,180,180);")
                new_label.setText (self.tasks[i][1])
                new_button.setText ("🗑")
                new_button.setStyleSheet ("background-color: rgb(255,255,127);")
                new_chckbox.setSizePolicy (QSizePolicy.Maximum , QSizePolicy.Fixed)
                new_button.setSizePolicy (QSizePolicy.Maximum , QSizePolicy.Fixed)
                new_label.setFont (QFont ("Segoe UI" , 12))
                new_chckbox.setChecked (True)

                self.ui.task_section.addWidget (new_chckbox , i + len (self.check) , 0)
                self.ui.task_section.addWidget (new_label , i + len (self.check) , 1)
                self.ui.task_section.addWidget (new_button , i + len (self.check) , 2)


        


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


    def check_tasks ( self , checkbox , id , label , priority) :
        if checkbox.isChecked () == True :
            self.database.update_task (id , 1)
            label.setStyleSheet ("background-color: rgb(180,180,180);")


        else :
            self.database.update_task (id , 0)
            if priority == 0 :
                label.setStyleSheet ("background-color: rgb(0,255,127);")
                
            elif priority == 1 :
                label.setStyleSheet ("background-color: rgb(255,160,112);")

            elif priority == 2 :
                label.setStyleSheet ("background-color: rgb(255,61,103);")
        

    def delete_tasks ( self ) :
        ...





if __name__ == "__main__" :
    app = QApplication ( sys.argv )
    window = Mainwindow ()
    window.show ()
    app.exec ()