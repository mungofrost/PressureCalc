#Sept 2017 - updated to Python3

#volume from pressure and elemental data
#also h,k,l if cubic systems

#takes <element> <pressure> and outputs expected volume per atom

########
#Stuff which might want changed

datafile = "pvdata.dat"

######
#IMPORTS

import pvTools
import sys

######
#dcalc, uses a and h k l to find d for cubic system, takes hkl as list [h,k,l]
def dcalc(a,hkl):
	dsq = a*a/(sum(i*i for i in hkl))
	d = dsq**0.5
	return d

#################
#Code begins
##

arguments = sys.argv
sys.argv.pop(0) #pop script name

#check if there are the expected 2 arguments
if len(sys.argv) is not 2:
	print ("Requires two arguments: <element> <pressure>. ")
	input("Quitting.")
	exit()

#########
#Extract data
file = open(datafile,'r')
elementData = pvTools.pvFilereader(file, sys.argv[0])
#catch missing data
if elementData is None:
	print ("Element not in " + datafile + "\n")
	input("Return to quit")
	exit()

V0,B0,B1,struct = elementData
structure = struct.lower() #avoid fucking about with capitals

P = float(sys.argv[1])

#######
# Find volume

V = pvTools.vinetVolume(P,V0,B0,B1)

outString = "Volume at " + str(P) + " is " + str(round(V,3)) + "   (units as in " + datafile + ")"

#####
# If it's cubic there's more!

if structure in ['bcc','fcc']:

	#h k ls - different for fcc and bcc
	if structure == 'bcc':
		#h+k+l = 2n
		hkllist = [[1,1,0],[2,0,0],[2,1,1],[2,2,0],[3,1,0],[2,2,2],[4,0,0]]
		#2 atoms per cell, calculate a
		a = (2*V)**(1./3.)

	else:
		#fcc and h,k,l all odd or all even
		hkllist = [[1,1,1],[2,0,0],[2,2,0],[3,1,1],[2,2,2],[4,0,0]]
		#4 atoms per unit cell, calculate a
		a = (4*V)**(1./3.)

	#lattice parameter
	outString += "\nLattice constant a = " + str(round(a,3)) + "\n\nhkl\td\n\n"


	for hkl in hkllist:
		#find d
		dhkl = dcalc(a,hkl)
		outString += ''.join(str(hkl)) + "\t" + str(round(dhkl,3)) + "\n"

#output
print(outString)
