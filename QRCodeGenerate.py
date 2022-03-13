import pyqrcode
import png
from pyqrcode import QRCode

url = str(input("Enter Link: "))
qr = pyqrcode.create(url)
file = input("Enter Filename: ")
png = ".png"
new_file = file+png
qr.png(new_file, scale=6)