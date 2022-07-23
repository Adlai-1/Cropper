from PIL import Image
import os

left = "Provide your starting point for croping from the left-side of your image."
right = "Provide your starting point for croping from the right-side of your image."
top = "Provide your starting point for croping from the top of your image."
bottom = "Provide your starting point for croping from the bottom of your image."

def Crop(file:str):
    img = Image.open(file)
    img = img.crop( (left, top, right, bottom) )
    img.save(file)

dir = 'Your directory Path here!'
Images = os.listdir(dir) # sets Images as a list of all image files found in the provided directory.

for a in range(len(Images)):
    try:
        Crop(dir+'/'+Images[a])
    except:
        print('No Files')