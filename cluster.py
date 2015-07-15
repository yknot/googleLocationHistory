import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
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

# filter data
def filterPoints(x1, x2, y1, y2, Data):
    subset = []
    for P in Data:
        if P.lon > x1 and P.lon < x2:
            if P.lat > y1 and P.lat < y2:
                subset.append(P)

    return subset

# plot cluster data
def plot(DF):
    uniq = list(set([P.cluster for P in DF]))

    z = range(1,len(uniq))
    hot = plt.get_cmap('hot')
    cNorm = colors.Normalize(vmin=0, vmax=len(uniq))
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=hot)

    for P in DF:
        plt.scatter(P.lon, P.lat, s=15, color=scalarMap.to_rgba(P.cluster))

    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Plotting Clusters')
    plt.show()

# save data to csv for mapping
def save(DF, name):
    with open(name + '.csv', 'w') as out:
        out.write('lat,lon,cluster\n')
        for P in DF:
            out.write(str(P.lat) + ',' + str(P.lon) + ',' + str(P.cluster) + '\n')


# read in to multi dimensional array
HISTORY = [line.strip().split(',') for line in open('history-2014.csv')]

Data = []

# head of the file
for row in HISTORY[1:]:
    Data.append(Point(row[0], row[1], row[2], row[3], row[4]))



# Northeast
# NE = filterPoints(-80,-65,35,50, Data)
#
# eps = .0000001
# MinPts = 3
# DBSCAN(NE, eps, MinPts)
#
# plot(NE)
#
# save(NE, 'NE')

# San Fran
SF = filterPoints(-125, -119, 35, 40, Data)

eps = .1
MinPts = 3
DBSCAN(SF, eps, MinPts)

plot(SF)

save(SF, 'SF')
