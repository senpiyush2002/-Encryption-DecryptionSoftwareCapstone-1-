from tkinter import *
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import base64
from Crypto.Cipher import DES3

key = b'chocolatevanillacherryla'  # 24-byte key
iv = b'myiv1234'  # 8-byte iv

# ding the plaintext using PKCS#5 padding
def pad(text):
    return text + (8 - len(text) % 8) * chr(8 - len(text) % 8)

# Triple DES in CBC mode
def encrypt(plaintext):
    plaintext = pad(plaintext)
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext.encode())
    return base64.b64encode(ciphertext).decode()

def unpad(text):
    pad = ord(text[-1])
    return text[:-pad]

def decrypt(ciphertext):
    ciphertext = base64.b64decode(ciphertext)
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext).decode()
    plaintext = unpad(plaintext)
    return plaintext


root = Tk()
root.geometry("400x450")
root.title(" 3-DES ")

def Take_input1():
	INPUT = inputtxt.get("1.0", "end-1c")
	print(INPUT)
	user_input=(str(INPUT))
	encrypted_text = encrypt(user_input)
	Output.insert(END, str(encrypted_text))
def Take_input2():
	INPUT = inputtxt.get("1.0", "end-1c")
	print(INPUT)
	user_input=(str(INPUT))
	encrypted_text = user_input
	plaintext = decrypt(encrypted_text)
	Output.insert(END, plaintext)
	
inputtxt = Text(root, height = 10,
				width = 25,
				bg = "light yellow")

Output = Text(root, height = 5,
			width = 25,
			bg = "light cyan")

Display1 = Button(root, height = 2,
				width = 20,
				text ="Encrypt",
				command = lambda:Take_input1())
Display2 = Button(root, height = 2,
				width = 20,
				text ="Decrypt",
				command = lambda:Take_input2())

inputtxt.pack()
Display1.pack()
Display2.pack()
Output.pack()

mainloop()