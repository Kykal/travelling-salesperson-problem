#Libraries
from os import stat
from typing import get_origin
import numpy as np
import sys
import random

#Declaring variables
coords = []
k = 0.1 #alpha
coords = []
route = []
routeCoords = []

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
Tmax = int(Tmax)
dimension = int( dimension  ) - 1
status = [ True for i in range(0, dimension+1) ]    #Set all nodes the status of 'True' (can be visited)
tempStatus = status.copy()
for i in range(0, dimension+1) :      #Save all nodes coords and score in an array called 'coords'
    x,y,z = tsp.readline().strip().split()
    coords.append( [float(x), float(y), float(z)] )

initialCoords = [ coords[0][0], coords[0][1] ]
x1 = initialCoords[0]
y1 = initialCoords[1]
endCoords = [ coords[1][0], coords[1][1] ]

print( "\n"+filename+" file loaded!" )

#Constructive
minDistance = sys.float_info.max
for i in range(2, dimension+1) :
    x2 = coords[i][0]
    y2 = coords[i][1]
    distance = Eu2D( x1, y1, x2, y2 )
    if distance <= minDistance :
        minDistance = distance
        minNode = i
        tempStatus[i] = False

