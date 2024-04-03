# 1. Atver "Terminal" logu (Terminal -> New Terminal) un ielādē bibliotēku "qrcode" ar komandas palidzību
# > pip3 install qrcode
# 
# 2. Palaid kodu, nolasi kodu ar sava telefona kameru
#
# 3. Pamaini kodu lai teksts būtu prasīts no lietotāja (input())
#
# 4. Izmantojot bibliotēkas dokumentāciju, uzraksti kodu lai tiktu ģenerēts QR kods ar šādiem parametriem:
# https://github.com/lincolnloop/python-qrcode
# - teksts tiek prasīts no lietotāja
# - border izmērs - 5
# - koda izmērs - 20
# - kļūdu labojums - Q
# - stils - vertikāls gradients (VerticalGradiantColorMask)
#


import os
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import VerticalGradiantColorMask

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data('Some data')

img = qr.make_image(image_factory=StyledPilImage, color_mask=VerticalGradiantColorMask())

img.save("qrcode.png")
os.startfile("qrcode.png")