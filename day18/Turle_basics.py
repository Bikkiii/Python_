from turtle import Turtle,Screen

t1= Turtle()
t2= Turtle()

screen= Screen()
t1.shape("turtle")
t1.color('red')
t2.shape("triangle")
t2.color('pink')

t1.forward(50)      #How many steps forward
t1.left(90)         #How much degree to rotate
t2.forward(50)
t2.left(90)

t1.forward(100)
t1.left(90)
t2.forward(100)
t2.left(90)

t1.forward(100)
t1.left(90)
t2.forward(100)
t2.left(90)

t1.forward(100)
t1.left(90)
t1.forward(50)
t2.forward(100)
t2.left(90)
t2.forward(50)

screen.exitonclick()