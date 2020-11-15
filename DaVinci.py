import PaintFunctions as PF
import time
import random


size_options = ['medium small','medium large','large']
brush_types_xy =['default brush','calligraphy brush 1','calligraphy brush 2',
                 'airbrush','oil brush','crayon','marker','natural pencil','oil brush',
                 'watercolor brush'
                 ]
#in this file it will draw paintings using the current and upcoming functions avaliable in PaintFunctions.py. 
fill_tool_xy = (379, 110)
pencil_tool_xy = (345, 110)
canvas_width = 1500
canvas_height = (250, 756) #we used a margin on either side of the height to avoid potential problems in the gui
#iteration variable
x = 0
while x==0:
    #maybe input a status parameter in the function call below to not have it loop back through the color scheme
    #options
    current_colors_xy = PF.create_color_theme()
    if current_colors_xy=='exit':
        x = 0
    else:
        feedback = input('Proceed with selected color scheme? (y/n) \n>')
        if feedback == 'y':
            x = 10
while x > 0:
    print(x)
    x = x-1
    time.sleep(1)
print('Painting started')
###################### CHANGE
try:
    # Painting types: Oil, crayon simple
    
    current_brush_type = PF.select_brush(random.choice(brush_types_xy))   
          
    count = 0
    while count < 300:
        choice = random.randint(1,15)
        if choice < 2:
            PF.fill(current_colors_xy, fill_tool_xy, current_brush_type, canvas_width, canvas_height)
            count = count + 1
        elif choice < 4:
            PF.select_size(random.choice(size_options))
            count = count + 1
        elif choice < 5:
            current_brush_type = PF.select_brush(random.choice(brush_types_xy))
            if current_brush_type=='airbrush':
                PF.select_size('large')
                PF.squarespiral(current_colors_xy, canvas_width, canvas_height)
            choice+=1
        elif choice < 7:
            PF.horizontalLine(current_colors_xy, canvas_width, canvas_height)
            count = count + 1
        elif choice < 9:
            PF.verticalLine(current_colors_xy, canvas_width, canvas_height)
            count = count + 1
        else:
            PF.diamond(current_colors_xy, canvas_width, canvas_height)
            count = count + 1
    print('Program complete')
except:
    print('Program cancelled')
    





        
    
