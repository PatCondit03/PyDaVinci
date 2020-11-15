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

 
def create_color_theme():
    print('Color Library:')
    print('black, gray, light gray, white')
    print('red, maroon')
    print('navy, blue, light blue, sky')
    print('green, light green')
    print('orange, light orange, yellow, brown')
    print('pink, peach, purple, light purple\n')
    print('Would you like to choose your own color scheme? (y/n)')
    choice = input('>')
    if choice == 'n':
        # dictionary of color scheme selected for current painting
        current_colors_xy = {}
        # iteration variable
        count = 0
        # list of color names for color scheme selecte for current painting
        current_colors_names = []
        # a random integer is selected to determine the number of colors in the color theme for the current painting
        number_current_colors = r.randint(2 , 3)
        # black will be added to every color theme
        current_colors_xy['black'] = (1090,100)
        current_colors_names.append('black')
        print(str(number_current_colors+1)+' colors chosen:\nblack')
        #   we add new colors to the current theme, 
        #   saving and printing the name of each until we reach number_current_colors
        while count < number_current_colors:
            name, (place, row) = r.choice(list(all_colors_xy.items()))
            if name not in current_colors_names: 
                current_colors_xy[name] = (place,row)
                print(name)
                current_colors_names.append(current_colors_xy[name])
                count+=1
        # as mentioned above, black is added to every theme
        # we return the dict of the current color theme to be used in the color selection function
    else:
        current_colors_xy = {}
        passvar = 0
        while passvar == 0:
            try:
                print('\nPlease enter the colors you would like used, separated by one space. or enter exit to end program')
                colors_desired = input('>').split()
                if str(colors_desired[0]) == 'exit':
                    return('exit')
                for color in colors_desired:
                    current_colors_xy[color] = all_colors_xy[color]
                    current_colors_xy['black'] = all_colors_xy['black']
                print('success!')
                passvar = 1
            except:
                print('ERROR: could not understand your input. Lets try again.')
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
    
    
    
    

# function to draw a square shaped spiral
def squarespiral(current_colors_xy, canvas_width, canvas_height):
    name, (place,  row) = r.choice(list(current_colors_xy.items()))
    gui.click(place, row, 2, 0.2)
    # ^^ choose a color
    a, b = canvas_height
    gui.click(r.randint(0,canvas_width),r.randint(a, b))
    distance = r.randint(20,300)
    increment = r.randint(4,10)
    while distance > 0:
        gui.dragRel(distance, 0)   # move right
        distance -= increment
        gui.dragRel(0, distance)   # move down
        gui.dragRel(-distance, 0)  # move left
        distance -= increment
        gui.dragRel(0, -distance)  # move up
        
        
        
        
        
# function to draw a square diamond
def diamond(current_colors_xy, canvas_width, canvas_height):
    name, (place,  row) = r.choice(list(current_colors_xy.items()))
    gui.click(place, row, 2, 0.2)
    # ^^ choose a color
    gui.click(r.randint(0,canvas_width),r.randint(300, 700))
    distance = r.randint(1,300)
    gui.dragRel(distance, -distance)   # move right
    gui.dragRel(distance, distance)   # move down
    gui.dragRel(-distance, distance)  # move left
    gui.dragRel(-distance, -distance)  # move up



# function to draw a horizontal line
def horizontalLine(current_colors_xy, canvas_width, canvas_height):
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
            gui.dragRel(length, 0)
            cont = False
        else:
            length = r.randint(-600,600)
    
    
    
    
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
    
    
    
# function to choose the "fill" tool and fill in the area clicked with a color
def fill(current_colors_xy, fill_tool_xy, current_brush_type, canvas_width, canvas_height):
    name, (place,  row) = r.choice(list(current_colors_xy.items()))
    gui.click(place, row, 2, 0.2)
    a, b = fill_tool_xy
    gui.click(a, b)
    a, b = canvas_height
    gui.click(r.randint(0,canvas_width),r.randint(a, b))
    select_brush(current_brush_type)
    
    
    

def cut_and_paste(canvas_width, canvas_height):
    select_xy = (180, 110)
    a, b = select_xy
    gui.click(a, b, 2, .3)
    
    a, b = canvas_height
    gui.click(r.randint(0,canvas_width),r.randint(a, b))
    gui.dragRel(r.randint(-600,600), r.randint(-600,600))   
    gui.move(-30, -30)
    time.sleep(5)
    a, b = r.randint(0,100), r.randint(0,100)
    gui.click(a, b)
    gui.dragRel(a, b)

    