import time
import pyautogui
import random

time.sleep(4)
distance = 200
pyautogui.click(477,412)

#list of all the locations of colors in MS Paint
colorlist = [1090, 1123, 1153, 1189, 1223, 1255, 1290, 1323, 1353, 1390]

rows = [100, 120]

# function to draw a square shaped spiral
def squarespiral():
    pyautogui.click(colorlist[random.randint(0,9)], rows[random.randint(0,1)], 2, 0.2)
    pyautogui.click(random.randint(0,1880),random.randint(200, 756))
    distance = random.randint(20,300)
    increment = random.randint(4,10)
    while distance > 0:
        pyautogui.dragRel(distance, 0)   # move right
        distance -= increment
        pyautogui.dragRel(0, distance)   # move down
        pyautogui.dragRel(-distance, 0)  # move left
        distance -= increment
        pyautogui.dragRel(0, -distance)  # move up
        
# function to draw a square
def square():
    pyautogui.click(colorlist[random.randint(0,9)], rows[random.randint(0,1)], 2, 0.2)
    pyautogui.click(random.randint(0,1700),random.randint(300, 700))
    distance = random.randint(1,300)
    pyautogui.dragRel(distance, -distance)   # move right
    pyautogui.dragRel(distance, distance)   # move down
    pyautogui.dragRel(-distance, distance)  # move left
    pyautogui.dragRel(-distance, -distance)  # move up

# function to draw a line
def line():
    pyautogui.click(colorlist[random.randint(0,9)], rows[random.randint(0,1)], 2, 0.2)
    pyautogui.click(random.randint(0,1880),random.randint(200, 756))
    pyautogui.dragRel(random.randint(-300,300), random.randint(-300,300))
    
# function to choose the "fill" tool and fill in the area clicked with a color
def click():
    pyautogui.click(379,110)
    pyautogui.click(random.randint(0,1880),random.randint(200, 756))
    pyautogui.click(345,110)

x = 1
count = 0


'''
# This section is commented out becuase it is an alternative method of drawing.
# Essentially, the loops are skewed so that ceratin functions are used more often
#   than others for a different style of drawing


while count < 100:
    choice = random.randint(1,10)
    if choice == 1:
        click()
        count = count + 1
    elif choice == 2:
        square()
        count = count + 1
    elif choice == 3:
        line()
        count = count + 1
    else:
        squarespiral()
        count = count +1
while count >=100:
    choice = random.randint(1,10)
    if choice == 1:
        squarespiral()
        count = count + 1
    elif choice == 2:
        square()
        count = count + 1
    elif choice == 3:
        line()
        count = count + 1
    else:
        click()
        count = count +1
'''

# working code, loop will have the program commit 200 actions        
while count < 200:
    choice = random.randint(1,10)
    if choice == 1:
        click()
        count = count + 1
    elif choice == 2:
        squarespiral()
        count = count + 1
    elif choice == 3:
        line()
        count = count + 1
    else:
        square()
        count = count +1
        
# After the above 200 actions, it will do 100 click functions to try and have a more common color
while count >=200 and count <= 300:
        click()
        count = count +1        
        
        
