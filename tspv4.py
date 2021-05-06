import numpy as np
import sys
import time
import math
import random as rand

#Declaring variables
infoLoop = False
nodes = []
tempNodesDistances = []
alpha = 0.4 #Greedy ಠ_ಠ
tempConsiderDistances = []
tempConsiderNodes = []
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
for i in range( 0, dimension-2 ) :
    tempNodesDistances.clear()
    tempMinDistance = sys.float_info.max
    tempMaxDistance = 0
    djE = 0
    tempConsiderDistances.clear()
    tempConsiderNodes.clear()
    tempCoords.clear()
    amountConsiderNodes = 0
    for j in range( 0, dimension ) : #Obtain all its euclidean distances from actual node
        x2 = nodes[j][0]
        y2 = nodes[j][1]
        euclideanDistance = Eu2D( x1, y1, x2, y2)
        
        tempNodesDistances.append(euclideanDistance)

    if sum( nodeBool ) > 1 :
        for j in range( 0, sum(nodeBool) ) :    #Obtain the smallest and greater distances between actual node and neighbors
            if (tempNodesDistances[j] < tempMinDistance) and (tempNodesDistances[j] != 0) and ( nodeBool[j] == True ) :
                tempMinDistance = tempNodesDistances[j]
            if (tempNodesDistances[j] > tempMaxDistance) and ( nodeBool[j] == True ) :
                tempMaxDistance = tempNodesDistances[j]

        djE = ( tempMinDistance + ( alpha*( tempMaxDistance-tempMinDistance ) ) )

        for j in range( 0, sum(nodeBool) ) :
            if tempNodesDistances[j] <= djE and nodeBool[j] == True: 
                tempConsiderDistances.append( tempNodesDistances[j] )
                tempConsiderNodes.append( j )
                amountConsiderNodes += 1
        print( nodeBool )
        print( "Amount of True: %s"  %sum(nodeBool))
        print( amountConsiderNodes )
        print( tempConsiderDistances)
        nRand = rand.randint(0, amountConsiderNodes)

        route.append( tempConsiderNodes[nRand]+1 )
        routeDistance += tempConsiderDistances[nRand]

        nodeBool[ tempConsiderNodes[nRand] ] = False

        tempCoords = nodes[tempConsiderNodes[nRand]].copy()
        x1 = tempCoords[0]
        y1 = tempCoords[1]