'''
CODE FOR MAKE A RESIZE IMAGES FOR ANOTHER CODES
'''
from PIL import ImageTk, Image
import base64

def img_resize_encode():
    img = Image.open(r"C:\Users\joaop\Downloads\Image13-removebg-preview.png")

    new_img = img.resize((300,100), Image.ANTIALIAS)

    new_img.save('newlogopic.png')

    # return base64.b64encode('newlogopic.png')

print(img_resize_encode())