import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
class MainForm(QWidget):
            def __init__(self):
                self.Qt = QWidget()
                QWidget.__init__(self, flags=Qt.Widget)

                self.tbw = QTabWidget()
                self.init_widget()

            def init_widget(self):
                self.setWindowTitle("POS_DB_Browser")

                self.resize(800, 600)
                self.setMinimumSize(800,600)
                self.setMaximumSize(800,600)

                form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
                self.setLayout(form_lbx)
                form_lbx.addWidget(self.tbw)

class Ui_LoginFrom(object):
   def setupUi(self, LoginFrom):
            LoginFrom.setObjectName("LoginFrom")
            LoginFrom.resize(350, 280)
            LoginFrom.setMinimumSize(QtCore.QSize(350, 280))
            LoginFrom.setMaximumSize(QtCore.QSize(350, 280))
            LoginFrom.setSizeIncrement(QtCore.QSize(350, 280))
            LoginFrom.setBaseSize(QtCore.QSize(350, 280))
            LoginFrom.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.RepublicOfKorea))
            LoginFrom.setFrameShape(QtWidgets.QFrame.StyledPanel)
            LoginFrom.setFrameShadow(QtWidgets.QFrame.Raised)
   def login(self):
        server = self.ServerIp.text()
        user = self.ID.text()
        pw = self.Password.text() 
        db = self.Database.text()
        try:
            self.sdb = QSqlDatabase.addDatabase('testdb')
            self.sdb.setHostName(server)
            self.sdb.setDatabaseName(db)
            self.sdb.setUserName(user)
            self.sdb.setPassword(pw)
            estado = self.sdb.open()
            if estado==False:
                QMessageBox.warning(self,"Error",self.db.lastError().text(),QMessageBox.Discard)
            else:
                dialog = QtWidgets.QDialog()
                dialog = MainForm()
                dialog.show()

        except:
            QMessageBox.warning(self, "Error", self.db.lastError().text(), QMessageBox.Discard)
if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = MainForm()
    form.show()

    sys.exit(app.exec_())
