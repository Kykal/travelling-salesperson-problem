import numpy as np
import sys
import time
import math

#Declaring variables
nodes = []
route = []
routeCoords = []
totalDistance = 0
actualTime = 0
timeLimit = 60.0 #seconds
position = 1
upgrades = 0
loop = True
evolution = 0

#Function to calculate Euclidean Distance
def Eu2D(x1, y1, x2, y2):
    return np.sqrt( (x1-x2)**2 + (y1-y2)**2 )

#Open the file we want to use
tsp = open("TSP/test.tsp", "r")

#Jump lines to 'Dimension', save its dimension and jump to coordenates
for x in range(3):
    tsp.readline()
dimension = int( tsp.readline().split()[1] )
for x in range(2):
    tsp.readline()

#Save coordinates in a matrix called 'nodes' and assings the status of True to all nodes.
for i in range(0, dimension):
    x,y = tsp.readline().strip().split()[1:]
    nodes.append([float(x), float(y)])
status = [True for i in range(dimension)]

#Asks user where to start, save input as integer subtracting one. Saves initial coordinates as 'initCoords' and its coordinates.
initNumber = int( input("From 1 to %s\n\tWhere do you want to start?: " %dimension) ) - 1
initCoords = nodes[initNumber]
status[initNumber] = False
x1 = initCoords[0]
y1 = initCoords[1]

#Append variables to 'route' and 'routeCoords'.
route.append(initNumber+1)
routeCoords.append(initCoords)

#Algorithm timer execute
startTime = time.time()

#Calculates and compares euclidean distance between initial coordinates and neighboors.
for j in range(0, dimension-1):
    minDistance = sys.float_info.max
    for i in range( 0, dimension ):
        x2 = nodes[i][0]
        y2 = nodes[i][1]
        euclideanDistance = Eu2D(x1, y1, x2, y2)
        if status[i] == True and euclideanDistance < minDistance:
                minDistance = euclideanDistance
                minCoords = nodes[i]
                xStatus = i
        actualTime = time.time() - startTime
        if actualTime >= timeLimit :
            loop = False
            break

    totalDistance += minDistance
    x1 = minCoords[0]
    y1 = minCoords[1]
    status[xStatus] = False
    route.append(xStatus+1)
    routeCoords.append(minCoords)
    actualTime = time.time() - startTime
    if actualTime >= timeLimit :
        loop = False
        break

#Local Search
temp = route.copy()

while loop == True and actualTime < timeLimit:
    for i in range(0, dimension-3) :
        if position+1 < dimension-1 :
            aux = routeCoords[position]
            routeCoords[position] = routeCoords[position+1]
            routeCoords[position+1] = aux
            aux = temp[position]
            temp[position] = temp[position+1]
            temp[position+1] = aux
            if temp == route :
                loop = False
                break
            tempTotalDistance = 0
            for k in range(0, dimension-1):
                x1 = routeCoords[k][0]
                y1 = routeCoords[k][1]
                x2 = routeCoords[k+1][0]
                y2 = routeCoords[k+1][1]
                euclideanDistance = Eu2D(x1, y1, x2, y2)
                tempTotalDistance += euclideanDistance
                actualTime = time.time() - startTime
                if actualTime >= timeLimit :
                    loop = False
                    break
            if tempTotalDistance < totalDistance :
                newRoute = temp.copy()
                upgrades += 1
                totalDistance = tempTotalDistance
            position += 1
            evolution += 1
        else :
            position = 1
        actualTime = time.time() - startTime
        if actualTime >= timeLimit :
            loop = False
            break

if actualTime >= timeLimit :
    print( "Limit time exceeded (%s seconds)." %timeLimit )
    loop = False
if upgrades == 0 :
    route.append(initNumber+1)
    print("\nThere are no better routes to take.\n")
    print( "Best route: %s" %route)
else :
    newRoute.append(initNumber+1)
    print( "\nBest route: %s" %newRoute)

print("[x1: %s][y1: %s]" %(x1, y1))
print("[x2: %s][y2: %s]" %(x2, y2))

#Algorithm timer ends
execTime = time.time() - startTime
print( "Best distance: {:,.5f}".format( totalDistance) )
print( "Execution time: %s seconds.\n" %execTime )

tsp.close()