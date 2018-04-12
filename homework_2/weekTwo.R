df <- read.csv('db.csv') 
heatmap(cor(df)) 
library(WVPlots) 
ScatterHist(df, "height", "weight")
df <- read.csv('D:/homework_2/mlbootcamp5_train.csv')

heatmap(cor(df))

library(WVPlots)
ScatterHist(df, "height", "weight", "title")

library(ggplot2)

ggplot(df, aes(x='df$gender', y=df$weight)) + 
  geom_violin(aes(fill=factor(df$gender)))

df$age_years = round(df$age / 365)

df_not_cardio = subset(df,df$cardio == 0)

df_cardio = subset(df,df$cardio == 1)

library(reshape2)
new_df <- df[, c('gender','cholesterol','gluc','smoke','alco','active','cardio')]
df_melt <- melt(new_df)

ggplot(df,aes(df$age_years,fill=factor(df$cardio))) + 
  geom_histogram(binwidth = 1, position = "dodge")

barplot(cor(new_df))

ggplot(new_df,aes(mac_df,fill=factor(new_df))) + 
  geom_bar(position = "dodge")

ggplot(df, aes(df$height, fill = factor(df$gender))) + 
  geom_density(alpha = 0.4)
