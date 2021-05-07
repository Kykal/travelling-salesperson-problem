import numpy as np
import sys
import time
import math
import random as rand

#Declaring variables
infoLoop = False
nodes = []
tempEuclideanDistances = []
tempDistances = []
tempNodes = []
tempCoords = []
route = []
routeDistance = 0
routeCoords = []
realRoute = []
realDistance = 0
alpha = 0.1 #Greedy ಠ_ಠ
timeLimit = 600.0 #seconds
bestDistance = sys.float_info.max
timeLimitExceed = False

#Function to calculate Euclidean Distance
def Eu2D(x1, y1, x2, y2):
    return np.sqrt( (x1-x2)**2 + (y1-y2)**2 )

#Open the file we want to use.
tsp = open("TSP/eil76.tsp", "r")

#Save its information.
while infoLoop == False :
    actualLine = tsp.readline().split()
    actualLineLenght = len(actualLine)
    if actualLine[0] == 'NAME' or actualLine[0] == 'NAME:' :
        filename = actualLine[actualLineLenght-1]
        print( "\n%s file loaded!\n" %filename )
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
print( "\nCalculating, please wait...\n" )
initCoords = nodes[initNumber]
x1 = nodes[initNumber][0]
y1 = nodes[initNumber][1]
route.append(initNumber+1)
nodeBool[initNumber] = False
routeCoords.append(initCoords)

#Multi-start with alpha
for x in range( 0, 3**dimension ) : 
    actualTime = time.time() - startTime
    if actualTime >= timeLimit :
        timeLimitExceed = True
        break
    x1 = nodes[initNumber][0]
    y1 = nodes[initNumber][1]
    route.clear()
    route.append(initNumber+1)
    routeDistance = 0
    nodeBool = [ True for i in range(0, dimension) ]
    nodeBool[initNumber] = False
    realDistance = 0
    realRoute.clear()
    routeCoords.clear()
    routeCoords.append(initCoords)
    lsDistance = 0

    for i in range( 0, dimension-1 ) :
        if actualTime >= timeLimit :
            timeLimitExceed = True
            break
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
            routeCoords.append(tempCoords[nRand])
            route.append( tempNodes[nRand]+1 )
        elif sumTrues == 1: 
            for j in range( 0, dimension ) :
                if nodeBool[j] == True :
                    routeDistance += Eu2D(x1, y1, nodes[j][0], nodes[j][1])
                    route.append( j+1 )
                    x1 = nodes[j][0]
                    y1 = nodes[j][1]
                    routeCoords.append( nodes[j] )

    routeDistance += Eu2D( x1, y1, nodes[initNumber][0], nodes[initNumber][1] )
    route.append( initNumber+1 )
    routeCoords.append( initCoords )
    realRouteCoords = routeCoords.copy()

    realRoute = route.copy()
    realDistance = routeDistance.copy()

    if realDistance < bestDistance :
        bestDistance = realDistance.copy()
        bestRoute = realRoute.copy()
        print("Alpha notifiacion:\n\tCyle: {:,.0f}\tBest distance at the moment: {:,.5f}" .format(x+1, bestDistance))
        print( "\tRoute: %s" %bestRoute)

    #Local search (2node-switch)
    for k in range(1, dimension-1) :
        aux = realRouteCoords[k]
        realRouteCoords[k] = realRouteCoords[k+1]
        realRouteCoords[k+1] = aux.copy()

        aux = realRoute[k]
        realRoute[k] = realRoute[k+1]
        realRoute[k+1] = aux

        lsDistance = 0
        for f in range(0, dimension) :
            lsDistance += Eu2D( realRouteCoords[f][0], realRouteCoords[f][1], realRouteCoords[f+1][0], realRouteCoords[f+1][1]  )
        
        if lsDistance < bestDistance :
            bestDistance = lsDistance.copy()
            bestRoute = realRoute.copy()
            print("Local Search notification:\n\tCyle: {:,.0f}\tBest distance at the moment: {:,.5f}" .format(x+1, bestDistance))
            print( "\tRoute: %s\n" %realRoute)
    
    actualTime = time.time() - startTime
    if actualTime >= timeLimit :
        print( "\nTime limit exceeded [{:,.0f} second(s)]. Terminating program." .format(timeLimit) )
        break

execTime = time.time() - startTime

print( "\nBest route: %s" %bestRoute)
print( "Best distance: {:,.2f} distance units" .format( bestDistance ) )
print( "Time elapsed: %s seconds\n" %execTime)