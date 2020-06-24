### File giao_dien
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# from PyQt5.QtCore import QTimer,QByteArray, QDir
import  sys
import mysql.connector
from open import  *
from login_main import *
# from dk_log import *
from login_main_1 import *
class Do_an(QMainWindow):
    # class constructor2
    # if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # w=Do_an()
    # w.show()
    # sys.exit(app.exec_())

    def __init__(self, parent=None):
        # call QWidget constructor
        super(Do_an, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.image = QImage()
        # self.image2 = QImage()
        self.ui.pushButton.clicked.connect(self.open)
        self.ui.pushButton_2.clicked.connect(self.open1)
        self.ui.pushButton_3.clicked.connect(self.open1)
        # self.pushButton.clicked.connect(self.login)
    def open(self):
        self.window=QtWidgets.QMainWindow()
        self.a=Ui_Form()
        self.a.setup(self.window)
        self.window.show()
        self.hide()
    def open1(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_Form1()
        self.ui.setup(self.window)
        self.window.show()
    def messagebox(self,title,message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_
    def warning(self,title,message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w=Do_an()
    w.show()
    sys.exit(app.exec_())



        # def login1(self):
    #     # print ('congrats, you are connected with database')
    #     try:
    #         b =  mysql.connector.connect(host='localhost', user='root', passwd='tl200298', database='testdb')
    #         print ('congrats, you are connected with database')
    #     except:
    #         print ('sorry, you are not connected with database')
    # def login(self):
    #     user=self.ui.lineEdit.text()
    #     passwd=self.ui.lineEdit_2.text()
    #     username=str(user)
    #     password=str(passwd)
    #     mydb = mysql.connector.connect(host="localhost",user="root",  passwd="tl200298",  database="testdb")     
    #     mycursor = mydb.cursor()
    #     # query="select * from users1 where username=%s and password=%s"
    #     query="SELECT * FROM users1 WHERE username = %s and password=%s"

    #     mycursor.execute(query,(username,password))
    #     data = mycursor.fetchall()
    #     # for x in data:
    #     #     print(x)
    #     if (len(data)>0):
    #         self.window=QtWidgets.QMainWindow()
    #         self.ui=Ui_MainWindow1()
    #         self.ui.setup(self.window)
    #         self.window.show()
    #         print('thanh cong')
    #         # self.messagebox("Congrats", "you are logged in")

    #     else:
    #         # self.warning("alert","enter correct details")
    #         print('con cac')