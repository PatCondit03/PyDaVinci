import pyautogui as gui
import random as r

# early definition of the distance variable **why is this here**
distance = 200

# color_horiz_location is the horizontal location of the color grids
# color_horiz_location = [1090, 1123, 1153, 1189, 1223, 1255, 1290, 1323, 1353, 1390]
# definition of all colors with their location in MS Paint
all_colors_xy = {
    'black': (1090, 100),
    'grey': (1123, 100),
    'maroon': (1153, 100),
    'red': (1189, 100),
    'orange': (1223, 100),
    'yellow': (1255, 100),
    'green': (1290, 100),
    'light_blue': (1323, 100),
    'blue': (1353, 100),
    'purple': (1390, 100),
    'white': (1090, 120),
    'light_grey': (1123, 120),
    'brown': (1153, 120),
    'pink': (1189, 120),
    'light_orange': (1223, 120),
    'peach': (1255, 120),
    'light_green': (1290, 120),
    'sky_blue': (1323, 120),
    'light_navy': (1353, 120),
    'light_purple': (1390, 120)
    }
fill_tool_xy = (379, 110)
pencil_tool_xy = (345, 110)
canvas_width = 1880
canvas_height = (200, 756) #we used a margin on either side of the height to avoid potential problems in the gui
 
def create_color_theme(): 
    # dictionary of color scheme selected for current painting
    current_colors_xy = {}
    # iteration variable
    count = 0
    # list of color names for color scheme selecte for current painting
    current_colors_names = []
    # a random integer is selected to determine the number of colors in the color theme for the current painting
    number_current_colors = r.randint(2 , 4)
    # black will be added to every color theme
    print(str(number_current_colors+1)+' colors chosen:\nblack')
    
    #   we add new colors to the current theme, 
    #   saving and printing the name of each until we reach number_current_colors
    while count < number_current_colors:
        name, (place, row) = r.choice(list(all_colors_xy.items()))
        current_colors_xy[name] = (place,row)
        print(name)
        current_colors_names.append(current_colors_xy[name])
        count+=1
    # as mentioned above, black is added to every theme
    current_colors_xy['black'] = (1090,100)
    # we return the dict of the current color theme to be used in the color selection function
    return(current_colors_xy)




# function to draw a square shaped spiral
def squarespiral(current_colors_xy, canvas_width, canvas_height):
    name, (place,  row) = r.choice(list(current_colors_xy.items()))
    gui.click(place, row, 2, 0.2)
    # ^^ choose a color
    gui.click(r.randint(0,canvas_width),r.randint(canvas_height))
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
    gui.click(r.randint(0,canvas_width),r.randint(canvas_height))
    gui.dragRel(r.randint(-300,300), 0)
    
# function to draw a vertical line
def verticalLine(current_colors_xy, canvas_width, canvas_height):
    name, (place,  row) = r.choice(list(current_colors_xy.items()))
    gui.click(place, row, 2, 0.2)
    # ^^ choose a color
    gui.click(r.randint(0,canvas_width),r.randint(canvas_height))
    gui.dragRel(0, r.randint(-300,300))
    
    
    
# function to choose the "fill" tool and fill in the area clicked with a color
def fill(fill_tool_xy, pencil_tool_xy, canvas_width):
    gui.click(fill_tool_xy)
    gui.click(r.randint(0,canvas_width),r.randint(canvas_height))
    gui.click(pencil_tool_xy)
    