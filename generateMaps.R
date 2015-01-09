library(ggmap)
source("plotMap.R")





# load in data
if (!exists("gps"))
  gps <- read.csv("history-2014.csv", sep = ',', header = TRUE)


# Northeast zoomed out
NLon = mean(gps$lon[gps$lon > -80 && gps$lon < -65 && gps$lat > 35 && gps$lat < 50])
NLat = mean(gps$lat[gps$lon > -80 && gps$lon < -65 && gps$lat > 35 && gps$lat < 50])

northeastCoord = c(NLon, NLat)
plotMap(gps,northeastCoord, 6, 'Northeast')

# NewYork zoomed in
newyorkCoord = c(-73.989496, 40.7317825)
plotMap(gps, newyorkCoord, 13, 'NewYork')

# Upstate zoomed in
upstateCoord = c(-73.9730261, 42.922505)
plotMap(gps, upstateCoord, 9, 'Upstate')



# colorado
coloradoCoord = c(-105.4334507, 39.5589435)
plotMap(gps, coloradoCoord, 9, 'Colorado')

# st martin
stMartinCoord = c(-63.070718, 18.0607718)
plotMap(gps, stMartinCoord , 12, 'StMartin')


# SF zoomed out
sanfranCoord = c(-122.2280528, 37.6410506)
plotMap(gps, sanfranCoord, 10, 'SanFrancisco')

# SF zoomed in
sanfranCoordZoom = c(-122.4470414, 37.7686922)
plotMap(gps, sanfranCoordZoom, 12, 'SanFranciscoZoom')

