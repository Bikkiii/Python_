# my_tuple=(1,3,8)
# print(my_tuple[0])
# my_tuple[2]=10          #Throws error coz Tuples are unchangeable

from turtle import Turtle,Screen
import random
t1=Turtle()
screen=Screen()
t1.shape('turtle')
screen.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color
    
dir=[0,90,180,270]
t1.pensize(5)
t1.speed('fastest')
for i in range(500):
    direction=random.choice(dir)
    t1.color(random_color())
    t1.forward(25)
    t1.setheading(direction)


screen=Screen()
screen.exitonclick()

