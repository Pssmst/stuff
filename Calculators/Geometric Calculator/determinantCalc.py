import math, os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

# Get values #########################################################

def solveDeterminant():
    print('(m)x + (a)y = (b)\n')

    m1 = float(input('Enter m1: '))
    a1 = float(input('Enter a1: '))
    b1 = float(input('Enter b1: '))

    clear()
    print(f'{m1}x + {a1}y = {b1}\n(m)x + (a)y = (b)\n')

    m2 = float(input('Enter m2: '))
    a2 = float(input('Enter a2: '))
    b2 = float(input('Enter b2: '))

    clear()
    print(f'Solving:\n{m1}x + {a1}y = {b1}\n{m2}x + {a2}y = {b2}\n')

    # Solve ###########################################################

    # [m1 a1]
    # [m2 a2]
    D = (m1*a2)-(m2*a1)

    # [m1 b1]
    # [m2 b2]
    Dx = (m1*b2)-(m2*b1)

    # [b1 a1]
    # [b2 a2]
    Dy = (b1*a2)-(b2*a1)

    x = Dx/D
    y = Dy/D

    print(f'Solution is ({round(x, 3)},{round(y, 3)})')

solveDeterminant()