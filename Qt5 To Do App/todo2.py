import imp
from smtpd import DebuggingServer
from threading import get_ident
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QListWidgetItem
from PyQt5.QtCore import Qt
import sqlite3
import sys
from numpy import deg2rad, rec
from login import *

ilk_id = 2

conn = sqlite3.connect('mylist.db')

c = conn.cursor()

c.execute("""CREATE TABLE if not exists todo_list( 
    list_item text,
    done int, kid int)
    """)

conn.commit()

conn.close()

id = -5
def gonder(x):
    global id
    id = x
   
class maintodo(object):
    
    def setupUi(self, MainWindow):
       
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(521, 365)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.additem_pushButton = QtWidgets.QPushButton(
        self.centralwidget, clicked=lambda: self.add_it())
        self.additem_pushButton.setGeometry(QtCore.QRect(10, 50, 150, 31))
        self.additem_pushButton.setObjectName("additem_pushButton")
        self.markasdone_pushButton_2 = QtWidgets.QPushButton(
        self.centralwidget, clicked=lambda: self.markasdone_it())
        self.markasdone_pushButton_2.setGeometry(
            QtCore.QRect(155, 50, 150, 31))
        self.markasdone_pushButton_2.setObjectName("markasdone_pushButton_2")
        self.clearall_pushButton_3 = QtWidgets.QPushButton(
        self.centralwidget, clicked=lambda: self.clear_it())
        self.clearall_pushButton_3.setGeometry(QtCore.QRect(302, 50, 150, 31))
        self.clearall_pushButton_3.setObjectName("clearall_pushButton_3")

        self.exitButton = QtWidgets.QPushButton(
        self.centralwidget, clicked=lambda: self.exitButton)
        self.exitButton.setGeometry(QtCore.QRect(450, 50, 60, 30))
        self.exitButton.setObjectName("clearall_pushButton_3")
        self.exitButton.clicked.connect(self.to_exit)

        self.additem_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.additem_lineEdit.setGeometry(QtCore.QRect(10, 10, 501, 31))
        self.additem_lineEdit.setObjectName("additem_lineEdit")
        self.mylist_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.mylist_listWidget.setGeometry(QtCore.QRect(10, 90, 501, 231))
        self.mylist_listWidget.setObjectName("mylist_listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 521, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.grab_all()

  
    def grab_all(self):
       
        self.clear_it()
       
        conn = sqlite3.connect('mylist.db')
       
        c = conn.cursor()

        c.execute("SELECT * FROM todo_list")
        records = c.fetchall()

        conn.commit()

        conn.close()

        for record in records:
            item = QListWidgetItem(record[0])
            if record[1] == 1:
                item.setForeground(Qt.green)
            
            
            if record[2] == id:
                self.mylist_listWidget.addItem(item)

    def add_it(self):
        item = self.additem_lineEdit.text()

        if item == "":
            msg = QMessageBox()
            msg.setWindowTitle("BOŞŞŞ")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()
            return

        conn = sqlite3.connect('mylist.db')
       
        c = conn.cursor()
        c.execute("INSERT INTO todo_list(list_item, done, kid) VALUES (?,?,?)", (item, 0, id))
        conn.commit()
     
        conn.close()
       
        self.mylist_listWidget.addItem(item)

        self.additem_lineEdit.setText("")
        
        msg = QMessageBox()
        msg.setWindowTitle("Saved To Database!!")
        msg.setText("Your Todo List Has Been Saved!")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
        self.grab_all()

    

   
    def markasdone_it(self):
       
        clicked = self.mylist_listWidget.currentRow()
        if clicked != None:
            conn = sqlite3.connect('mylist.db')
            c = conn.cursor()
            c.execute("UPDATE todo_list SET done = ? WHERE list_item = ?", (1, self.mylist_listWidget.takeItem(clicked).text()))
            conn.commit()
            conn.close()
        self.grab_all()
        
   # app = QtWidgets.QApplication(sys.argv)
    def clear_it(self):
        self.mylist_listWidget.clear()

    def to_exit(self):
        sys.exit(QtWidgets.QApplication(sys.argv).exec_())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To Do List"))
        self.additem_pushButton.setText(
            _translate("MainWindow", "Add Item To List"))
        self.markasdone_pushButton_2.setText(
            _translate("MainWindow", "Mark As Done"))
        self.clearall_pushButton_3.setText(
            _translate("MainWindow", "Clear The List"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))    
