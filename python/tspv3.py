import numpy as np
import sys
import time
import math
import random as rand

#Declaring variables
nodes = []
route = []
routeCoords = []
nodesDistance = []
nodesNumbers = []
tempNodesDistances = []
tempNodesNumbers = []
tempRouteCoords = []
totalDistance = 0
maxIter = 10

#Function to calculate Euclidean Distance
def Eu2D(x1, y1, x2, y2):
    return np.sqrt( (x1-x2)**2 + (y1-y2)**2 )

#Open the file we want to use
tsp = open("ulysses16.tsp", "r")

#Jump lines to 'Dimension', save its dimension and jump to coordenates
for x in range(3):
    tsp.readline()
dimension = int( tsp.readline().split()[1] )
for x in range(2):
    tsp.readline()
n = dimension-1

#Save coordinates in a matrix called 'nodes' and assings the status of True to all nodes.
for i in range(0, dimension):
    x,y = tsp.readline().strip().split()[1:]
    nodes.append([float(x), float(y)])
status = [True for i in range(dimension)]

#Asks user where to start, save input as integer subtracting one. Saves initial coordinates as 'initCoords' and its coordinates.
initNumber = int( input("From 1 to %s\n\tWhere do you want to start?: " %dimension) ) - 1
initCoords = nodes[initNumber]
x1 = initCoords[0]
y1 = initCoords[1]

#Append variables to 'route' and 'routeCoords'.
route.append(initNumber+1)
routeCoords.append(initCoords)

#Algorithm timer execute
startTime = time.time()

#Nearest Neighbor with k-best method
for i in range( 0, dimension-2 ) :
    tempMinDist = sys.float_info.max
    nodesDistance.clear()
    nodesNumbers.clear()
    tempNodesDistances.clear()
    tempNodesNumbers.clear()
    possibleNodes = 0
    for j in range( 0, n ) : #Obtain all euclidean distances
        x2 = nodes[j][0]
        y2 = nodes[j][1]
        
        euclideanDistance = Eu2D(x1, y1, x2, y2 )
        nodesDistance.append(euclideanDistance)
        nodesNumbers.append(j)
    status[initNumber] = False

    for j in range(0, n) : 
        if nodesDistance[j] < tempMinDist and nodesDistance[j] != 0 and status[j] == True :
            tempMinDist = nodesDistance[j]
            tempNumber = j
            nodeSelected = nodes[j]
            possibleNodes += 1
    tempNodesDistances.append(tempMinDist)
    tempNodesNumbers.append(tempNumber)
    possibleNodes += 1
    tempRouteCoords.append(nodeSelected)

    tempMinDist = sys.float_info.max
    if n > 1 :
        for j in range(0, n) :
            if (nodesDistance[j] < tempMinDist) and (nodesDistance[j] != 0) and (status[j] == True) and (nodesDistance[j] != tempNodesDistances[0]) :
                tempMinDist = nodesDistance[j]
                tempNumber = j
                nodeSelected = nodes[j]
                possibleNodes += 1
    tempNodesDistances.append(tempMinDist)
    tempNodesNumbers.append(tempNumber)
    
    tempRouteCoords.append(nodeSelected)

    tempMinDist = sys.float_info.max
    if n > 2 :
        for j in range(0, n) :
            if (nodesDistance[j] < tempMinDist) and (nodesDistance[j] != 0) and (status[j] == True) and (nodesDistance[j] != tempNodesDistances[0]) and (nodesDistance[j] != tempNodesDistances[1]) :
                tempMinDist = nodesDistance[j]
                tempNumber = j
                nodeSelected = nodes[j]
                possibleNodes += 1
    tempNodesDistances.append(tempMinDist)
    tempNodesNumbers.append(tempNumber)
    
    tempRouteCoords.append(nodeSelected)
    
    randomN = rand.randint(0, possibleNodes-1)
    route.append( tempNodesNumbers[randomN]+1 )
    routeCoords.append( tempRouteCoords[randomN] )
    status[ tempNodesNumbers[randomN] ] = False
    print(tempNodesDistances)

    x2 = nodeSelected[0]
    y2 = nodeSelected[1]

for i in range(0, dimension) :
    if status[i] == True :
        totalDistance += Eu2D(x2, y2, nodes[i][0], nodes[i][1])
        route.append(i+1)

print("\n")
print(nodes[i])
print(route)
print("Total distance: %s" %totalDistance)

tsp.close()