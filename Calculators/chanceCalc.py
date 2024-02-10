import time, os, random as rand

chance = 1
lst = []
targetList = []
length = 10
limit = 2

for i in range(length):
    chance = chance *(1/limit)
print(f"The chance is: {chance*100}%")
time.sleep(2)

for i in range(length):
    targetList.append(1)

while True:
    for i in range(length):
        var = rand.randint(1,limit)
        lst.append(var)
    
    for i in range(len(lst)):
        print(lst[i], end=' ')
    print()
    
    if lst == targetList:
        break
    else:
        lst = []

print("yay!")