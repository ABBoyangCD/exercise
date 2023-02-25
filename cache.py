# Boyang Ji 201649047

def fifo():  # This is fifo function
    for i in request:
        if len(cashe) < 8:
            if i not in cashe:
                cashe.append(i)
                print("miss")
            else:
                print("hit")
        else:
            if i not in cashe:
                cashe.pop(0)
                cashe.append(i)
                print("miss")
            else:
                print("hit")
    print(cashe)
    cashe.clear()
    request.clear()
    startInput()


def lfu():
    # This is lfu function
    # Using dictionaries to count requested pages
    dict1 = {}
    dict2 = {}
    for i in request:
        if len(dict1) < 8:
            if i in dict1:
                print("hit")
                dict1[i] = dict1[i]+1
            else:
                print("miss")
                dict1[i] = 1
        else:  # len(dict1)>=8
            if i not in dict1:
                print("miss")
                min_value = min(dict1.values())
                # Finding the minimum number of requests
                min_keys = [k for k in dict1 if dict1[k] == min_value]
                # Find the smallest number
                dict2[min(min_keys)] = dict1[min(min_keys)]
                dict1.pop(min(min_keys))
                if i not in dict2:
                    dict1[i] = 1
                else:  # in dict2
                    dict1[i] = dict2[i]+1
                    dict2.pop(i)
            else:  # i in dict1
                print("hit")
                dict1[i] = dict1[i]+1
    print(list(dict1.keys()))
    dict1.clear()
    dict2.clear()
    request.clear()
    startInput()


def chooseAlgorithms():
    # This function is to select the algorithm
    # Select 1 for the fifo algorithm,
    # 2 for the lfu algorithm and
    # 3 for the termination procedure
    # Parameters: input – int
    choice = input("please choose a Algorithms:")
    if choice == "1":
        print("you choose fifo")
        fifo()
    elif choice == "2":
        print("you choose lfu")
        lfu()
    elif choice == "Q":
        print("program over")


request = []    # Store the request page
cashe = []    # Store cache


def startInput():
    while 1:
        page = int(input("please enter a intger:"))
        if page == 0:
            break
        else:
            request.append(page)
    print(request)
    chooseAlgorithms()


startInput()
