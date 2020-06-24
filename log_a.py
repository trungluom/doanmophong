import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from log_b import *
import csv


class Login(QDialog):
    """User login """
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_login_form()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(lambda: self.handle_login(servers=servers))
        servers = {}
        with open('servers.csv', newline='') as csvfile:
            server_reader = csv.reader(csvfile)
            for row in server_reader:
                self.ui.cbo_db_name.addItem(row[1])
                servers[row[1]] = (row[0],row[2],row[3])


    def handle_login(self, servers=''):
        the_key = self.ui.cbo_db_name.currentText()
        self.server = servers[the_key][0]


if __name__=="__main__":
    app=QApplication(sys.argv)
    access = Login()
    access.exec_()
    print(access.server)

    myapp = Test_form()
    myapp.show()
    sys.exit(app.exec_())