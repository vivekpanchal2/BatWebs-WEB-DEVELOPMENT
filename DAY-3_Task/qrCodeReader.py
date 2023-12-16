# python code for Qrcode Reader

import cv2
from pyzbar.pyzbar import decode

# Function to read QR code
def read_qr_code(filename):
    image = cv2.imread(filename)
    decoded_objects = decode(image)

    for obj in decoded_objects:
        print("Data:", obj.data.decode("utf-8"))

# Example usage
filename = "qrcode.png"
read_qr_code(filename)