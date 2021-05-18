#Libraries
import numpy as np

#Declaring variables
regNumber = 0
coords = []

#Function to calculate Euclidean Distance
def Eu2D(x1, y1, x2, y2):
    return np.sqrt( (x1-x2)**2 + (y1-y2)**2 )

#Open and read the .txt file, obtain its information.
path = "datasets/"
filename = "set_64_1_15"
filenamePath = path+filename+".txt"

tsp = open( filenamePath, 'r' )
if filenamePath.split('_')[0] == 'datasets/set' :
    regNumber = filenamePath.split('_')[1]
elif (filenamePath.split('_')[1] == 'problem') :
    if filenamePath.split('_')[2] == '1' :
        regNumber = 32
    if filenamePath.split('_')[2] == '2' :
        regNumber = 21
    if filenamePath.split('_')[2] == '3' :
        regNumber = 33
Tmax = tsp.readline().strip().split()[0]
regNumber = int( regNumber )
for x in range(0, regNumber) :
    x,y,z = tsp.readline().strip().split()
    coords.append( [float(x), float(y), float(z)] )
coords = np.asarray(coords)

print( "\n"+filename+" file loaded!" )

#Unique user input
initNode = int( input( "\nFrom node 1 to %s, where do you want to start?: " %regNumber) ) - 1

#Algorythm

print(coords)