#Libraries
from os import stat
from typing import get_origin
import numpy as np
import sys
import random

from numpy.lib.function_base import select

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

#Function to calculate Euclidean Distance
def Eu2D(x1, y1, x2, y2):
    return np.sqrt( (x1-x2)**2 + (y1-y2)**2 )

#Open and read the .txt file, obtain its information.
path = "datasets/"
filename = "set_64_1_15"
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
dimension = int( dimension  ) - 1
status = [ True for i in range(0, dimension-1) ]    #Set all nodes the status of 'True' (can be visited)
tempStatus = status.copy()
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

routeCoords.append( xyRoute )

print( "\nInitial coords: [%s][%s]\n" %(x1, y1) )

for i in range(0, 3) :
    minDistance = sys.float_info.max
    if sum( status ) > k :
        for i in range(2, dimension+1) :    #Compare euc. distances from actual node to neighbor nodes to obtain the lowest euc. distance available 
            x2 = coords[i][0]
            y2 = coords[i][1]

            distance = Eu2D( x1, y1, x2, y2 )
            if (distance < minDistance) and ( status[i] == True ) :
                minDistance = distance
                minNode = i
        
        status[minNode] = False
        availableNodes.append( minNode )
        availableCoords.append( coords[minNode] )
        availableDistances.append( minDistance )
        if k < 3 :
            k += 1
    else :
        break

randomNumber = random.randint( 0, k-1 )
route.append( availableNodes[randomNumber] )
xyRoute = [ availableCoords[randomNumber][0], availableCoords[randomNumber][1] ]
routeCoords.append( xyRoute )
totalDistance = availableDistances[randomNumber]
score += coords[availableNodes[randomNumber]][2]

print( route )
print( routeCoords )
print( totalDistance )
print( score )