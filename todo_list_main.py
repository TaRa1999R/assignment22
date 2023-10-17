
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
        
        for i in range (len (self.button_bin)) :
            self.button_bin[i]["button"].clicked.connect (partial (self.remove_task , self.button_bin[i]["id"]))

        for i in range (len (self.button_info)) :
            self.button_info[i]["button"].clicked.connect (partial (self.show_task_info , self.button_info[i]["id"] ))

    
    def read_tasks ( self ) :
        self.tasks = self.database.get_tasks ()
        self.checkbox = []
        self.button_bin = []
        self.button_info = []

        for i in range (len (self.tasks)) :
            if self.tasks[i][6] == 0 :
                new_checkbox = QCheckBox ()
                new_label = QLabel ()
                new_button = QPushButton ()
                new_button_info = QPushButton ()
                self.checkbox.append ({"checkbox" : new_checkbox , "id" : self.tasks[i][0]})
                self.button_bin.append ({"button" : new_button , "id" : self.tasks[i][0]})
                self.button_info.append ({"button" : new_button_info , "id" : self.tasks[i][0]})

                new_label.setText (self.tasks[i][1])
                new_button.setText ("🗑")
                new_button_info.setText ("📁")
                new_checkbox.setSizePolicy (QSizePolicy.Maximum , QSizePolicy.Fixed)
                new_button.setSizePolicy (QSizePolicy.Maximum , QSizePolicy.Fixed)
                new_button_info.setSizePolicy (QSizePolicy.Maximum , QSizePolicy.Fixed)
                new_label.setFont (QFont ("Segoe UI" , 12))
                new_button.setStyleSheet ("background-color: rgb(253,255,80);")
                new_button_info.setStyleSheet ("background-color: rgb(207,165,255);")
                if self.tasks[i][5] == 0 :
                    new_label.setStyleSheet ("background-color: rgb(0,255,127);")
                
                elif self.tasks[i][5] == 1 :
                    new_label.setStyleSheet ("background-color: rgb(255,160,112);")

                elif self.tasks[i][5] == 2 :
                    new_label.setStyleSheet ("background-color: rgb(255,73,115);")

                self.ui.task_section.addWidget (new_checkbox , i , 0)
                self.ui.task_section.addWidget (new_label , i , 1)
                self.ui.task_section.addWidget (new_button_info , i , 2)
                self.ui.task_section.addWidget (new_button , i , 3)
        
        for i in range (len (self.tasks)) :
            if self.tasks[i][6] == 1 :
                new_checkbox = QCheckBox ()
                new_label = QLabel ()
                new_button = QPushButton ()
                new_button_info = QPushButton ()
                self.checkbox.append ({"checkbox" : new_checkbox , "id" : self.tasks[i][0]})
                self.button_bin.append ({"button" : new_button , "id" : self.tasks[i][0]})
                self.button_info.append ({"button" : new_button_info , "id" : self.tasks[i][0]})

                new_label.setText (self.tasks[i][1])
                new_button.setText ("🗑")
                new_button_info.setText ("...")
                new_checkbox.setSizePolicy (QSizePolicy.Maximum , QSizePolicy.Fixed)
                new_button.setSizePolicy (QSizePolicy.Maximum , QSizePolicy.Fixed)
                new_button_info.setSizePolicy (QSizePolicy.Maximum , QSizePolicy.Fixed)
                new_label.setFont (QFont ("Segoe UI" , 12))
                new_checkbox.setChecked (True)
                new_button.setStyleSheet ("background-color: rgb(255,61,103);")
                new_button_info.setStyleSheet ("background-color: rgb(255,61,103);")
                new_label.setStyleSheet ("background-color: rgb(195,195,195);")

                self.ui.task_section.addWidget (new_checkbox , i + len (self.checkbox) , 0)
                self.ui.task_section.addWidget (new_label , i + len (self.checkbox) , 1)
                self.ui.task_section.addWidget (new_button_info , i + len (self.checkbox) , 2)
                self.ui.task_section.addWidget (new_button , i + len (self.checkbox) , 3)


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
        if checkbox.isChecked () == True :
            self.database.update_task (id , 1)
        
        else :
            self.database.update_task (id , 0)
        

    def remove_task ( self , id ) :
        feedback = self.database.delete_task (id)
        if feedback == True : ...

        else : ...


    def show_task_info ( self , id ) :
        for i in range (len (self.tasks)) :
            if self.tasks[i][0] == id :
                description = self.tasks[i][2]
                date = self.tasks[i][3]
                time = self.tasks[i][4]
        text = f"{description}.📋\nit must be done until : {date} 📅\n before : {time} ⏰"
        message = QMessageBox (windowTitle = "📂Details📂" , text = text)
        message.exec_ ()


if __name__ == "__main__" :
    app = QApplication ( sys.argv )
    window = Mainwindow ()
    window.show ()
    app.exec ()