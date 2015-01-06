import os


# get raw text in a string
def getRaw(f):
	return open(f).read()



# get the data from the kml file
def getData(filename):
	raw = getRaw(filename)


	# loop through whens and gx:coords

	raw.find('<when>')



# get all the kml files
kmlFiles = [ f for f in os.listdir('.') if f[-4:] == '.kml' ]

# run through each file
for k in kmlFiles:
	getData(k)

