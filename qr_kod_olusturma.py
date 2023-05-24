from typing import Text
from gtts import gTTS
import os
import qrcode

data=qrcode.make("""Parol
Parol Tabletin aktif maddesi parasetamol, klinik olarak kanıtlanmış, analjezik ve
antipiretik etkili bir ilaçtır. Hipotalamustaki termoregülasyon merkezi üzerindeki etkisi
ile antipiretik etki gösterir. Parasetamol, prostaglandin sentezini önler. Gastrointestinal
sistemden hızla absorbe olur. Parol, analjezik ve antipiretik etkilerini 15-30 dakikada ve 3-4
saat süreyle gösterir. soğuk algınlığı, influenza ve diğer bakteriyel ve viral
enfeksiyonlar da ise hem analjezik hem de antipiretik etki gösterir.
Kontrendikasyonları:Anemili veya kardiyak, pulmoner, renal ya da hepatik hastalıkları olan kiĢilerde doktor
kontrolü olmadan kullanılmamalıdır.""")

data.save("deneme.png")
