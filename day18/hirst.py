import colorgram
from turtle import Turtle,Screen
import random
#Extracting colors

# rgb_colors=[]
# colors = colorgram.extract(r"day18\image.jpg", 30)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
        
        
color_list=[(246, 244, 243), (235, 240, 246), (247, 240, 243), (240, 246, 243), (133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219), (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209)]
t1=Turtle()
screen=Screen()
t1.shape('turtle')
screen.colormode(255)
t1.setheading(225)
t1.forward(300)
t1.setheading(0)

number_of_dots=100
for i in range(1,number_of_dots+1):
    t1.dot(20,random.choice(color_list)) 
    t1.penup()
    t1.forward(50)
    
    if i % 10 ==0:
        t1.setheading(90)
        t1.forward(50)
        t1.setheading(180)
        t1.forward(500)
        t1.setheading(0)



screen.exitonclick()

       