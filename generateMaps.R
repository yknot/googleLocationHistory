library(ggmap)
source("plotMap.R")





# load in data
if (!exists("gps"))
  gps <- read.csv("history-2014.csv", sep = ',', header = TRUE)

# get center for NorthEast data
NElon = mean(gps$lon[gps$lon > -80 && gps$lon < -65 && gps$lat > 35 && gps$lat < 50])
NElat = mean(gps$lat[gps$lon > -80 && gps$lon < -65 && gps$lat > 35 && gps$lat < 50])

NEcoord = c(NElon, NElat)

z = 6


plotMap(gps[gps$lon > -80 && gps$lon < -65 && gps$lat > 35 && gps$lat < 50], NEcoord, z, 'Northeast')


