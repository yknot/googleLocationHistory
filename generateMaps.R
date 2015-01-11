library(ggmap)
source("plotMap.R")


# load in data
if (!exists("gps"))
  gps <- read.csv("history-2014.csv", sep = ',', header = TRUE)


####################### graphs
# Northeast zoomed out
NLon = mean(gps$lon[gps$lon > -80 && gps$lon < -65 && gps$lat > 35 && gps$lat < 50])
NLat = mean(gps$lat[gps$lon > -80 && gps$lon < -65 && gps$lat > 35 && gps$lat < 50])

northeastCoord = c(NLon, NLat)
plotMap(gps,northeastCoord, 6, 'raws/Northeast')


# NewYork zoomed in
newyorkCoord = c(-73.989496, 40.7317825)
plotMap(gps, newyorkCoord, 13, 'raws/NewYork')

# Upstate zoomed in
upstateCoord = c(-73.9730261, 42.922505)
plotMap(gps, upstateCoord, 9, 'raws/Upstate')


# colorado
coloradoCoord = c(-105.4334507, 39.5589435)
plotMap(gps, coloradoCoord, 9, 'raws/Colorado')

# st martin
stMartinCoord = c(-63.070718, 18.0607718)
plotMap(gps, stMartinCoord , 12, 'raws/StMartin')

# SF zoomed out
sanfranCoord = c(-122.2280528, 37.6410506)
plotMap(gps, sanfranCoord, 10, 'raws/SanFrancisco')

# SF zoomed in
sanfranCoordZoom = c(-122.4470414, 37.7686922)
plotMap(gps, sanfranCoordZoom, 12, 'raws/SanFranciscoZoom')




############################## annotated 
# Annotated Northeast
              # Oneonta,    Hanover,    Providence,     Devens,     Wildwood,     Scotia
ultimateLon = c(-75.0661099, -72.1908299, -71.4211681, -74.8176785, -71.6191505, -73.9606454)
ultimateLat = c( 42.4564004,   43.714773,  41.8169925,  38.9878335,  42.5475304,  42.837002)

ultimate = data.frame(ultimateLon, ultimateLat)

            #  killington, mt. washington
skiingLon = c(-72.7855623, -71.3055278)
skiingLat = c(43.6542525, 44.2710252)

skiing = data.frame(skiingLon, skiingLat)


hikingLon = c(-74.1309855)
hikingLat = c(44.0822724)

hiking = data.frame(hikingLon, hikingLat)


# get Northeast map
map <- get_map(location=northeastCoord, source = "google", maptype = "roadmap", zoom=6)

ggmap(map) +
  geom_point(aes(x = lon, y = lat), data = gps,
             alpha = .5, color="darkred", size = 1) +
  geom_point(aes(x = ultimateLon, y = ultimateLat), data = ultimate,
             alpha = 1, color="darkblue", size = 4) +
  geom_point(aes(x = skiingLon, y = skiingLat), data = skiing,
             alpha = 1, color="darkgreen", size = 4) +
  geom_point(aes(x = hikingLon, y = hikingLat), data = hiking,
             alpha = 1, color="yellow", size = 4) +
  theme_nothing()


ggsave(filename=paste('raws/Northeast_annotated', ".png", sep=""))#, limitesize=FALSE)


