
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
        self.read_tasks ()

        self.ui.add.clicked.connect (self.add_task)
        for i in range (len (self.checkbox)) :
            self.checkbox[i]["checkbox"].clicked.connect (partial (self.check_task , self.checkbox[i]["checkbox"] , self.checkbox[i]["id"]))

    
    def read_tasks ( self ) :
        self.tasks = self.database.get_tasks ()
        self.checkbox = []
        self.button_bin = []
        self.label_info = []

        for i in range (len (self.tasks)) :
            if self.tasks[i][6] == 0 :
                new_checkbox = QCheckBox ()
                new_label = QLabel ()
                new_button = QPushButton ()
                self.checkbox.append ({"checkbox" : new_checkbox , "id" : self.tasks[i][0]})
                self.button_bin.append ({"button" : new_button , "id" : self.tasks[i][0]})
                self.label_info.append ({"label" : new_label , "id" : self.tasks[i][0]})

                new_label.setText (self.tasks[i][1])
                new_button.setText ("🗑")
                new_checkbox.setSizePolicy (QSizePolicy.Maximum , QSizePolicy.Fixed)
                new_button.setSizePolicy (QSizePolicy.Maximum , QSizePolicy.Fixed)
                new_label.setFont (QFont ("Segoe UI" , 12))
                new_button.setStyleSheet ("background-color: rgb(207,165,255);")
                if self.tasks[i][5] == 0 :
                    new_label.setStyleSheet ("background-color: rgb(0,255,127);")
                
                elif self.tasks[i][5] == 1 :
                    new_label.setStyleSheet ("background-color: rgb(255,160,112);")

                elif self.tasks[i][5] == 2 :
                    new_label.setStyleSheet ("background-color: rgb(255,73,115);")

                self.ui.task_section.addWidget (new_checkbox , i , 0)
                self.ui.task_section.addWidget (new_label , i , 1)
                self.ui.task_section.addWidget (new_button , i , 2)
        
        for i in range (len (self.tasks)) :
            if self.tasks[i][6] == 1 :
                new_checkbox = QCheckBox ()
                new_label = QLabel ()
                new_button = QPushButton ()
                self.checkbox.append ({"checkbox" : new_checkbox , "id" : self.tasks[i][0]})
                self.button_bin.append ({"button" : new_button , "id" : self.tasks[i][0]})
                self.label_info.append ({"label" : new_label , "id" : self.tasks[i][0]})

                new_label.setText (self.tasks[i][1])
                new_button.setText ("🗑")
                new_checkbox.setSizePolicy (QSizePolicy.Maximum , QSizePolicy.Fixed)
                new_button.setSizePolicy (QSizePolicy.Maximum , QSizePolicy.Fixed)
                new_label.setFont (QFont ("Segoe UI" , 12))
                new_checkbox.setChecked (True)
                new_button.setStyleSheet ("background-color: rgb(255,61,103);")
                new_label.setStyleSheet ("background-color: rgb(195,195,195);")

                self.ui.task_section.addWidget (new_checkbox , i + len (self.checkbox) , 0)
                self.ui.task_section.addWidget (new_label , i + len (self.checkbox) , 1)
                self.ui.task_section.addWidget (new_button , i + len (self.checkbox) , 2)


    def add_task ( self ) :
        if self.ui.title.text () == "" :
            text = f"You haven't type any title for new task.\nPlease write the title and details first, and push the button at the end. \nThanks😇"
            message = QMessageBox (windowTitle = "❌Error!!❌" , text = text)
            message.exec_ ()
        
        else :
            new_title = self.ui.title.text ()
            new_description = self.ui.description.toPlainText ()
            new_date = self.ui.date.text ()
            new_time = self.ui.time.text ()
            if self.ui.priority.currentText () == "Low" :
                new_priority = 0
            
            elif self.ui.priority.currentText () == "Medium" :
                new_priority = 1
            
            elif self.ui.priority.currentText () == "High" :
                new_priority = 2

            feedback = self.database.add_task (new_title , new_description , new_date , new_time , new_priority)

            if feedback == True :
                self.read_tasks ()
                self.ui.title.setText ("")
                self.ui.description.setText ("")
                self.ui.date.setText ("")
                self.ui.time.setText ("")
                self.ui.priority.setCurrentText ("Low")


            else :
                text = f"New task couldn't be added.😒 \nPlease try again."
                message = QMessageBox (windowTitle = "❌Error!!❌" , text = text)
                message.exec_ ()



    def check_task ( self , checkbox , id ) :
        print ("hi")
        if checkbox.isChecked == True :
            feedback = self.database.update_task (id , 1)
        
        else :
            feedback = self.database.update_task (id , 0)
        
        print (feedback)
        # self.read_tasks ()
        
        # else :
        #     text = f"An Error occur.😕 \nPlease try again."
        #     message = QMessageBox (windowTitle = "❌Error!!❌" , text = text)
        #     message.exec_ ()

    def remove_task ( self ) : ...


    def show_task_info ( self ) : ...


if __name__ == "__main__" :
    app = QApplication ( sys.argv )
    window = Mainwindow ()
    window.show ()
    app.exec ()