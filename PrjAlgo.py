import random
import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


#Greedy Method
def GreedyMethod(a,m):
    a = sorted(a)
    machines = []
    for i in range(m):
        machines.append(0)

    for i in range(len(a)):
        machines[i % m] += a[i]
    print()
    print(" Greedy Method: ")
    print("jobs: (sorted) " , a)
    print("Time spent for all machines: " , machines)
    print("result: " , max(machines))



#Dynamic Programming
def DynamicProgramming(a,m):
    a = sorted(a)
    print()
    print(" Dynamic Programming: ")
    print("jobs: (sorted) ", a)
    paintArray = []
    for i in range(m):
        paintArray.append([])
    machines = []
    for i in range(m):
        machines.append(a[~i])
    debugArray =[]
    time = 0
    if m==1:
        time = sum(a)
        debugArray.append(time)
        paintArray[0].append(time)
    else:
        for i in range(m):
            a.pop(~0)
        for i in range(m):
            debugArray.append(machines[i])
            paintArray[i].append(machines[i])

        while len(a) > 0:
            time += 1
            for i in range(m):
                machines[i] -= 1
            for i in range(m):
                if machines[i] == 0:
                    if len(a) == 0:
                        break
                    elif len(a) == 1:
                        machines[i] = a[0]
                        debugArray[i] += a[0]
                        a = []
                    else:
                        machines[i] = a[~0]
                        debugArray[i] += a[~0]
                        a.pop(~0)
                    paintArray[i].append(machines[i])

        time += max(machines)
            # print("macihens: " , machines)

    print("Time spent for all machines: " , debugArray)
    print("result:" , time)
    print("How the jobs distributed: ")
    for i in range(len(paintArray)):
        print("machine number ",i+1, ": ",paintArray[i])
    # print("paintArray is: ",paintArray)
    return paintArray




  #user inputs:
# m = 7
# n = 30
print("-------------------   Scheduling Jobs on Identical Machines Program   -------------------  ")
m = int(input("Please Enter the number of machines: "))
n = int(input("Please Enter the number of Jobs: "))
a = []
for i in range(n):
    a.append(random.randrange(1,51))
print("list of jobs: " , a)
print()



GreedyMethod(a,m)
DynamicPaint = DynamicProgramming(a,m)



print("----------------------------------------------------------")


# print(max(machines))

# print(DynamicPaintTest)
# print(len(DynamicPaintTest))
# print(DynamicPaint)
# print(len(DynamicPaint))


