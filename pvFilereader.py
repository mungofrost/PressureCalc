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
		
		if line.split(None,1)[0] == symbol:
			data = line

			#convert data string to list of items
			data = data.split()
	
			#add 'no' if structure absent
			if len(data) == 4
				data.append('no')
			
			#convert V0,B0,B1 to floats
			for i in range(1,3):
				data[i] = float(data[i])
			
			#get rid of symbol
			data.pop(0)
		
	return data
	
	
	
	
	

