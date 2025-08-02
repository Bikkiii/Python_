import math
height=int(input("Enter the height of the wall: "))
width=float(input("Enter the width of the wall: "))
coverage=5

def paint_calc(h,w,cover):
    total_can=math.ceil((height*width)/5)     #rounded to the up
    print(f"The total can required to paint the wall is {total_can}")
paint_calc(h=height,w=width,cover=coverage)
