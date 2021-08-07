import pyqrcode
import png
from pyqrcode import QRCode

# receives string from user
name = input("Enter url: ")

s = "" + name
  
# Generate QR code
url = pyqrcode.create(s)
  
# # Create and save the svg file naming "myqr.svg"
# url.svg("myqr.svg", scale = 8)

# Create and save the png file naming "myqr.png"
url.png('output.png', scale = 6)

