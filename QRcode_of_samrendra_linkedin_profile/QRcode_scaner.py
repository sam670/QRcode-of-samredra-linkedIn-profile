'''
##normal QR code of a text
import qrcode as qr
img = qr.make("hello this is samrendra")
img.save("MyQRcode.png")
'''

import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10,border=4)
qr.add_data("https://www.linkedin.com/in/samrendra-vishwakarma-5505941a2/")
qr.make(fit=True)
img=qr.make_image(fill_color="black" , back_color="white")
img.save("Sam_LinkedIN_Profile.png")

