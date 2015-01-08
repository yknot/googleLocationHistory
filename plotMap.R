plotMap <- function(df, coord, z, filename){
  
  # get Northeast map
  map <- get_map(location=coord, source = "google", maptype = "roadmap", zoom=z)
  
  # plot Northeast with location points
  ggmap(map) +
    geom_point(aes(x = lon, y = lat), data = df,
               alpha = .5, color="darkred", size = 2) +
    theme_nothing()
  
  
  ggsave(filename=paste(filename, ".png", sep=""))#, limitesize=FALSE)
  
}