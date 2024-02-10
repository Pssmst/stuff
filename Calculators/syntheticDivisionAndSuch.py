import cmath as m

numbers = ['0','1','2','3','4','5','6','7','8','9']

def filterTerms(equation): # Make this filter out entire equations later!
    num_list = []
    num = ''
    negative = False

    for char in equation:

        if (char == "-"): # If negative sign detected
            negative = True
        
        elif (char in numbers): # If number detected
            num += char
        
        else: # If anything else
            if (negative): num_list.append("-" + num)
            else:          num_list.append(num)
            num = ''
            negative = False
            
    # Append last number
    if (negative): num_list.append("-" + num)
    else:          num_list.append(num)

    for element in num_list[:]: # Delete empty elements by using a COPY of the list
        if (element == ''):
            num_list.remove(element)

    for i in range(len(num_list)): # Turn all strings into integers
        num_list[i] = int(num_list[i])

    print(f'Num List: {num_list}')
    return num_list


def syntheticDivision():
    equation = input("Equation: ")
    term_list = filterTerms(equation)
    box = int(input("Enter box number: "))
    
    new_term_list = []
    carry = 0
    
    for term in term_list: # This is the synthetic division
        new_term = term + carry # First step just drops the term down, so carry = 0
        new_term_list.append(new_term)
        carry = new_term*box
        print(f'NewTerm:{new_term} | carry:{carry}')
    
    if (new_term_list[3] == '0'):
        print('Looks good to me')
    
    print(new_term_list)
    
    # Quadratic formula
    a = new_term_list[0]
    b = new_term_list[1]
    c = new_term_list[2]
    
    radicand = b**2 - 4*a*c
    print(f'radicand: {radicand}')
    
    positive_sol_num = (-b + m.sqrt(radicand)) / (2*a)
    negative_sol_num = (-b - m.sqrt(radicand)) / (2*a)
    
    positive_sol_str = f'{-b + m.sqrt(radicand)}/{2*a}'
    negative_sol_str = f'{-b - m.sqrt(radicand)}/{2*a}'
    
    print(f'x = {box}, {positive_sol_num}, {negative_sol_num}')
    #print(f'x = {box}, {positive_sol_str}, {negative_sol_str}')

syntheticDivision()