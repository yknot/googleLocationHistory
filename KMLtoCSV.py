import os

import sys, csv, codecs
from pykml import parser as kmlParser



# from pykml import parser
# import csv


# def getDocument(kml):
# 	root = kml.getroot()
# 	return root.Document

# def getData(filename):
# 	document = getDocument(parser.parse(open(filename)))






# for k in kmlFiles:
# 	getData(k)










def getDocumentAndTagPrefix(xml):
	root = xml.getroot();
	tagPrefix = root.tag.replace( '}' + xml.docinfo.root_name, '}' )
	return root.Document, tagPrefix

def iterFolders(folder, tagprefix):
	lst = [ i for i in folder.iterchildren(tagprefix+'Placemark') ]
	return folder if not len(lst) else iter(lst)

def getdata(filename):
	document, tagPrefix =getDocumentAndTagPrefix( kmlParser.parse( open(filename) ) )
	mainFolder = document.Placemark
	
	name = None
	placemarks = None;
	for folder in iterFolders(mainFolder, tagPrefix):
		name = folder.iterchildren(tagPrefix+"name").next().text
		placemarks = [ x for x in folder.iterchildren(tagPrefix+"gx:Track") ]
		break;
	return name,placemarks;

def places_to_list(places):
	lst = [
		['name','lat','lon', 'coordinates']
	]

	for place in places:
		lst.append([
			place.name, place.LookAt.latitude, place.LookAt.longitude
			, place.Point.coordinates
		])
	return lst

def to_csv(filename, lst):
	with codecs.open(filename, 'w', encoding='utf8') as fl:
		out = csv.writer(fl);	
		out.writerows( lst )





kmlFiles = [ f for f in os.listdir('.') if f[-4:] == '.kml' ]
filename = kmlFiles[0]

name, places = getdata(filename)
lst = places_to_list(places)


filename = filename.replace('.kml','.csv')

to_csv(filename, lst)

print "See {filename}\nGoodluck (^_^)!".format(filename=filename)
