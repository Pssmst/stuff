'''
import time, os, random as rand

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

mylist = []
sublist = []
coordinate_list = []

x = 30 #int(input("Grid width (x): "))
y = 30 #int(input("Grid length (y): "))
x+=1

while True:
    xpos = int(input("x position: "))
    ypos = int(input("y position: "))
    coordinate_list.append(f"({xpos},{ypos})")
    ypos = y-ypos
    mylist = []

    for e in range(y):
        # Format y numbers and left line
        if y-e < 10:
            sublist = [f"0{y-e}|"]
        else:
            sublist = [f"{y-e}|"]

        # Define grid & coordinates
        for i in range(x):
            if i+1 == xpos and e == ypos:
                sublist.append("0")
            else:
                sublist.append("⋅")
        mylist.append(sublist)

    # Print coordinates in text
    clear()
    for i in range(len(coordinate_list)):
        if i == 0:  print(coordinate_list[i], end="")
        else:       print(f" - {coordinate_list[i]}", end="")
    print()
    
    # Print grid
    for i in range(y):
        for e in range(x):
            if e != 0:  print(mylist[i][e], end="  ")
            else:       print(mylist[i][e], end=" ")
        print()

    # Format bottom line and x numbers
    print("Y  ", end="")
    for e in range(x-1):
        print("¯¯¯", end="")

    print("\n  X ", end="")
    for e in range(x-1):
        if e+1 < 10:
            print(f"0{e+1}", end=" ")
        else:
            print(f"{e+1}", end=" ")
    print("\n")
'''