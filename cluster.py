import matplotlib.pyplot as plt
from scipy.spatial import cKDTree


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

    def coord(self):
        return [self.lon, self.lat]



class DBSCAN(object):
    """DBSCAN algorithm implementation
        - init with eps and minPts value
        - use addPoints to add to the tree
        - use solve to compute or re-compute clusters"""

    def __init__(self, eps, minPts):
        self.eps, self.minPts = eps, minPts
        self.points = []

    def addPoints(self, data):
        if len([p for p in data if type(p) != Point]) > 0:
            raise ValueError('Error in data passed in. Not array of points.')

        for p in data:
            self.points.append(p)

        self.coords = [p.coord() for p in self.points]

        self.tree = cKDTree(self.coords)
        self.neighbors = self.tree.query_ball_point(self.coords, self.eps)


    def solve(self):
        visited = set()
        self.clusters = []
        numCluster = -1

        for i in range(len(self.points)):
            # if visited skip it
            if i in visited:
                continue
            # add the index to visited list
            visited.add(i)

            # if the length of neighbors for i is greater than min points
            if len(self.neighbors[i]) >= self.minPts:
                # add new cluster
                self.clusters.append({i})
                # increment counter
                numCluster += 1
                # set cluster value of point to cluster number
                self.points[i].cluster = numCluster
                # points in the neighborhood
                toMerge = set(self.neighbors[i])

                while toMerge:
                    j = toMerge.pop()
                    # if j isn't visited visit and add cluster value
                    if j not in visited:
                        visited.add(j)
                        self.points[j].cluster = numCluster
                        # if minPts add them to the toMerge set
                        if len(self.neighbors[j]) >= self.minPts:
                            toMerge |= set(self.neighbors[j])

                    if not any([j in c for c in self.clusters]):
                        self.points[j].cluster = numCluster
                        self.clusters[-1].add(j)



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
    points = [p.coord() for p in DF]

    plt.scatter(*zip(*points), color=[.75] * 3, alpha=.5, s= 15)

    colors = 'rbgycm' * 1000
    for i, clust in enumerate(scan.clusters):
        core = list(clust)
        plt.scatter(*zip(*[points[i] for i in xrange(len(points)) if i in clust]), color=colors[i], alpha=1, s=15)

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
NE = filterPoints(-80,-65,35,50, Data)

eps = .0001
minPts = 3
scan = DBSCAN(eps, minPts)

scan.addPoints(NE)
scan.solve()

plot(NE)

save(NE, 'NE')

# San Fran
# SF = filterPoints(-125, -119, 35, 40, Data)
#
# eps = .01
# minPts = 3
# scan = DBSCAN(eps, minPts)
#
# scan.addPoints(SF)
# scan.solve()
#
#
# plot(SF)
# save(SF, 'SF')
