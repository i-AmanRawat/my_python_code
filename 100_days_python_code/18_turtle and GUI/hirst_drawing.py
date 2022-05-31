'''
import colorgram
colors = colorgram.extract('hirst_image.jpg' , 36)    #-->firstly specify file name in which image exist then number of colors to be taken out here 6
color_list = []     #declaring empty list to avoid 'not defined' error
for color in colors:    # calling elements of colors one by one
    r = color.rgb.r     # fetching rgb then specifally red color code from it
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b )  # making rgb code tuple and appending it into the list
    color_list.append(new_color)
print(color_list)   #finally printing the list of color that has been extracted from that hist image
 #now commenting this program bcz we got the list of color codes

hsl = first_color.hsl   -->hsl is meant to be understandable by the humans as it is not with the rgb which for machines 
       H --> stands for Hue
       S --> stands for saturation
       L --> stands for lightness
    
print(hsl)

Example how actually we get color from colors then how we fetch our desires
    <colorgram.py Color: Rgb(r=226, g=226, b=225), 73.74414221238479%>
    r = color.rgb.r 
'''

import turtle as t
import random
tom = t.Turtle()
tom.pen(pensize=8, speed=40)
t.colormode(255)
tom.hideturtle()
color_list = [(226, 226, 225), (236, 236, 239), (182, 65, 34), (213, 149, 97), (14, 24, 42), (230, 237, 233),
              (239, 208, 94), (241, 234, 238), (237, 62, 33), (157, 26, 19), (72, 29, 32), (84, 94, 115),
              (166, 141, 66), (67, 41, 35), (120, 32, 37), (183, 85, 94), (135, 152, 164), (49, 52, 127),
              (229, 175, 161), (165, 64, 70), (167, 141, 150), (98, 113, 112), (160, 168, 165), (189, 190, 196),
              (217, 174, 180), (15, 25, 24), (79, 70, 43), (183, 196, 189), (119, 121, 147), (248, 196, 4),
              (185, 195, 196), (253, 12, 5), (251, 10, 11), (58, 65, 69), (124, 130, 128), (121, 131, 133)]

for i in range (0,451,50):
    tom.penup()
    tom.setposition(-250, (-250 + i))
    tom.pendown()
    for j in range (10):
        tom.dot(20, random.choice(color_list))
        tom.penup()
        tom.forward(50)
        tom.pendown()

screen = t.Screen()
screen.exitonclick()
