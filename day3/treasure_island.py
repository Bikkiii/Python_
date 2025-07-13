print("Welcome to Treasure Island\nYour mission is to find the treasure")
move=input("Which direction do you want to go? L or R: ")
if move == "L":
   swim=input("You are in the sea, do you want to swim or wait? S or W: ")
   if swim=="W":
       door=input("You are last step away to find the treasure\nThere are three doors(RED,BLUE,YELLOW)\nWhich door do you want to open? R,B or Y: ")
       if door=="Y":
           print("Congrats!!, You won the game")
       else:
           print("Game Over!!!")
   else:
        print("Game Over!!!")          
else:
    print("Game Over!!!")    