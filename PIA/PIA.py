#Libraries
from os import stat
from typing import get_origin
import numpy as np
import sys
import random

#Declaring variables
dimension = 0
coords = []
coordsScore = []
route = []
routeCoords = []
score = 0
totalDistance = 0
availableNodes = []
availableCoords = []
availableDistances = []
k = 1
routeComplete = False

#Function to calculate Euclidean Distance
def Eu2D(x1, y1, x2, y2):
    return np.sqrt( (x1-x2)**2 + (y1-y2)**2 )

#Open and read the .txt file, obtain its information.
path = "datasets/"
filename = "set_64_1_25"
filenamePath = path+filename+".txt"

tsp = open( filenamePath, 'r' )
if filenamePath.split('_')[0] == 'datasets/set' :   #Check filename to know the dataset dimension
    dimension = filenamePath.split('_')[1]
elif (filenamePath.split('_')[1] == 'problem') :
    if filenamePath.split('_')[2] == '1' :
        dimension = 32
    if filenamePath.split('_')[2] == '2' :
        dimension = 21
    if filenamePath.split('_')[2] == '3' :
        dimension = 33
Tmax = tsp.readline().strip().split()[0]        #Save the available time budget per path as 'Tmax'
Tmax = int(Tmax)
dimension = int( dimension  ) - 1
status = [ True for i in range(0, dimension+1) ]    #Set all nodes the status of 'True' (can be visited)
for i in range(0, dimension+1) :      #Save all nodes coords and score in an array called 'coords'
    x,y,z = tsp.readline().strip().split()
    coords.append( [float(x), float(y), float(z)] )

print( "\n"+filename+" file loaded!" )
print( "From node 0 to %s" %dimension )

#Save initial coordinates
initCoord = coords[0]
x1 = initCoord[0]
y1 = initCoord[1]
xyRoute = [x1,y1]
route.append(0)
status[0] = False

routeCoords.append( xyRoute )

print( "\nInitial coords: [%s][%s]\n" %(x1, y1) )
while routeComplete == False :
    availableCoords.clear()
    availableDistances.clear()
    availableNodes.clear()
    tempStatus = status.copy()
    minNode = None
    distance = 0
    k=1
    for j in range(0, 3) :
        if sum( tempStatus ) > k or minNode != None :
            minDistance = sys.float_info.max
            for i in range(2, dimension+1) :    #Compare euc. distances from actual node to neighbor nodes to obtain the lowest euc. distance available 
                x2 = coords[i][0]
                y2 = coords[i][1]
                distance = Eu2D( x1, y1, x2, y2 )
                goBackDistance = Eu2D( x2, y2, coords[1][0], coords[1][1] )
                tempCompleteDistance = float(totalDistance + goBackDistance)
                if (tempCompleteDistance <= Tmax) :
                    if (distance < minDistance) and ( tempStatus[i] == True ) :
                        minDistance = distance
                        minNode = i
                else :
                    status[i] = False
                    distance = 0
                    minDistance = 0
                    minNode = None
            if minNode != None : 
                tempStatus[minNode] = False
                availableNodes.append( minNode )
                availableCoords.append( coords[minNode] )
                availableDistances.append( minDistance )
                if k < 3 :
                    k += 1
            elif minNode == None :
                distance = 0
                minDistance = 0
                break
    if minNode != None : 
        randomNumber = random.randint( 0, k-1 )
        route.append( availableNodes[randomNumber] )
        xyRoute = [ availableCoords[randomNumber][0], availableCoords[randomNumber][1] ]
        routeCoords.append( xyRoute )
        status[ availableNodes[randomNumber] ] = False
        totalDistance += availableDistances[randomNumber]
        score += coords[availableNodes[randomNumber]][2]
        x1 = coords[availableNodes[randomNumber]][0]
        y1 = coords[availableNodes[randomNumber]][1]
    else :
        routeComplete = True

route.append(1)
xyRoute = [ coords[1][0], coords[1][1] ]
routeCoords.append( xyRoute )
distance = Eu2D( routeCoords[len(route)-2][0], routeCoords[len(route)-2][1], coords[1][0],coords[1][1] )
totalDistance += distance

bestDistance = totalDistance.copy()

#Local Search
for m in range( 1, dimension-2 ) :
    aux = route[m]
    route[m] = route[m+1]
    route[m+1] = aux
    
    aux = routeCoords[m]
    routeCoords[m] = routeCoords[m+1]
    routeCoords[m+1] = routeCoords[m]

    lsDistance = 0
    for f in range(0, len(route)-1 ) :
        lsDistance += Eu2D( routeCoords[f][0], routeCoords[f][1], routeCoords[f+1][0], routeCoords[f+1][1] )

    if lsDistance < bestDistance : 
        bestDistance = lsDistance.copy()
        bestRoute = route.copy()



print( "%s\n%s\n" %(route, routeCoords) )
print( "Distance: {:,.4f} m\nScore: {:,.0f}\n" .format(totalDistance, score).replace(',', ' ') )