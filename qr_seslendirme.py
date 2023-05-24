
from pyzbar import pyzbar 
from PIL import Image

qr=pyzbar.decode(Image.open("deneme2.png"))
print( qr[0].data.decode('utf-8'))
data = qr[0].data.decode('utf-8')

text = data

language = 'tr'

speech = gTTS(text = text, lang = language, slow = False)

speech.save("text.mp3")

os.system("start text.mp3")
