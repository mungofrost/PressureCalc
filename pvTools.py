########################
# pvTools.py
# various common fuctions for the PfV (pressure from volume) and VfP (volume from pressure) scripts

import math

#######################################
# vinet, takes volume, volume at no pressure, bulk modulus and pressure derivative of bulk modulas and caulculates pressure from vinet equation of state
def vinet (V,V0,B0,B1):
	eta = (V/V0)**(1./3.)
	P = 3*B0*((1.-eta)/eta**2)*math.exp((3./2.)*(B1-1.)*(1-eta))
	return P


#########################################
# vinetVolume, takes pressure, volume at no pressure, bulk modulus and pressure derivative of bulk modulus and iterates to find volume using vinet EoS

def vinetVolume (P,V0,B0,B1):
		
	#volume and upper and lower bounds
	V = V0
	Vlower = 0.
	Vupper = V0
	
	Pcalc = vinet(V,V0,B0,B1)
	
	#iterate until Pcalc converges on desired pressure, P
	while abs(P-Pcalc) > 0.0001:
		
		#volume guessed as mid point of bounds and Pcalc updated
		V = (Vupper+Vlower)/2.
		Pcalc = vinet(V,V0,B0,B1)
		
		#volume to small (ie Pcalc bigger than P)
		if Pcalc > P:
			Vlower = V
		
		#otherwise volume was too big and Pcalc too low
		else:
			Vupper = V
	
	#now Pcalc approx P and V corresponds
	
	return V

	
########################################
#Filereader:
#
# Takes file of form:
# <element> <V0> <B0> <B1> <str (optional)>
# and returns list [V0,B0,B1,str]
## ignores '#' comments
#
# Input is file object and desired element
# If element is absent returns 'None'
# Otherwise returns [V0,B0,B1,str] as float,float,float,string

def pvFilereader (dataFile, symbol):
	
	lines = dataFile.readlines()
	
	# read through file, if starts with element save it
	data = None
	
	for line in lines:
		
		#Catch empty lines
		if line.split == []:
			continue
			
		if line.split()[0] == symbol:
			data = line
			
			#convert data string to list of items
			data = data.split()
	
			#add 'no' if structure absent
			if len(data) == 4:
				data.append('no')
			
			#convert V0,B0,B1 to floats
			for i in range(1,4):
				data[i] = float(data[i])
			
			#get rid of symbol
			data.pop(0)
			
			break
		
	return data
	
	
	
	
	

