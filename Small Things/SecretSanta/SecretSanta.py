import random as rand, os

def assign(path, a, b):
    with open(path, "w", encoding='utf-8') as f:
        f.write(f"To {a}:\nGet a gift for {b}")
    print(f"updated {a}'s file")

# declare people
aList = ['person1', 'person2', 'person3', 'person4']
bList = ['person1', 'person2', 'person3', 'person4']

while (aList != []):
    a = rand.choice(aList)
    b = rand.choice(bList)

    # check for repeats like "Person1 has to get a gift for Person1"
    while (a == b):
        a = rand.choice(aList)

    # put names in text documents for secrecy
    txt = fr"{a.lower()}.txt"
    path = os.path.abspath(__file__)
    path = path[:-14]
    path = fr"{path}{txt}"

    assign(path, a, b)
    
    # remove decisions from list for futher use
    aList.remove(a)
    bList.remove(b)