from PyQt5 import QtCore, QtGui, QtWidgets
from filewindow import Ui_File_Encryption_Decryption
from RSAwindow import Ui_RSA_window

class Ui_ED(object):
    def call_fileED(self):
        self.window=QtWidgets.QWidget()
        self.ui=Ui_File_Encryption_Decryption()
        self.ui.setupUi(self.window)
        self.window.show()

    def call_rsa_window(self):
        self.window=QtWidgets.QWidget()
        self.ui=Ui_RSA_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, ED):
        ED.setObjectName("ED")
        ED.resize(1133, 340)
        ED.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(ED)
        self.centralwidget.setObjectName("centralwidget")
        self.upLeft = QtWidgets.QPushButton(self.centralwidget)
        self.upLeft.setGeometry(QtCore.QRect(30, 30, 351, 111))
        self.upLeft.setStyleSheet("#upLeft {\n"
"background-color: transparent;\n"
"border-image: url(:b1.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#upLeft:pressed\n"
"{\n"
"border-image: url(:b1.png);\n"
"}")
        self.upLeft.setText("")
        self.upLeft.setObjectName("upLeft")
        self.upLeft.clicked.connect(call_des)
        self.upMiddle = QtWidgets.QPushButton(self.centralwidget)
        self.upMiddle.setGeometry(QtCore.QRect(400, 30, 361, 111))
        self.upMiddle.setStyleSheet("#upMiddle {\n"
"background-color: transparent;\n"
"border-image: url(:b2.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#upLeft:pressed\n"
"{\n"
"   border-image: url(:b2.png);\n"
"}")
        self.upMiddle.setText("")
        self.upMiddle.setObjectName("upMiddle")
        self.upMiddle.clicked.connect(call_3des)
        self.upRight = QtWidgets.QPushButton(self.centralwidget)
        self.upRight.setGeometry(QtCore.QRect(790, 30, 331, 111))
        self.upRight.setStyleSheet("#upRight {\n"
"background-color: transparent;\n"
"border-image: url(:b3.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#upRight:pressed\n"
"{\n"
"   border-image: url(:b3.png);\n"
"}")
        self.upRight.setText("")
        self.upRight.setObjectName("upRight")
        self.upRight.clicked.connect(call_aes)
        self.bottomLeft = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.call_rsa_window())
        self.bottomLeft.setGeometry(QtCore.QRect(30, 150, 351, 111))
        self.bottomLeft.setStyleSheet("#bottomLeft {\n"
"background-color: transparent;\n"
"border-image: url(:b4.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#bottomLeft:pressed\n"
"{\n"
"   border-image: url(:b4.png);\n"
"}")
        self.bottomLeft.setText("")
        self.bottomLeft.setObjectName("bottomLeft")
        self.BottomRight = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.call_fileED())
        self.BottomRight.setGeometry(QtCore.QRect(410, 150, 701, 111))
        self.BottomRight.setStyleSheet("#BottomRight {\n"
"background-color: transparent;\n"
"border-image: url(:b7.png);\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}\n"
"#BottomRight:pressed\n"
"{\n"
"   border-image: url(:b7.png);\n"
"}")
        self.BottomRight.setText("")
        self.BottomRight.setObjectName("BottomRight")
        ED.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ED)
        self.statusbar.setObjectName("statusbar")
        ED.setStatusBar(self.statusbar)

        self.retranslateUi(ED)
        QtCore.QMetaObject.connectSlotsByName(ED)

    def retranslateUi(self, ED):
        _translate = QtCore.QCoreApplication.translate
        ED.setWindowTitle(_translate("ED", "MainWindow"))
def call_des():
    import DESwindow
def call_3des():
    import TripleDES
def call_aes():
    import AESwindow

  
    

import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ED = QtWidgets.QMainWindow()
    ui = Ui_ED()
    ui.setupUi(ED)
    ED.show()
    sys.exit(app.exec_())
