# Defining the function to choose color, with RGB as inputs


import pyautogui as gui
def choosecolor(R, G, B):
    gui.click(1440, 110)
    
    gui.click(1260, 630)
    gui.press('backspace', presses = 3)
    for c in str(R):
        gui.press(c)
        
    gui.click(1260, 670)
    gui.press('backspace', presses = 3)
    for c in str(G):
        gui.press(c)
        
    gui.click(1260, 690)
    gui.press('backspace', presses = 3)
    for c in str(B):
        gui.press(c)
    
    gui.press('enter')