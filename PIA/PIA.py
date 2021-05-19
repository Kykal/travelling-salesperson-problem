#Libraries
from os import stat
import numpy as np
import sys
import random

#Declaring variables
dimension = 0
coords = []
route = []

#Function to calculate Euclidean Distance
def Eu2D(x1, y1, x2, y2):
    return np.sqrt( (x1-x2)**2 + (y1-y2)**2 )

#Open and read the .txt file, obtain its information.
path = "datasets/"
filename = "set_64_1_15"
filenamePath = path+filename+".txt"
totalDistance = 0
distance = 0
minWorth = sys.float_info.max
availableNodes = []
availableCoords = []
availableDistances = []

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
dimension = int( dimension )
status = [ True for i in range(0, dimension-1) ]    #Set all nodes the status of 'True' (can be visited)
for i in range(0, dimension) :      #Save all nodes coords and score in an array called 'coords'
    x,y,z = tsp.readline().strip().split()
    coords.append( [float(x), float(y), float(z)] )

print( "\n"+filename+" file loaded!" )

#Save initial coordinates
initCoord = coords[0]
x1 = initCoord[0]
y1 = initCoord[1]
route.append(1)
status[0] = False
tempStatus = status.copy()

print( "\nInitial coords: [%s][%s]\n" %(x1, y1) )
#Save the neighbor nodes that can be visited withouth exceed our Tmax
if sum( status ) > 1 :
    for i in range(2, dimension) :
        x2 = coords[i][0]
        y2 = coords[i][1]
        distance = Eu2D( x1, y1, x2, y2 )
        actualWorth = distance/coords[i][2]   #The least the better
        if ( actualWorth <= minWorth ) and ( tempStatus[i] == True ) :
            minWorth = actualWorth.copy()
            minNode = i
            minDistance = distance.copy()

    availableNodes.append(minNode)
    availableCoords.append(coords[minNode])
    availableDistances.append(minDistance)
    tempStatus[minNode] = False
    x1 = coords[minNode][0]
    y1 = coords[minNode][1]

minWorth = sys.float_info.max
for i in range(2, dimension) :
    distance = Eu2D( x1, y1, x2, y2 )
    actualWorth = distance/coords[i][2]   #The least the better
    if ( actualWorth <= minWorth ) and ( tempStatus[i] == True ) :
        minWorth = actualWorth.copy()
        minNode = i
        minDistance = distance.copy()

availableNodes.append(minNode)
availableCoords.append(coords[minNode])
availableDistances.append(minDistance)
tempStatus[minNode] = False

minWorth = sys.float_info.max
for i in range(2, dimension) :
    distance = Eu2D( x1, y1, x2, y2 )
    actualWorth = distance/coords[i][2]   #The least the better
    if ( actualWorth <= minWorth ) and ( tempStatus[i] == True ) :
        minWorth = actualWorth.copy()
        minNode = i
        minDistance = distance.copy()

availableNodes.append(minNode)
availableCoords.append(coords[minNode])
availableDistances.append(minDistance)
tempStatus[minNode] = False

randNumber = random.randint()