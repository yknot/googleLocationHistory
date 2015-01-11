plotMap <- function(df, coord, z, filename){
  
  # get map
  map <- get_map(location=coord, source = "google", maptype = "roadmap", zoom=z)
  
  # plot with location points
  ggmap(map) +
    geom_point(aes(x = lon, y = lat), data = df,
               alpha = .5, color="darkred", size = 1) +
    theme_nothing()
  
  
  ggsave(filename=paste(filename, ".png", sep=""))#, limitesize=FALSE)
  
}