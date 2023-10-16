# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'todo_list.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(385, 588)
        MainWindow.setStyleSheet(u"background-color: rgb(110, 110, 110);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.task_section = QGridLayout()
        self.task_section.setObjectName(u"task_section")

        self.gridLayout.addLayout(self.task_section, 0, 0, 1, 1)

        self.add_section = QGridLayout()
        self.add_section.setObjectName(u"add_section")
        self.time_lable = QLabel(self.centralwidget)
        self.time_lable.setObjectName(u"time_lable")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.time_lable.setFont(font)
        self.time_lable.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.time_lable.setAlignment(Qt.AlignCenter)

        self.add_section.addWidget(self.time_lable, 3, 0, 1, 1)

        self.description_lable = QLabel(self.centralwidget)
        self.description_lable.setObjectName(u"description_lable")
        self.description_lable.setFont(font)
        self.description_lable.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.description_lable.setAlignment(Qt.AlignCenter)

        self.add_section.addWidget(self.description_lable, 1, 0, 1, 1)

        self.title_lable = QLabel(self.centralwidget)
        self.title_lable.setObjectName(u"title_lable")
        self.title_lable.setFont(font)
        self.title_lable.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.title_lable.setAlignment(Qt.AlignCenter)

        self.add_section.addWidget(self.title_lable, 0, 0, 1, 1)

        self.priority_lable = QLabel(self.centralwidget)
        self.priority_lable.setObjectName(u"priority_lable")
        self.priority_lable.setFont(font)
        self.priority_lable.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.priority_lable.setAlignment(Qt.AlignCenter)

        self.add_section.addWidget(self.priority_lable, 4, 0, 1, 1)

        self.date_lable = QLabel(self.centralwidget)
        self.date_lable.setObjectName(u"date_lable")
        self.date_lable.setFont(font)
        self.date_lable.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.date_lable.setAlignment(Qt.AlignCenter)

        self.add_section.addWidget(self.date_lable, 2, 0, 1, 1)

        self.new_time = QLineEdit(self.centralwidget)
        self.new_time.setObjectName(u"new_time")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_time.sizePolicy().hasHeightForWidth())
        self.new_time.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        self.new_time.setFont(font1)
        self.new_time.setStyleSheet(u"background-color: rgb(0, 255, 255);\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.new_time.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.add_section.addWidget(self.new_time, 3, 1, 1, 1)

        self.new_date = QLineEdit(self.centralwidget)
        self.new_date.setObjectName(u"new_date")
        sizePolicy.setHeightForWidth(self.new_date.sizePolicy().hasHeightForWidth())
        self.new_date.setSizePolicy(sizePolicy)
        self.new_date.setFont(font1)
        self.new_date.setStyleSheet(u"background-color: rgb(0, 255, 255);\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.new_date.setEchoMode(QLineEdit.Normal)
        self.new_date.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.add_section.addWidget(self.new_date, 2, 1, 1, 1)

        self.new_title = QLineEdit(self.centralwidget)
        self.new_title.setObjectName(u"new_title")
        sizePolicy.setHeightForWidth(self.new_title.sizePolicy().hasHeightForWidth())
        self.new_title.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.new_title.setFont(font2)
        self.new_title.setStyleSheet(u"background-color: rgb(0, 255, 255);\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")
        self.new_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.add_section.addWidget(self.new_title, 0, 1, 1, 1)

        self.priority = QComboBox(self.centralwidget)
        self.priority.addItem("")
        self.priority.addItem("")
        self.priority.addItem("")
        self.priority.setObjectName(u"priority")
        self.priority.setFont(font1)
        self.priority.setStyleSheet(u"background-color: rgb(0, 255, 255);\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")

        self.add_section.addWidget(self.priority, 4, 1, 1, 1)

        self.new_description = QTextEdit(self.centralwidget)
        self.new_description.setObjectName(u"new_description")
        sizePolicy.setHeightForWidth(self.new_description.sizePolicy().hasHeightForWidth())
        self.new_description.setSizePolicy(sizePolicy)
        self.new_description.setFont(font1)
        self.new_description.setStyleSheet(u"background-color: rgb(0, 255, 255);\n"
"border-top-left-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;")

        self.add_section.addWidget(self.new_description, 1, 1, 1, 1)

        self.add = QPushButton(self.centralwidget)
        self.add.setObjectName(u"add")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.add.setFont(font3)
        self.add.setStyleSheet(u"background-color: rgb(255, 255, 127);border-right-bottom-radius: 5xp;")

        self.add_section.addWidget(self.add, 0, 2, 1, 1)


        self.gridLayout.addLayout(self.add_section, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 385, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"To Do List", None))
        self.time_lable.setText(QCoreApplication.translate("MainWindow", u"time", None))
        self.description_lable.setText(QCoreApplication.translate("MainWindow", u"description", None))
        self.title_lable.setText(QCoreApplication.translate("MainWindow", u"title", None))
        self.priority_lable.setText(QCoreApplication.translate("MainWindow", u"priority", None))
        self.date_lable.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.new_time.setInputMask("")
        self.new_time.setText("")
        self.new_date.setInputMask("")
        self.new_date.setText("")
        self.new_title.setInputMask("")
        self.new_title.setText("")
        self.priority.setItemText(0, QCoreApplication.translate("MainWindow", u"Low", None))
        self.priority.setItemText(1, QCoreApplication.translate("MainWindow", u"Medium", None))
        self.priority.setItemText(2, QCoreApplication.translate("MainWindow", u"High", None))

        self.new_description.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.add.setText(QCoreApplication.translate("MainWindow", u"+", None))
    # retranslateUi

