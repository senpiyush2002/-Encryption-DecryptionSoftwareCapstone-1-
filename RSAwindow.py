import sys
import os
import os.path
from os import listdir
from os.path import isfile, join
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QFileDialog, QVBoxLayout
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class Encryptor:
    def rsa_enc(self, message,dir):
        
        public_key = RSA.import_key(open('public.pem').read())
        cipher = PKCS1_OAEP.new(public_key)
        encrypted_message = cipher.encrypt(message.encode())
        filename='encrypted'
        pathtosave = str(dir+"/"+ filename+".txt")      
        file1 = open(pathtosave, "wb")
        file1.write(encrypted_message) 
        file1.close() 

    def rsa_dec(self, filepath,private_key_path):
        print(private_key_path)
        with open(private_key_path, "rb") as k:
         private_key = RSA.importKey(k.read())
        cipher = PKCS1_OAEP.new(private_key)
        with open(filepath, 'rb') as fo:
            encrypted_message = fo.read()
        decrypted_message = cipher.decrypt(encrypted_message)
        print(decrypted_message)
        return str(decrypted_message.decode())
        

class Ui_RSA_window(QWidget):
    
    def getfile1(self):
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select an encrypted file',
            directory=os.getcwd(),
            filter='',
            initialFilter=''
        )
        response=str(response)
        response=response[2:-19]
        self.T2.setText(response)
        return response[0]
    
    def getfile2(self):
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select private key',
            directory=os.getcwd(),
            filter='',
            initialFilter=''
        )
        response=str(response)
        response=response[2:-19]
        self.T3.setText(response)
        return response[0]
    
    def encr(self):
        dir_name = QFileDialog.getExistingDirectory(self, "Select a Directory")
        path = Path(dir_name)
        dir=str(path)    
        message = self.TextBox1.toPlainText()
        enc=Encryptor()
        enc.rsa_enc(message,dir)
    
    def decr(self):
        encrypted_path= self.T2.toPlainText()
        private_key_path= self.T3.toPlainText()
        enc=Encryptor()
        decrypted_message=enc.rsa_dec(encrypted_path,private_key_path)
        self.T4.setText(decrypted_message)
    
    

    def setupUi(self, RSA_window):
        RSA_window.setObjectName("RSA_window")
        RSA_window.resize(722, 721)
        self.pushButton = QtWidgets.QPushButton(RSA_window)
        self.pushButton.setGeometry(QtCore.QRect(260, 170, 201, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.encr)
        self.TextBox1 = QtWidgets.QTextEdit(RSA_window)
        self.TextBox1.setGeometry(QtCore.QRect(110, 40, 501, 131))
        self.TextBox1.setObjectName("TextBox1")
        self.T2 = QtWidgets.QTextEdit(RSA_window)
        self.T2.setGeometry(QtCore.QRect(110, 270, 501, 81))
        self.T2.setObjectName("T2")
        self.T3 = QtWidgets.QTextEdit(RSA_window)
        self.T3.setGeometry(QtCore.QRect(110, 400, 501, 81))
        self.T3.setObjectName("T3")
        self.label = QtWidgets.QLabel(RSA_window)
        self.label.setGeometry(QtCore.QRect(330, 10, 71, 31))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(RSA_window)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 350, 201, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.getfile1)
        self.pushButton_3 = QtWidgets.QPushButton(RSA_window)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 480, 201, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.getfile2)
        self.label_2 = QtWidgets.QLabel(RSA_window)
        self.label_2.setGeometry(QtCore.QRect(330, 240, 101, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(RSA_window)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 660, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.decr)
        self.T4 = QtWidgets.QTextEdit(RSA_window)
        self.T4.setGeometry(QtCore.QRect(110, 520, 501, 131))
        self.T4.setObjectName("T4")

        self.retranslateUi(RSA_window)
        QtCore.QMetaObject.connectSlotsByName(RSA_window)

    def retranslateUi(self, RSA_window):
        _translate = QtCore.QCoreApplication.translate
        RSA_window.setWindowTitle(_translate("RSA_window", "RSA_window"))
        self.pushButton.setText(_translate("RSA_window", "Encrypt and Choose a Folder"))
        self.label.setText(_translate("RSA_window", "Encryption"))
        self.pushButton_2.setText(_translate("RSA_window", "Choose Encrypted Message"))
        self.pushButton_3.setText(_translate("RSA_window", "Choose Private Key"))
        self.label_2.setText(_translate("RSA_window", "Decryption"))
        self.pushButton_4.setText(_translate("RSA_window", "Decrypt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RSA_window = QtWidgets.QWidget()
    ui = Ui_RSA_window()
    ui.setupUi(RSA_window)
    RSA_window.show()
    sys.exit(app.exec_())
