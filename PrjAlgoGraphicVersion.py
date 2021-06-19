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
    # print("paintArray is: ",paintArray)
    return paintArray




  #user inputs:
# m = 7
# n = 30
print("-------------------   Scheduling Jobs on Identical Machines Program   -------------------  ")
m = int(input("Please Enter the number of machines "))
n = int(input("Please Enter the number of Jobs "))
a = []
for i in range(n):
    a.append(random.randrange(1,51))
print("list of jobs: " , a)
print()



GreedyMethod(a,m)
DynamicPaint = DynamicProgramming(a,m)



print("---------------------------------------------------------")
# aTest = [7 , 7 , 2 , 4 , 25]

# GreedyMethod(aTest,2)
# DynamicPaintTest = DynamicProgramming(aTest , 2)
# print(machines)
# print(max(machines))
print("--------------------")
print(DynamicPaint)
print(len(DynamicPaint))

pygame.init()
screen = pygame.display.set_mode((1500,900))
pygame.display.set_caption('Scheduling Jobs on Identical Machines Program')
font1 = pygame.font.Font('freesansbold.ttf', 48)
text = font1.render('1', True, GREEN, BLUE)
textRect = text.get_rect()
# textRect.center = (400 , 400 )


while True:
    screen.fill(WHITE)
    # ballTest.show()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # pygame.draw.circle(screen, RED, (100, 200), 20)
    screen.blit(text, textRect)
    # pygame.draw.rect(screen,RED,(10,10,100,100))
    pygame.draw.line(screen,BLACK,(0,900),(1500,900),40)
    for i in range(len(DynamicPaint)):
        pygame.draw.line(screen, BLACK, (int((i+1)*1500.0/(len(DynamicPaint)+1)), 200), (int((i+1)*1500.0/(len(DynamicPaint)+1)), 900), 10)
        height = 0
        for j in range(len(DynamicPaint[i])):
            height += DynamicPaint[i][j]
            font1 = pygame.font.Font('freesansbold.ttf', DynamicPaint[i][j] + 25)
            text = font1.render(str(DynamicPaint[i][j]), True, GREEN, BLUE)
            textRect.center= (int((i+1)*1500.0/(len(DynamicPaint)+1)) - (DynamicPaint[i][j])//2 , 875 - 1.5*height)
            height += 30
            # pygame.time.wait(1000)
            screen.blit(text, textRect)

    # pygame.draw.line(screen, BLACK, (300, 200), (300, 900), 10)
    pygame.display.update()


