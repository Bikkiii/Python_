from turtle import Turtle,Screen

obj=Turtle()     #Constructiong an object
print(obj)      #objejct being printed

my_screen= Screen()             #Creating an object named my_screen
print(my_screen.canvheight)     #my_screen is an ibject and canvheight is an attributes
print(my_screen.canvwidth)
my_screen.bgcolor("pink")
obj.shape("turtle")             #shape of turtle
obj.color("red")                #Color of turtle

obj.forward(100)                #moves turtle forward by 100 steps
obj.left(90)
obj.heading()
obj.forward(100)

obj.left(90)
obj.heading()
obj.forward(100)

obj.left(90)
obj.heading()
obj.forward(100)

obj.left(90)
obj.heading()

my_screen.exitonclick()
