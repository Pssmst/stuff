import math as m
import os
global x
round_input = 100

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

def wait():
    input("Type anything to continue: ")
    clear()

def finalprint(shape,value):
    if x == 0:   math = "Area"
    elif x == 1: math = "Perimeter"
    elif x == 2: math = "Volume"
    elif x == 3: math = "Surface Area"
    print(f"The {math.lower()} of the {shape} is {round(value, round_input)}.")
    wait()

choice_list = [
    ['Square','Rectangle','Triangle','Circle','Regular Pentagon'], # Area
    ['Square','Rectangle','Triangle','Regular Pentagon'], # Perimeter
    ['Cube','Rectangular Prism','Cone','Pyramid','Triangular Prism','Sphere','Cylinder','Dodecahedron'], # Volume
    ['Cube','Rectangular Prism','Cone','Pyramid','Triangular Prism','Sphere','Cylinder','Dodecahedron'], # Surface Area
    ['Circumference','Diameter','Radius','Slope','Pythagorean Theorem'], # Extra
]

topics = ['Area','Perimeter','Volume','Surface Area','Extra']

while True:
    try:
        print("--- Epic Calculator ---")
        print("NOTE: Type 'options' for more!\n")
        print("0: Area\n1: Perimeter\n2: Volume\n3: Surface Area\n4: Extra\n")
        x = input("What do you want to solve for?: ")
        if x.lower() in ['options','option','optio','opti','opt','op','o']:
            clear()
            round_input = int(input("Answer rounding decimal place: "))
            wait()
            continue
        else:
            x = int(x)
        clear()
        
        print(f'--- {topics[x]} ---\n')

        for i in range(len(choice_list[x])):
            print(f"{i}: {choice_list[x][i]}")
            i+=1

        if x != 4:
            y = int(input("\nWhich shape do you want?: "))
        else:
            y = int(input("\nPick your formula: "))

        user_list = [x,y]
        clear()
        print(f"--- {choice_list[x][y]} ---\n")
        
    # AREA ====================================================================================================================

        if user_list == [0,0]: # Square
            length = float(input("Side length: "))
            finalprint('square', length**2)

        elif user_list == [0,1]: # Rectangle
            length = float(input("Side 1: "))
            width = float(input("Side 2: "))
            finalprint('rectangle', length * width)

        elif user_list == [0,2]: # Triangle
            base = float(input("Base: "))
            height = float(input("Height: "))
            finalprint('triangle', base*height/2)

        elif user_list == [0,3]: # Circle
            radius = float(input("Radius: "))
            finalprint('circle', m.pi*radius**2)

        elif user_list == [0,4]: # Regular Pentagon
            length = float(input("Side length: "))
            finalprint('pentagon', (1/4) * length**2 * m.sqrt(5*(5 + 2 * m.sqrt(5))))

    # PERIMETER ===============================================================================================================

        elif user_list == [1,0]: # Square
            length = float(input("Length: "))
            finalprint('square', length*4)

        elif user_list == [1,1]: # Rectangle
            length = float(input("Length: "))
            width = float(input("Width: "))
            finalprint('rectangle', length*2 + width*2)

        elif user_list == [1,2]: # Triangle
            base = float(input("Base: "))
            side2 = float(input("Side 2: "))
            side3 = float(input("Side 3: "))
            finalprint('triangle', base + side2 + side3)

        elif user_list == [1,3]: # Regular Pentagon
            length = float(input("Length: "))
            finalprint('pentagon', length*5)

    # VOLUME ==================================================================================================================

        elif user_list == [2,0]: # Cube
            length = float(input("Length: "))
            finalprint('cube', length**3)

        elif user_list == [2,1]: # Rectangular Prism
            length = float(input("Length: "))
            width = float(input("Width: "))
            height = float(input("Height: "))
            finalprint('rectangular prism', length * width * height)
            
        elif user_list == [2,2]: # Cone
            radius = float(input("Radius: "))
            height = float(input("Height: "))
            finalprint('cone', (1/3) * m.pi * radius**2 * height)
            
        elif user_list == [2,3]: # Pyramid
            base = float(input("Base: "))
            height = float(input("Height: "))
            finalprint('pyramid', (1/3) * base**2 * height)
            
        elif user_list == [2,4]: # Triangular Prism
            base = float(input("Base: "))
            length = float(input("Length: "))
            height = float(input("Height: "))
            finalprint('triangular prism', (1/2) * base*length*height)
            
        elif user_list == [2,5]: # Sphere
            radius = float(input("Radius: "))
            finalprint('sphere', (4/3) * m.pi * radius**3)
            
        elif user_list == [2,6]: # Cylinder
            radius = float(input("Radius: "))
            height = float(input("Height: "))
            finalprint('cylinder', (m.pi*radius**2)*height)
            
        elif user_list == [2,7]: # Dodecahedron
            edge = float(input("Edge length of the pentagonal faces: "))
            finalprint('dodecahedron', (15 + 7 * m.sqrt(5))/4 * edge**3)

    # SURFACE AREA ============================================================================================================

        elif user_list == [3,0]: # Cube
            length = float(input("Length: "))
            finalprint('cube', 6*(length**2))

        elif user_list == [3,1]: # Rectangular Prism
            length = float(input("Length: "))
            width = float(input("Width: "))
            height = float(input("Height: "))
            finalprint('rectangular prism', 2*length*width + 2*length*height + 2*width*height)
            
        elif user_list == [3,2]: # Cone
            radius = float(input("Radius: "))
            height = float(input("Height: "))
            finalprint('cone', m.pi*radius*(radius + height))
            
        elif user_list == [3,3]: # Pyramid
            length = float(input("Length: "))
            height = float(input("Height: "))
            finalprint('pyramid', length**2 + 2*length*height)
            
        elif user_list == [3,4]: # Triangular Prism
            base = float(input("Main triangle base: "))
            side2 = float(input("Main triangle side 2: "))
            side3 = float(input("Main triangle side 3: "))
            height = float(input("Main triangle height: "))
            length = float(input("Prism length: "))
            finalprint('triangular prism', 2*(base*height/2) + (base + side2 + side3)*height)

        elif user_list == [3,5]: # Sphere
            radius = float(input("Radius: "))
            finalprint('sphere', 4*m.pi*radius**2)
            
        elif user_list == [3,6]: # Cylinder
            radius = float(input("Radius: "))
            height = float(input("Height: "))
            finalprint('cylinder', 2*m.pi*radius**2 + 2*m.pi*radius*height)
            
        elif user_list == [3,7]: # Dodecahedron
            edge = float(input("Edge length of the pentagonal faces: "))
            finalprint('dodecahedron', 3*edge**2 * m.sqrt(25 + 10 * m.sqrt(5)))

    # EXTRA ===================================================================================================================

        elif user_list == [4,0]: # Circumference
            radius = float(input("Radius: "))
            print(f"Your circumference is {2*m.pi*radius}.")
            wait()

        elif user_list == [4,1]: # Diameter
            radius = float(input("Radius: "))
            print(f"Your diameter is {radius*2}.")
            wait()

        elif user_list == [4,2]: # Radius
            print("Solve for radius given what?\n0: Circumference\n1: Diameter")
            radiuschoice = float(input("Choose: "))
            if radiuschoice == 0:
                circumference = float(input("Circumference: "))
                print(f"Your radius is {circumference / (2 * m.pi)}.")
                wait()
            elif radiuschoice == 1:
                diameter = float(input("Diameter: "))
                print(f"Your radius is {diameter/2}.")
                wait()

        elif user_list == [4,3]: # Slope
            x1 = float(input("x1: "))
            y1 = float(input("y1: "))
            x2 = float(input("x2: "))
            y2 = float(input("y2: "))
            print(f"Your slope is {(y2 - y1) / (x2 - x1)}.")
            wait()

        elif user_list == [4,4]: # Pythagorean theorem
            a = float(input("Leg 1 (a): "))
            b = float(input("Leg 2 (b): "))
            print(f"Your hypotenuse (c) is {m.sqrt(a**2 + b**2)}.")
            wait()
    except:
        print("Error detected!")
        wait()
        continue