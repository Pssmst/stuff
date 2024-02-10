import time

def fibonacciCalc():
    index = 0
    f_list = [0, 1]
    yes = ['yes','ye','y']
    no = ['no', 'n']

    condition = input("Do you want to see the advanced settings? (y/n): ")

    # Advanced settings
    if condition.lower() in yes:
        advanced = True
        start = int(input("Starting point (start index - defaults to 0): "))
        end = int(input("Sequence length (end index - defaults to 100): "))

        index_condition = input("Do you want to show the position of each number? (y/n - defaults to no): ")
        if index_condition.lower() in yes:
            index_show = True
        else:
            index_show = False

        commas_condition = input("Do you want to include commas in the numbers? (y/n - defaults to yes): ")
        if commas_condition.lower() in no:
            commas_show = False
        else:
            commas_show = True
        
        time_condition = input("Do you want to print each number individually at a time? (y/n - defaults to yes): ")
        if time_condition.lower() in no:
            time_show = False
        else:
            time_show = True

    else:
        start = 1
        end = 100
        index_show = False
        commas_show = True
        time_show = True

    print("")

    for i in range(end):
        if index >= start-1:
            if index_show == True:
                if commas_show == True:
                    print("(" + str(index) + ")", "{:,}".format(f_list[index]))
                else:
                    print(f"({index}) {f_list[index]}")
            else:
                if commas_show == True:
                    print("{:,}".format(f_list[index]))
                else:
                    print(f_list[index])
        if index < end:
            index += 1
            f_list.append(f_list[index-1] + f_list[index])

        if time_show == True:
            time.sleep(0.005)

    while True:
        input("")