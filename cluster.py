import pylab as pl
import math
from sets import Set


class Point(object):
    """Point class for lat, lon, visited, and cluster"""
    def __init__(self, date, time, timezone, lon, lat):
        self.date, self.time, self.timezone = date, time, timezone
        self.lon, self.lat = float(lon), float(lat)
        self.visited = self.cluster = 0

    def __str__(self):
        return """
Date:  """ + self.date + """
Time:  """ + self.time + """
TZ:    """ + self.timezone + """
Lat:   """ + str(self.lat) + """
Lon:   """ + str(self.lon) + """
Visit: """ + str(self.visited) + """
Clust: """ + str(self.cluster)


# pass in data frame, eps, minpts
def DBSCAN(D, eps, MinPts):
    # set cluster counter
    C = 1
    date = ''
    print 'Starting Loop'
    # for each point in the data
    for P in D:
        if date != P.date:
            date = P.date
            print date
        # if visited continue
        if P.visited:
            continue
        # set as visited
        P.visited = 1
        # find neightbor pts
        # NeighborPts is set of indexes
        NeighborPts = regionQuery(P, D, eps)

        # if not enough points set as noise
        if len(NeighborPts) < MinPts:
            P.cluster = -1
        # else expand the cluster to nearby points
        else:
            expandCluster(P, NeighborPts, C, D, eps, MinPts)
            C += 1

# distance equation for 2 points
def distance(P, Q):
    return math.sqrt(pow(Q.lat-P.lat,2) + pow(Q.lon-P.lon,2))

# return all points within P's eps-neighborhood (including P)
def regionQuery(P, D, eps):
    NeighborPts = Set()
    for i in range(len(D)):
        if distance(P, D[i]) < eps:
            NeighborPts.add(i)

    return NeighborPts


# recursively check to see if neighboorhood can be expanded
def expandCluster(P, NeighborPts, C, D, eps, MinPts) :
    # set P to cluster C
    P.cluster = C
    # for each new P in NeighborPts
    for j in NeighborPts:
        # if not visited, set to visited
        if not D[j].visited:
            D[j].visited = 1
            # find new NeighborPts based on new prime
            NeighborPtsNew = regionQuery(D[j], D, eps)
            # if big enough list join with current list
            if len(NeighborPtsNew) >= MinPts:
                NeighborPts = NeighborPts | NeighborPtsNew

        if D[j].cluster == 0:
            D[j].cluster = C





# read in to multi dimensional array
HISTORY = [line.strip().split(',') for line in open('history-2014.csv')]

Data = []

# head of the file
for row in HISTORY[1:]:
    Data.append(Point(row[0], row[1], row[2], row[3], row[4]))

# filter D down to only northeast NE
NE = []
for P in Data:
    if P.lon > -80 and P.lon < -65:
        if P.lat > 35 and P.lat < 50:
            NE.append(P)
#
# SF = []
# for P in Data:
#     if P.lon > -125 and P.lon < -119:
#         if P.lat > 35 and P.lat < 40:
#             SF.append(P)

# pl.scatter([P.lat for P in SF], [P.lon for P in SF])

eps = .1
MinPts = 3
DBSCAN(NE, eps, MinPts)



# with open('SF.csv', 'w') as out:
#     out.write('lat,lon,cluster\n')
#     for P in SF:
#         out.write(str(P.lat) + ',' + str(P.lon) + ',' + str(P.cluster) + '\n')



with open('NE.csv', 'w') as out:
    out.write('lat,lon,cluster\n')
    for P in NE:
        out.write(str(P.lat) + ',' + str(P.lon) + ',' + str(P.cluster) + '\n')
