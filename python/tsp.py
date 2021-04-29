import numpy as np
import sys
import time

def Eu2D(x1, y1, x2, y2):           #Function to calculate its euclidean distance
    return np.sqrt( (x1-x2)**2 + (y1-y2)**2 )

tsp = open("test.tsp", "r") #Here we type the filename of the .tsp we want to use.

for x in range(3):  #Jump lines to Dimension
    tsp.readline()

dimension = tsp.readline().split()[1]
n = int(dimension)

for x in range(2):
    tsp.readline()

node = []
dM = []
status = [True for i in range(n)]
minium = sys.float_info.max
k = 0
auxI = 0

for i in range(0, n):   #Save coordinates in a matrix
    x,y = tsp.readline().strip().split()[1:]
    node.append([float(x), float(y)])

for i in range (0, n):  #Calculate its euclidean distance
    x1 = node[i][0]
    y1 = node[i][1]
    
    temp = []
    for j in range(0, n):
        x2 = node[j][0]
        y2 = node[j][1]

        eD = Eu2D(x1, y1, x2, y2)
        temp.append(eD)

    dM.append(temp)

i = -1

while i < 1 or i > n:
    number = input("\nFrom 1 to "+dimension+"\nStart in: ")     #Starting point
    i = int(number)
    f = i

startTime = time.time() #Calculate execution time

i -= 1

nearn = []
routeCoords = []
total = 0

while k < n:
    status[i] = False
    nearn.append(i+1)
    for j in range(0, n):
        if dM[i][j] < minium and status[j] == True and dM[i][j] != 0:
            minium = dM[i][j]
            auxI = j
    
    i=auxI
    k += 1
    if k < n:
        total += minium
    if k == n:
        total += dM[k-1][f-1]

    minium = sys.float_info.max

execTime = time.time() - startTime

nearn.append(f)

print("\nRoute: %s" %nearn)
print("\nTotal distance: %s units" %total )
print("Execution time: %s s." %execTime)

tsp.close()