import sys
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import datetime
import cv2

from pyzbar import pyzbar 
from PIL import Image
from gtts import gTTS
import os
import qrcode


class Pencere(QtWidgets.QWidget): # mirasları aldı.

    def __init__(self):
        super().__init__()  # miras aldıklarını çalıştırdık direkt.
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet('background-color : orange')
        
        self.buton = QtWidgets.QPushButton("QR KODU SESLİ OKU")
        self.buton.setStyleSheet('background-color : pink')
        self.say = 0
        global resim
        resim = QtWidgets.QLabel() # tekrar etiket oluşturduk ve bu etikete yine istediğimiz şeyi ekleyebiliriz.
        

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.buton)
        v_box.addWidget(resim)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)  #v_box u h_boxun içine attık. o yüzden h_boxu göstermelisiniz.

        self.buton.clicked.connect(self.qr_oku)  # Burada butona clicklediğinde verilen fonksiyona connectle dedik.
       
        resim.setPixmap(QtGui.QPixmap("qr.png")) #bu şekilde etikete resim ekleyebilirsiniz. Burada PyQt5 in yukarıda da import ettiğimiz QtGui fonksiyonunu kullanıyoruz.
        resim.move(140,60)
        
        self.show()

    def qr_oku(self):
        qr=pyzbar.decode(Image.open('qr.png'))
        print( qr[0].data.decode('utf-8'))
        data = qr[0].data.decode('utf-8')

        print(data)

        text = data

        language = 'tr'

        speech = gTTS(text = text, lang = language, slow = False)

        speech.save("text.mp3")

        os.system("start text.mp3")
            
app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
