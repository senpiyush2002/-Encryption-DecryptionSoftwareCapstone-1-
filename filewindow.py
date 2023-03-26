import sys
import os
import os.path
from os import listdir
from os.path import isfile, join
import time
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QFileDialog, QVBoxLayout
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Crypto import Random
from Crypto.Cipher import AES

class Encryptor:
    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    def encrypt_file(self, file_path,filename,dir):
        key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
        with open(file_path, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, key)
        pathtosave = str(dir+"/"+ filename+".enc")   
        print(pathtosave)    
        file1 = open(pathtosave, "wb")
        file1.write(enc) 
        file1.close() 

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self, file_path,filename,dir):
        key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
        with open(file_path, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, key)
        pathtosave = str(dir+"/"+ filename[:-4])   
        print(pathtosave)    
        file2 = open(pathtosave, "wb")
        file2.write(dec) 
        file2.close() 
     
class Ui_File_Encryption_Decryption(QWidget):
    
    def getfileEN(self):
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter='',
            initialFilter=''
        )
        enc=Encryptor()
        response=str(response)
        response=response[2:-19]
        dir,filename = os.path.split(response)      
        enc.encrypt_file(response,filename,dir)
        return response[0]
    
    def getfileDE(self):
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter='',
            initialFilter=''
        )
        response=str(response)
        response=response[2:-19]
        dir,filename = os.path.split(response)
        enc=Encryptor()
        enc.decrypt_file(response,filename,dir)
        return response[0]
    
    

    def setupUi(self, File_Encryption_Decryption):
        File_Encryption_Decryption.setObjectName("File_Encryption_Decryption")
        File_Encryption_Decryption.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(File_Encryption_Decryption)
        self.pushButton.setGeometry(QtCore.QRect(140, 67, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.getfileEN)
        self.pushButton_2 = QtWidgets.QPushButton(File_Encryption_Decryption)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 180, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.getfileDE)
        self.label = QtWidgets.QLabel(File_Encryption_Decryption)
        self.label.setGeometry(QtCore.QRect(140, 20, 111, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(File_Encryption_Decryption)
        self.label_2.setGeometry(QtCore.QRect(10, 250, 301, 51))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(File_Encryption_Decryption)
        self.label_3.setGeometry(QtCore.QRect(140, 120, 111, 41))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(File_Encryption_Decryption)
        QtCore.QMetaObject.connectSlotsByName(File_Encryption_Decryption)

    def retranslateUi(self, File_Encryption_Decryption):
        _translate = QtCore.QCoreApplication.translate
        File_Encryption_Decryption.setWindowTitle(_translate("File_Encryption_Decryption", "File Encryption/Decryption"))
        self.pushButton.setText(_translate("File_Encryption_Decryption", "Choose a File"))
        self.pushButton_2.setText(_translate("File_Encryption_Decryption", "Choose a File"))
        self.label.setText(_translate("File_Encryption_Decryption", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Encrypt</span></p></body></html>"))
        self.label_2.setText(_translate("File_Encryption_Decryption", "Note: Uses AES for File Encryption and Decryption"))
        self.label_3.setText(_translate("File_Encryption_Decryption", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Decrypt</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    File_Encryption_Decryption = QtWidgets.QWidget()
    ui = Ui_File_Encryption_Decryption()
    ui.setupUi(File_Encryption_Decryption)
    File_Encryption_Decryption.show()
    sys.exit(app.exec_())
