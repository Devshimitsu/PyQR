import pyqrcode 
import png 
from pyqrcode import QRCode 


# String which represents the QR code 
s = input("\nEnter Text Or Url Here: ")

# Generate QR code 
url = pyqrcode.create(s) 

print("\n[1] .svg")
print("[2] .png")

option=input("\nSelect An Option: ")

if option == "1":
	# Create and save the svg file naming "myqr.svg" 
	url.svg("myqr.svg", scale=8)

elif option == "2":
	# Create and save the png file naming "myqr.png" 
	url.png("myqr.png", scale=8)

else:
	print("\nWrong Option !")


# BY DEVSHIMITSU