def primeCalc(length):
    numberList = []
    start = 2
    multiple = 2

    for i in range(1, length):
        numberList.append(i)
    del numberList[0]

    while True:
        try:
            del numberList[numberList.index(start*multiple)]
            multiple += 1
        except:
            multiple += 1
        if ((start*multiple) > length):
            start += 1
            multiple = 2
        if (start > (round(length/2))):
            break

    print(numberList[0])

primeCalc(21)