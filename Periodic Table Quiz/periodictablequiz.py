import random as rand
import time
import os

# Declare variables
can_continue = False
correct_count = 0
wrong_count = 0
yes = ["y", "ye", "yes", "yup"]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def ask_question(option1, option2):
        # Ask for ELEMENT
        print(f"What is the element for {option1}?")
        answer = input("Enter your answer: ")

        # Check for end
        if answer.lower() in ["end", "quit"]:
            breaker = True
        
        # Evaluate answer
        if answer == option2:
            correct = True
            correct_count += 1
            print("\n> Correct!")
            if preference in yes:
                del element_list[index]
                del symbol_list[index]
        else:
            correct = False
            wrong_count += 1
            print(f"\n> Wrong. It was {option2}.")

while True:
    # Ask for testing preference
    print("\n[] Do you want the elements deleted from the list when you get them correct?")
    print('Type "yes" or "no" (Defaults to yes)')
    preference = input("Your answer: ")

    # Ask for testing preference
    print("\n[] Do you want EVERY element, or just the basic ones?")
    print('Type "yes" or "no" (Defaults to no)')
    student_input = input("Your answer: ")
    
    if student_input.lower() in yes:    student = False
    else:                               student = True
    
    if student == False:
        element_list = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon", "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium", "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium", "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Oganesson"]

        symbol_list = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]

    elif student == True:
        element_list = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon", "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc", "Bromine", "Krypton", "Rubidium", "Strontium", "Silver", "Tin", "Iodine", "Xenon", "Cesium", "Barium", "Tungsten", "Platinum", "Gold", "Mercury", "Lead", "Polonium", "Radon", "Francium", "Radium", "Uranium", "Plutonium"]
        
        symbol_list = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Br", "Kr", "Rb", "Sr", "Ag", "Sn", "I", "Xe", "Cs", "Ba", "W", "Pt", "Au", "Hg", "Pb", "Po", "Rn", "Fr", "Ra", "U", "Pu"]
    break

# Keep going until there are no more elements in the list
while element_list != []:
    clear()
    print('You can type "end" or "quit" at any time to finish the quiz!\n')

    # Randomly choose question
    question = rand.randint(1,2)
    element = rand.choice(element_list)
    
    index = element_list.index(element)
    symbol = symbol_list[index]

    if question == True:
        ask_question(element,symbol)
    else:
        ask_question(symbol,element)

    if breaker == True: break
        
    time.sleep(1.5)

# End quiz when you run out of elements
print("-----------------------------------")
total_count = correct_count + wrong_count

if total_count != 0:
    print(f"Good job! You got {correct_count} correct and {wrong_count} wrong. That's {correct_count}/{total_count}, or {round(correct_count / total_count, 2) * 100}%!")
else:
    print("Dude, in order to see how you did you actually have to take the quiz")