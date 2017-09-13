#Pressure from Volume or h k l d

# Takes either  <element> <volume> or <element> <h> <k> <l> <d> from command line
# outputs pressure

#####
# Stuff which might want changed:

datafile = 'pvdata.dat'

#####
#Imports

import sys
import pvTools

#####
#



#######
#Volume calculator from h k l d
##

def vCalc (h,k,l,d,struct):
	#####
	#Supports only cubic
	if struct not in ['fcc','bcc']:
		print ("h k l volume only sipported for cubic crystal systems")
		input("Quitting")
		exit()
	
	vol = ((h*h+k*k+l*l)**(1./2.)*d)**3.
		
	#want volume per atom, fcc has 4 per cell, bcc 2
	if struct == 'fcc':
		return vol/4.0
	else:
		return vol/2.0
	
	
		
###########################
# Code begins
#########

arguments = sys.argv
arguments.pop(0) #argv[0] is name of script

#####
#Check there are 2 or 5 arguments
if len(arguments) not in [2,5]:
	print ("The program requires either two (<element> <volume) or 5 (<element> <h> <k> <l> <d>) inputs.")
	input("Quitting.")
	exit()

#########
#Extract element data

file = open(datafile,'r')
elementData = pvTools.pvFilereader(file, sys.argv[0])

#catch missing data
if elementData is None:
	print ("Element not in " + datafile + "\n")
	input("Return to quit") 
	exit()
	
V0,B0,B1,struct = elementData
structure = struct.lower() #avoid fucking about with capitals


#########
# Volume

V = 0

# check arguments are good and get volume

# input is <element> <volume> 
if len(sys.argv) == 2:
	V = float(sys.argv[1])

#input is <element> <h> <k> <l> <d>
else:
	#check structure is supported (fcc,bcc currently)
	acceptedStructures = ['fcc','bcc']
	if structure not in acceptedStructures:
		print ("Structure not supported for h k l d volume calculation, please use PfV.py <volume> <element> mode")
		input("Quitting.")
	
	else:
		h,k,l,d = sys.argv[1:5]
		h = int(h)
		k = int(k)
		l = int(l)
		d = float(d)
		V = vCalc(h,k,l,d,structure)
		
#######
# Now use V, V0, B0, B1 to get P via vinet EoS

pressure = pvTools.vinet(V,V0,B0,B1)

print ("Pressure is " + str(round(pressure,3)) + "   (units as in " + datafile + ")")
