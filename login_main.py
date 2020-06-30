# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
        # ("SELECT NAME, PHONE FROM PS_INFO WHERE NAME='" | Quote(&UserInput) | "'", &Name, &Phone)
        #==================================MYSQL=========================================================
        # mydb = mysql.connector.connect(host="localhost",user="root",  passwd="tl200298",  database="testdb")     
        # mycursor = mydb.cursor()
        # query="select * from users1 where username=%s and password=%s"
        # query="select * from testdb.users where username=self.username and password=self.password"
from PyQt5 import QtCore, QtGui, QtWidgets
# import mysql.connector
import cx_Oracle
import sys
from giao_dien_admin import *

class Ui_Form(object):
    # def __init__(self, parent=None):
    #     # call QWidget constructor
    #     super(Ui_Form, self).__init__()
    #     self.log = Ui_Form()
    #     self.log.setup(self)
        
    def login(self):
        user=self.lineEdit.text()
        passwd=self.lineEdit_2.text()
        username=str(user)
        password=str(passwd)
        #=================================SQL============================================================
        conn = cx_Oracle.connect('testdb/123@//localhost:1521/xe') # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
        mycursor = conn.cursor()
        query="SELECT * FROM testdb.users WHERE username=:username and passwords=:passwords"
        mycursor.execute(query,username=username,passwords=password)
        data = mycursor.fetchall()
        print(mycursor)
        if (len(data)>0):
            self.window=QtWidgets.QMainWindow()
            self.ui=Ui_MainWindow()
            self.ui.giaodien_admin(self.window)
            self.window.show()
            # self.app.hide()
            # print('thanh cong')          
            pass
            # self.messagebox("Congrats", "you are logged in")
        else:
            # self.warning("alert","enter correct details")
            # self.login_event
            print('that bai')
        pass
    def login_event(self,event):
        reply = QMessageBox.question(self,'Login','Login fail, try again!',
                QMessageBox.Yes | QMessageBox.No,QMessageBox)
        if reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

        pass
    def setup(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 400)
        Form.setMinimumSize(QtCore.QSize(300, 400))
        Form.setMaximumSize(QtCore.QSize(300, 400))
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 130, 202, 171))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(130, 20))
        self.lineEdit.setMaximumSize(QtCore.QSize(130, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText('Please enter your username')
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        

        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(130, 20))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(130, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setPlaceholderText('Please enter your password')
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.LabelRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 50, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 310, 201, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(80, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.login)
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Username:"))
        self.label_2.setText(_translate("Form", "Password:"))
        self.label_3.setText(_translate("Form", "Đăng nhập để tiếp tục."))
        self.pushButton.setText(_translate("Form", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setup(Form)
    Form.show()
    sys.exit(app.exec_())
