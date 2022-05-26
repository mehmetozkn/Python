from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from todo2 import *

k_id = -2

class Ui_MainWindow(object):
 
    def setupUi(self, MainWindow):
        
        self.mainwindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.bg_photo = QtWidgets.QLabel(self.centralwidget)
        self.bg_photo.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.bg_photo.setAutoFillBackground(False)
        self.bg_photo.setText("")
        self.bg_photo.setPixmap(QtGui.QPixmap("bg.jpeg"))
        self.bg_photo.setScaledContents(True)
        self.bg_photo.setObjectName("bg_photo")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(110, 50, 511, 411))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_register = QtWidgets.QWidget()
        self.page_register.setStyleSheet("*{\n"
                                         "font: Roboto 20pt \"Brush Script MT\";\n"
                                         "color : brown;\n"
                                         "background: transparent\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton\n"
                                         "\n"
                                         "{\n"
                                         "background-color : rgb(85, 0, 0, 0.7);\n"
                                         "}\n"
                                         "\n"
                                         "QLabel\n"
                                         "{\n"
                                         "color: yellow\n"
                                         "}\n"
                                         "\n"
                                         "QLineEdit{\n"
                                         "background-color : rgb(85, 0, 0, 0.7);\n"
                                         "color:white;\n"
                                         "}")
        self.page_register.setObjectName("page_register")
        self.formLayoutWidget = QtWidgets.QWidget(self.page_register)
        self.formLayoutWidget.setGeometry(QtCore.QRect(100, 150, 481, 191))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.registerNameTextField = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.registerNameTextField.setObjectName("register_name")
        self.registerNameTextField.setStyleSheet("")
        self.verticalLayout_4.addWidget(self.registerNameTextField)
        self.registerPasswordTextField = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.registerPasswordTextField.setObjectName("register_password")
        self.registerPasswordTextField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout_4.addWidget(self.registerPasswordTextField)
        self.registerConfirmPasswordTextField = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.registerConfirmPasswordTextField.setObjectName("register_confirm_password")
        self.registerConfirmPasswordTextField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout_4.addWidget(self.registerConfirmPasswordTextField)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.registerNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.registerNameLabel.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.registerNameLabel)
        self.registerPasswordLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.registerPasswordLabel.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.registerPasswordLabel)
        self.registerConfirmPasswordLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.registerConfirmPasswordLabel.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.registerConfirmPasswordLabel)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_3)
        self.registerButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.registerButton.setStyleSheet("")
        self.registerButton.setObjectName("registerButton")
        self.registerButton.setGeometry(QtCore.QRect(260, 290, 170, 60))
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.registerButton)
        self.backButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.backButton.setStyleSheet("")
        self.backButton.setObjectName("backButton")
        self.backButton.setGeometry(QtCore.QRect(260, 290, 170, 60))
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.backButton)
        self.stackedWidget.addWidget(self.page_register)


        self.page_login = QtWidgets.QWidget()
        self.page_login.setStyleSheet("*{\n"
                                      "font: Roboto 20pt \"Brush Script MT\";\n"
                                      "color : brown;\n"
                                      "background: transparent\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton\n"
                                      "\n"
                                      "{\n"
                                      "background-color : rgb(85, 0, 0, 0.7);\n"
                                      "}\n"
                                      "\n"
                                      "QLabel\n"
                                      "{\n"
                                      "color: yellow\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit{\n"
                                      "background-color : rgb(85, 0, 0, 0.7);\n"
                                      "color:white;\n"
                                      "}")
        self.page_login.setObjectName("page_login")
        self.frame = QtWidgets.QFrame(self.page_login)
        self.frame.setGeometry(QtCore.QRect(10, 10, 491, 391))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.login_button = QtWidgets.QPushButton(self.frame)
        self.login_button.setGeometry(QtCore.QRect(70, 290, 170, 60))
        self.login_button.setStyleSheet("")
        self.login_button.setObjectName("login_button")
        self.to_register_button = QtWidgets.QPushButton(self.frame)
        self.to_register_button.setGeometry(QtCore.QRect(260, 290, 170, 60))
        self.to_register_button.setStyleSheet("")
        self.to_register_button.setObjectName("to_register_button")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 70, 181, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.loginNameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.loginNameLabel.setStyleSheet("")
        self.loginNameLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.loginNameLabel.setObjectName("label_2")
        self.verticalLayout.addWidget(self.loginNameLabel)
        self.loginPasswordLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.loginPasswordLabel.setStyleSheet("")
        self.loginPasswordLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.loginPasswordLabel.setObjectName("label")
        self.verticalLayout.addWidget(self.loginPasswordLabel)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(220, 70, 211, 151))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")


        self.login_name = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.login_name.setStyleSheet("")
        self.login_name.setObjectName("login_name")
        self.verticalLayout_2.addWidget(self.login_name)
        self.login_password = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.login_password.setStyleSheet("")
        self.registerButton.setGeometry(QtCore.QRect(260, 290, 170, 60))
        self.login_password.setObjectName("login_password")
        self.login_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout_2.addWidget(self.login_password)
        self.stackedWidget.addWidget(self.page_login)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.to_register_button.clicked.connect(self.to_register_page)
        self.registerButton.clicked.connect(self.to_home_page)
        self.login_button.clicked.connect(self.check_info)
        self.backButton.clicked.connect(self.to_back)

        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS USERS(ID INTEGER NOT NULL PRIMARY KEY, USERNAME TEXT, PASSWORD TEXT)")
        conn.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.registerNameLabel.setText(_translate("MainWindow", "Username: "))
        self.registerNameLabel.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
        self.registerPasswordLabel.setText(_translate("MainWindow", "Password:"))
        self.registerPasswordLabel.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
        self.registerConfirmPasswordLabel.setText(_translate("MainWindow", "Confirm Password:"))
        self.registerConfirmPasswordLabel.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
        self.registerButton.setText(_translate("MainWindow", "Register"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.to_register_button.setText(_translate("MainWindow", "Register"))
        self.loginNameLabel.setText(_translate("MainWindow", "USERNAME :"))
        self.loginPasswordLabel.setText(_translate("MainWindow", "PASSWORD :"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        
    def to_register_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def to_back(self):
        self.stackedWidget.setCurrentIndex(1)

    def check_username(self, username):
        conn = sqlite3.connect("data.db")
        curr = conn.cursor()
        curr.execute("SELECT USERNAME FROM USERS")
        usernames = curr.fetchall()
        conn.close()
        for name in usernames:
            if username == name[0]:
                return False
        return True

    def to_home_page(self):
        _translate = QtCore.QCoreApplication.translate
        if self.registerNameTextField.text() == "" or self.registerPasswordTextField.text() == "" or self.registerConfirmPasswordTextField.text() == "":
            msg = QtWidgets.QMessageBox()
            msg.setText(_translate("MainWindow", "You must fill all lines !!!"))
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            x = msg.exec_()
        elif self.registerPasswordTextField.text() != self.registerConfirmPasswordTextField.text():
            msg = QtWidgets.QMessageBox()
            msg.setText(_translate("MainWindow", "Passwords didn't match !!!"))
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            x = msg.exec_()
        elif not self.check_username(self.registerNameTextField.text()):
            msg = QtWidgets.QMessageBox()
            msg.setText(_translate("MainWindow", "Username already taken !!!"))
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            x = msg.exec_()
        else:
            conn = sqlite3.connect("data.db")
            conn.execute("INSERT INTO USERS(USERNAME,PASSWORD) values(?,?)",
                         (self.registerNameTextField.text(), self.registerPasswordTextField.text(),))
            conn.commit()
            conn.close()
            self.stackedWidget.setCurrentIndex(1)
    

    def check_info(self):
        _translate = QtCore.QCoreApplication.translate
        conn = sqlite3.connect("data.db")
        curr = conn.cursor()
        curr.execute("SELECT * FROM USERS")
        user_list = curr.fetchall()
        conn.close()
        flag = False
        for item in user_list:
            if item[1] == self.login_name.text() and item[2] == self.login_password.text():
                global k_id
                k_id = item[0]
                print("login sayfasi item[0] = ",item[0])
                print("login sayasi k_id =",k_id)
                flag = True
                self.mainWindow = QtWidgets.QMainWindow()
                self.ui = maintodo()
                gonder(k_id)
                self.ui.setupUi(self.mainWindow)
                self.mainwindow.hide()
                self.mainWindow.show()
                break
        if not flag:
            msg = QtWidgets.QMessageBox()
            msg.setText(_translate("Login", "Username and pasword didn't match !!!"))
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle(_translate("Login", "Login Error!"))
            x = msg.exec_()
        
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    list = ["Türkçe", "English"]
    t = QtCore.QTranslator()
    lang = QtWidgets.QInputDialog.getItem(MainWindow, "Select Language", "Language:", list)
    if lang[0] == "Türkçe":
        t.load("turkish.qm")
        app.installTranslator(t)

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



