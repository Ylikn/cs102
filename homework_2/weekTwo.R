df <- read.csv('db.csv') 
heatmap(cor(df)) 
library(WVPlots) 
ScatterHist(df, "height", "weight")