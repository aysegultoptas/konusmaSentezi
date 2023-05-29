#webcam
from __future__ import print_function

import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import time

# webcam acilir  
cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)

time.sleep(2)

def decode(im) : 
    # QR kodu bulma
    decodedObjects = pyzbar.decode(im)
    # Sonucu yazdirma
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data,'\n')     
    return decodedObjects


font = cv2.FONT_HERSHEY_SIMPLEX

while(cap.isOpened()):
    # frame frame yakalama
    ret, frame = cap.read()
    im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
         
    decodedObjects = decode(im)

    # koseli(qr kodun doğru bir sekilde algilanmasi icin) seklinde yakala
    for decodedObject in decodedObjects: 
        points = decodedObject.polygon
     
        if len(points) > 4 : 
          hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
          hull = list(map(tuple, np.squeeze(hull)))
        else : 
          hull = points;
         
        n = len(hull)     
        # Cerceveyi ciz
        for j in range(0,n):
          cv2.line(frame, hull[j], hull[ (j+1) % n], (255,0,0), 3)

        x = decodedObject.rect.left
        y = decodedObject.rect.top

        print(x, y)

        print('Type : ', decodedObject.type)
        print('Data : ', decodedObject.data,'\n')

        barCode = str(decodedObject.data)
        cv2.putText(frame, barCode, (x, y), font, 1, (0,255,255), 2, cv2.LINE_AA)
               
    # Cikti frame ini goster
    cv2.imshow('frame',frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'): # kapatmak icin 'q' a bas
        break
    elif key & 0xFF == ord('s'): # kaydetmek icin 's' e bas 
        cv2.imwrite('qr.png', frame)     
        

cap.release()
cv2.destroyAllWindows()


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


class Pencere(QtWidgets.QWidget): 

    def __init__(self):
        super().__init__()  
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet('background-color : orange')
        self.setWindowTitle("ARAYÜZ")
        self.buton = QtWidgets.QPushButton("QR KODU SESLİ OKU")
        self.buton.setStyleSheet('background-color : pink')
        self.say = 0
        global resim
        resim = QtWidgets.QLabel() 
        

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.buton)
        v_box.addWidget(resim)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)  

        self.buton.clicked.connect(self.qr_oku)  
       
        resim.setPixmap(QtGui.QPixmap("qr.png")) 
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
