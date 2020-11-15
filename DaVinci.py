import PortraitPaintFunctions as PPF
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
canvas_height = (250, 985) #we used a margin on either side of the height to avoid potential problems in the gui


time.sleep(4)
current_colors_xy = PPF.create_portrait_theme()
current_brush_type = PPF.select_brush('oil brush')


PPF.landscapeline(current_colors_xy, canvas_width, canvas_height, 'medium small', 'green')
iteration = 0
while iteration <200:
    PPF.horizontalLine(current_colors_xy, canvas_width, canvas_height, 600)
    print(iteration)
    iteration+=1