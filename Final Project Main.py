# IMPORTS
import time
from PIL import Image
import numpy as np
import pyautogui as gui
from ChooseColor import choosecolor


#opening image and getting 3d RGB pixel information    
im = Image.open('Colorwheel.jpg')
pixels = np.array(im)

# rep is the varible defining how compressed we want the image. can be between 2-6, the higher rep is the less pixellation
rep = 5
x = 0
while x <= rep:
    print(len(pixels), len(pixels[1]))
    pixels = np.delete(pixels, list(range(0, len(pixels), 2)), axis = 0)
    pixels = np.delete(pixels, list(range(0, pixels.shape[1], 2)), axis = 1)
    x += 1

#print(len(pixels), len(pixels[1]))

# Rough calculation of how long the program will take with a 
seconds = (len(pixels) * len(pixels[1])) + 7
minutes = (seconds*2) / 60
minutes = str(minutes)
minutes = minutes[0:4]
gui.alert(text='This drawing will take roughly'+ '\n' + minutes + ' minutes', 
          title='Program Information', button='Begin Drawing')
time.sleep(1)



column = 5  #column begins at 5 to avoid the program writing off screen for the first few pixels
row = 0
for pixel in pixels:
    while (column - 5) <= len(pixels[1]):
        for cell in pixel:
            choosecolor(cell[0], cell[1], cell[2])
            time.sleep(.2)
            gui.click(column, row + 300, clicks = 2)                
            column+=1
    row += 1
    column = 5

gui.alert(text='Drawing Complete', title='Program Information', button='End Program')









