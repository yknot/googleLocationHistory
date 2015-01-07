import os
import re


# get raw text in a string
def getRaw(f):
	return open(f).read()

# return list of all instances found
def getRegEx(raw, exp):
	p = re.compile(exp)

	return re.findall(p, raw)

def writeFile(t, f):
	f = f[:-4] + '.csv'

	g = open(f, 'w')
	g.write(t)
	g.close


# get the data from the kml file
def getData(filename):
	raw = getRaw(filename)

	# get regex results
	whens = getRegEx(raw, '<when>(.*)T(.*)(-.*)</when>')
	coords = getRegEx(raw, '<gx:coord>(.*) (.*) (.*)</gx:coord>')

	return whens, coords

	


# get all the kml files
kmlFiles = [ f for f in os.listdir('kmls/') if f[-4:] == '.kml' ]

csv = 'date,time,timezone,lon,lat\n'


# run through each file
for k in kmlFiles:
	whens, coords = getData('kmls//' + k)

	for i in xrange(len(whens)):
		csv += whens[i][0] + ',' + whens[i][1] + ',' + whens[i][2] + ',' + coords[i][0] + ',' + coords[i][1] + '\n'


writeFile(csv, 'history-2014.csv')


