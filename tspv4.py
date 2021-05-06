import numpy as np
import sys
import time
import math
import random as rand

#Declaring variables
infoLoop = False
nodes = []
tempEuclideanDistances = []
alpha = 0.1 #Greedy ಠ_ಠ
tempDistances = []
tempNodes = []
tempCoords = []
route = []
routeDistance = 0

#Function to calculate Euclidean Distance
def Eu2D(x1, y1, x2, y2):
    return np.sqrt( (x1-x2)**2 + (y1-y2)**2 )

#Open the file we want to use.
tsp = open("TSP/test.tsp", "r")

#Save its information.
while infoLoop == False :
    actualLine = tsp.readline().split()
    actualLineLenght = len(actualLine)
    if actualLine[0] == 'NAME' or actualLine[0] == 'NAME:' :
        filename = actualLine[actualLineLenght-1]
        print( "\n%s.tsp file loaded!\n" %filename )
    elif actualLine[0] == 'DIMENSION' or actualLine[0] == 'DIMENSION:' :
        dimension = int( actualLine[actualLineLenght-1] )
        nodeBool = [ True for i in range(0, dimension) ]
    elif actualLine[0].isnumeric() == True :
        x,y = actualLine[1:]
        nodes.append([float(x), float(y)])
    if actualLine[0] == 'EOF' :
        infoLoop = True

#Algorithm timer execute
startTime = time.time()

#Start point !!!!!!!!!!!!!!
initNumber = int( input("From 1 to %s\n\tWhere do you want to start?: " %dimension) ) - 1
initCoords = nodes[initNumber]
x1 = nodes[initNumber][0]
y1 = nodes[initNumber][1]
route.append(initNumber+1)
nodeBool[initNumber] = False

#Multi-start with alpha
for i in range( 0, dimension-1 ) :
    tempMinEucDistance = sys.float_info.max
    tempMaxEucDistance = 0
    tempNodes.clear()
    tempDistances.clear()
    tempCoords.clear()
    tempEuclideanDistances.clear()
    for j in range( 0, dimension ) : #Obtain all its euclidean distances from actual node
        x2 = nodes[j][0]
        y2 = nodes[j][1]
        euclideanDistance = Eu2D( x1, y1, x2, y2)
        
        tempEuclideanDistances.append(euclideanDistance)

    for j in range( 0, dimension ) :    #Looking for the smallest and greatest distance from my actual node to neighbors
        if (tempEuclideanDistances[j] > tempMaxEucDistance) and (nodeBool[j] == True) :
            tempMaxEucDistance = tempEuclideanDistances[j].copy()
        if (tempEuclideanDistances[j] < tempMinEucDistance) and (nodeBool[j] == True) :
            tempMinEucDistance = tempEuclideanDistances[j].copy()
    
    djE = tempMinEucDistance + ( alpha*(tempMaxEucDistance-tempMinEucDistance) )

    sumTrues = sum(nodeBool)
    
    if sumTrues > 1 :
        for j in range( 0, dimension ) :
            if ( tempEuclideanDistances[j] <= djE ) and ( nodeBool[j] == True ) :
                tempDistances.append( tempEuclideanDistances[j] )
                tempNodes.append( j )
                tempCoords.append(nodes[j])
        nRand = rand.randint( 0, len(tempNodes)-1 )
        nodeBool[ tempNodes[nRand] ] = False
        x1 = tempCoords[nRand][0]
        y1 = tempCoords[nRand][1]
        routeDistance += tempDistances[nRand]

        route.append( tempNodes[nRand]+1 )
    elif sumTrues == 1: 
        for j in range( 0, dimension ) :
            if nodeBool[j] == True :
                routeDistance += Eu2D(x1, y1, nodes[j][0], nodes[j][1])
                route.append( j+1 )
                x1 = nodes[j][0]
                y1 = nodes[j][1]

routeDistance += Eu2D( x1, y1, nodes[initNumber][0], nodes[initNumber][1] )
route.append( initNumber+1 )

execTime = time.time() - startTime

print( "Best route: %s" %route)
print( "Best distance: %s distance units" %routeDistance )
print( "Time elapsed: %s seconds" %execTime)