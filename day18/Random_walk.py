from turtle import Turtle,Screen
import random
t1=Turtle()
t1.shape('turtle')

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
dir=[0,90,180,270]
t1.pensize(5)
t1.speed('fastest')
for i in range(500):
    direction=random.choice(dir)
    t1.color(random.choice(colors))
    t1.forward(25)
    t1.setheading(direction)


screen=Screen()
screen.exitonclick()
