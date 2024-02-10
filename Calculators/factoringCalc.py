import os, math
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()
##########################################################################

factorList = []

def factor(n):
    print(f'FACTORING: {n} -----------------')

    for x in range(1, round(math.sqrt(n))+1):
        #print('x =', x)
        for y in range(1, n+1):
            if (x*y == n):
                print(f'{x} x {y}', end='')
                factorList.append([x,y])

                if (x == y): print(' < Square')
                else: print()
    print()


def isSecretInt(num): # Determine if a float is actually an int in disguise (i.e. '3.0')
    num = str(num)
    dot_found, isInt = False, False
    
    for char in num:
        if (char == '.'):
            dot_found = True
        
        if (dot_found):
            if (char in ['1','2','3','4','5','6','7','8','9']):
                isInt = False
            else:
                isInt = True
    
    if (isInt):
        #print("Num is int")
        return isInt
    else:
        #print("Num is float")
        return isInt


def simplifyFraction(factor, t1):
    print(f'\n{factor} / {t1} = {factor/t1}')

    if (isSecretInt(factor/t1)): # If the fraction (factor1/t1) equals a whole number
        x_multiplier = ''
        new_factor = int(factor/t1)
        print("Fraction is integer")
    else:
        gcd = math.gcd(factor, t1)
        x_multiplier = int(t1/gcd)
        new_factor = int(factor/gcd)
        print(f'Simplifying fraction: {factor}/{t1} --> {new_factor}/{x_multiplier}')

    return x_multiplier, new_factor # (x_multiplier, new_second_value)


def enterExpression():
    print("Expression types ---\n2 terms: (a)x^2 (+/-) (b)            | Example: 2x^2 + 14\n3 terms: (a)x^2 (+/-) (b)x (+/-) (c) | Example: 8x^2 - 7x + 10\n")
    
    expression = input("Expression: ")
    o1_found, o2_found, exponent_ready = False, False, False
    t1, exp, o1, t2, o2, t3 = '1', '', '', '0', '', '0'
    
    # Cool disclaimer: If you type the name of a boolean alone in an if statement, it's just a shorter way of saying `if boolean == True`
    # When you see something like `if exponent_ready and o1_found == False`, it's actually asking `if exponent_ready == True and o1_found == False`
    
    for char in expression:
        # If char is number
        if (char in ['0','1','2','3','4','5','6','7','8','9']):
            if (exponent_ready and o1_found == False):
                exp += char
            else:
                if (o1_found == False and o2_found == False): # assign term 1
                    if (t1 == '1'):
                        t1 = '0'
                    t1 += char
                elif (o1_found and o2_found == False): # assign term 2 after first operator
                    t2 += char
                elif (o1_found and o2_found == True): # assign term 3 after second operator
                    t3 += char

        # Determine power of x (so it doesn't think it's part of term 1)
        elif (o1_found == False and char == 'x'):
            exponent_ready = True
        
        # Default second term to x
        elif (o1_found and char == 'x' and t2 == '0'):
            t2 = '1'
        
        # If char is operator
        elif (char in ['+','-']):
            if o1_found:
                o2 += char
                o2_found = True
            else:
                o1 += char
                o1_found = True
    
        #print(f'{t1} {exp} {o1} {t2} {o2} {t3}   expReady:{exponent_ready}')
    
    if (exp == ''): exp = '2'
    return int(t1), int(exp), o1, int(t2), o2, int(t3)


def factorExpression():
    while True:
        completed = False
        
        print()
        t1, exp, o1, t2, o2, t3 = enterExpression()
        
        # 2-term expressions
        if (t3 == 0):
            if (t1 == 1):
                print(f'Percieved Expression: x^{exp} {o1} {t2}')
            else:
                print(f'Percieved Expression: {t1}x^{exp} {o1} {t2}')  
        
        # 3-term expressions
        else:
            if (t1 == 1):
                print(f'Percieved Expression: x^{exp} {o1} {t2}x {o2} {t3}')
            else:
                print(f'Percieved Expression: {t1}x^{exp} {o1} {t2}x {o2} {t3}')
        
        print("Not the same expression? You either typed something wrong or I did\n")

        # Find factors for term 3 (+ slide, multiply)
        factor(t3*t1)
        
        # Assign negative or positive value to terms & multipliers for factors to use later
        if (o1 == '+' and o2 == '+'):
            # (terms are automatically positive)
            multiplier1, multiplier2 = 1, 1
            print('Multipliers: (+)(+)')
            
        elif (o1 == '-' and o2 == '+'):
            t2 *= -1
            multiplier1, multiplier2 = -1, -1
            print('Multipliers: (-)(-)')
            
        elif (o1 == '+' and o2 == '-'):
            t3 *= -1
            multiplier1, multiplier2 = -1, -1
            print('Multipliers: (-)(-)')
            
        elif (o1 == '-' and o2 == '-'):
            t2 *= -1
            t3 *= -1-10
            multiplier1, multiplier2 = 1, -1
            print('Multipliers: (+)(-)')

        print(f'\nt2 = {t2} | t3 = {t3}')
        
        # FIND SOLUTION
        for i in range(len(factorList)):
            factor1 = factorList[i][0] * multiplier1
            factor2 = factorList[i][1] * multiplier2
            
            print(f'Checking: {factor1} + {factor2} = {factor1 + factor2}')

            if (factor1 + factor2 == t2):
                # PORTER METHOD
                if (t1 != 1):
                    x_multiplier1, new_factor1 = simplifyFraction(factor1, t1)
                    x_multiplier2, new_factor2 = simplifyFraction(factor2, t1)
                    print(f'\n>>> ({x_multiplier1}x + {new_factor1})({x_multiplier2}x + {new_factor2})')
                
                # REGULAR METHOD
                else:
                    print(f'\n>>> (x + {factor1})(x + {factor2})')
                completed = True
                
        if (completed == False):
            print('>>> Prime')
        
        input()
        clear()
        

### INPUT ###########################################################

factorExpression()