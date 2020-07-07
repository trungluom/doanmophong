from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import  sys
from login_main import *
# from login_main_1 import *
class dk_log(QMainWindow):    

    def __init__(self, parent=None):
        # call QWidget constructor
        super(dk_log, self).__init__()
        self.ui = Ui_Form()
        self.ui.setup(self)
        # self.image = QImage()
        # self.image2 = QImage()
        self.ui.pushButton.clicked.connect(self.close)
        # self.ui.pushButton.clicked.connect(self.close)

    def close():
    	self.hide()



if __name__ == "__main__":
    app = QApplication(sys.argv)				
    w=dk_log()
    w.show()
    sys.exit(app.exec_())
        
