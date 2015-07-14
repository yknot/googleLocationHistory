library(ggmap)
source("plotMap.R")

library(ggplot2)

SF <- read.csv("~/Dropbox/projects/googleLocationHistory/SF.csv")

f <- ggplot(SF, aes(lon, lat))
f + geom_point(color = SF$cluster)





# SF zoomed out
sanfranCoord = c(-122.2280528, 37.6410506)
plotMap(SF, sanfranCoord, 10, 'raws/SanFrancisco')
