import sys
from PyQt5.QtWidgets import QDialog, QApplication

from add import *

class myform(QDialog):
	"""docstring for myform"""
	def __init__(self):
		super(myform, self).__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.sum)
		self.show()
	def sum(self):
		num1=self.ui.lineEdit.text()
		num2=self.ui.lineEdit_2.text()
		x=int(num1)
		y=int(num2)
		z=x+y
		self.ui.lineEdit_3.setText('sum is'+str(z))
if __name__ == '__main__':
	app = QApplication(sys.argv)
	w=myform()
	w.show()
	sys.exit(app.exec_())