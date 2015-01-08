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

# colorado
coloradoCoord = c(-105.4334507, 39.5589435)
plotMap(gps, coloradoCoord, 9, 'Colorado')

# st martin
stMartinCoord = c(-63.070718, 18.0607718)
plotMap(gps, stMartinCoord , 12, 'StMartin')


# SF zoomed out
sanfranCoord = c(-122.2280528, 37.6410506)
plotMap(gps, sanfranCoord, 10, 'SanFrancisco')

