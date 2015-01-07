library(ggmap)

# load in data
gps <- read.csv("history-2014.csv", sep = ',', header = TRUE)

# get center for NorthEast data
NElon = mean(gps$lon[gps$lon > -80 && gps$lon < -65 && gps$lat > 35 && gps$lat < 50])
NElat = mean(gps$lat[gps$lon > -80 && gps$lon < -65 && gps$lat > 35 && gps$lat < 50])

# get map
map <- get_map(location=c(lon=NElon, lat=NElat), source = "google", maptype = "roadmap", zoom=6)

# plot with location points
ggmap(map) +
  geom_point(aes(x = lon, y = lat), data = gps,
           alpha = .5, color="darkred", size = 2) +
  theme_nothing()



ggsave(filename=paste('Test', ".png", sep=""), limitesize=FALSE)#height=50, width=40, units="cm", dpi=600)
