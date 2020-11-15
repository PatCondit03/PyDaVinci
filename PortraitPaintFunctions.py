import pyautogui as gui
import random as r
import time
# early definition of the distance variable **why is this here**
distance = 200

# color_horiz_location is the horizontal location of the color grids
# color_horiz_location = [1090, 1123, 1153, 1189, 1223, 1255, 1290, 1323, 1353, 1390]
# definition of all colors with their location in MS Paint
all_colors_xy = {
    'black': (1090, 100),
    'light_gray': (1123, 120),
    'gray': (1123, 100),
    'white': (1090, 120),
    'red': (1189, 100),
    'maroon': (1153, 100),
    'orange': (1223, 100),
    'light_orange': (1223, 120),
    'yellow': (1255, 100),
    'brown': (1153, 120),
    'pink': (1189, 120),
    'peach': (1255, 120),
    'green': (1290, 100),
    'light_green': (1290, 120),
    'blue': (1353, 100),
    'light_blue': (1323, 100),
    'sky': (1323, 120),
    'navy': (1353, 120),
    'purple': (1390, 100),
    'light_purple': (1390, 120)
    }


def create_portrait_theme():
    current_colors_xy = {}
    colors_desired = ['green', 'black', 'white', 'gray', 'light_gray']
    for color in colors_desired:
        current_colors_xy[color] = all_colors_xy[color]
    return(current_colors_xy)
    


def select_brush(brush_type):
    brush_types_xy = {
        'default brush': (475, 200),
        'calligraphy brush 1': (525, 200),
        'calligraphy brush 2': (600, 200),
        'airbrush': (650, 200),
        'oil brush': (475, 250),
        'crayon': (525, 250),
        'marker': (600, 250),
        'natural pencil': (650, 250),
        'oil brush': (475, 250),
        'watercolor brush': (475, 300),
        }
    brushes_xy = (475, 150)
    gui.click(brushes_xy)
    a, b = brush_types_xy[brush_type]
    gui.click(a, b, 2, .3)
    return(brush_type)
    
    
    
    
def select_size(size):
    sizes_options_xy = {
        'small': (900, 200),
        'medium small': (900, 250),
        'medium large': (900, 325),
        'large': (900, 375)
        }
    sizes_xy = (900, 150)
    gui.click(sizes_xy)
    a, b = sizes_options_xy[size]
    gui.click(a, b, 2, .3)
    

# function to draw a horizontal line
def horizontalLine(current_colors_xy, canvas_width, canvas_height, horizon):
    #place,  row = current_colors_xy['green']
    #gui.click(place, row, 2, 0.2)
    # added the two variables and loops below to ensure that the lines being drawn are long enough to look decent
    length = r.randint(-900,900)
    cont = True
    while cont is True:
        if length>300 or length<-300:
            a, b = canvas_height
            gui.click(r.randint(0,canvas_width),r.randint(horizon, b))
            gui.dragRel(length, 0)
            cont = False
        else:
            length = r.randint(-900,900)
    
    
    
    
# function to draw a vertical line
def verticalLine(current_colors_xy, canvas_width, canvas_height):
    name, (place,  row) = r.choice(list(current_colors_xy.items()))
    gui.click(place, row, 2, 0.2)
    # ^^ choose a color
    ## added the two variables and loops below to ensure that the lines being drawn are long enough to look decent
    length = r.randint(-600,600)
    cont = True
    while cont is True:
        if length>200 or length<-200:
            a, b = canvas_height
            gui.click(r.randint(0,canvas_width),r.randint(a, b))
            gui.dragRel(0, length)
            cont = False
        else:
            length = r.randint(-600,600)
            
            
            
            
def landscapeline(current_colors_xy, canvas_width, canvas_height, size, color):
    select_size(size)
    place,  row = current_colors_xy[color]
    gui.click(place, row, 2, 0.2)
    
    