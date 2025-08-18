from turtle import Turtle,Screen

t1=Turtle()
t1.shape('turtle')
t1.color('pink')
size=0
def loop():
    for i in range(10):
        t1.penup()
        t1.forward(10)
        t1.pendown()
        t1.forward(10)
    t1.left(90)    
while size <4: 
    loop()    
    size+=1      