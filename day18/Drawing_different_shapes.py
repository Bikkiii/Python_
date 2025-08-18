from turtle import Turtle,Screen
# import random
t1=Turtle()
t1.shape('turtle')

colors=['yellow','red','black','orange','pink','green','brown','purple']
def shape(n,c):
    t1.color(c)
    deg=360/n
    for i in range(n):
        t1.forward(100)
        t1.right(deg)
        
        
for i in range(3,11):
    # t1.color(random.choice(colors))
    shape(i,colors[i-3])    
       