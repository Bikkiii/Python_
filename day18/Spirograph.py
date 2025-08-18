# my_tuple=(1,3,8)
# print(my_tuple[0])
# my_tuple[2]=10          #Throws error coz Tuples are unchangeable

from turtle import Turtle,Screen
import random
t1=Turtle()
screen=Screen()
t1.speed("fastest")
screen.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color

def spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        t1.color(random_color())
        t1.circle(100)
        curr_heading=t1.heading()
        t1.setheading(curr_heading + size_of_gap)
        t1.circle(100)
spirograph(5)    
screen.exitonclick()

