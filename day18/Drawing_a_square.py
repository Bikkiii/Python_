# import turtle
# t1=turtle.Turtle()

# from turtle import *        #imports everything
    
# import turtle as t          #aliasing  
# t1=t.Turtle()

import heroes
print(heroes.gen())
from turtle import Turtle,Screen

t1=Turtle()
t1.shape('turtle')
t1.color('pink')

for i in range(4):
    t1.forward(100)
    t1.left(90)
    