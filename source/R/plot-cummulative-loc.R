library(ggplot2)
library(dplyr)
library(scales)

df<-read.csv("/Volumes/Cisco/Fall2021/quantum-revision/Analysis/bugs/snapshots_loc_2.csv")
head(df)

df2<-read.csv("/Volumes/Cisco/Fall2021/quantum-revision/Analysis/bugs/snapshots_cum_loc_2.csv")
head(df2)
# Now filter out the Patch that we don't want
data_df <- filter(df, Category != "Simulator")
head(data_df)

data_df2 <- filter(df2, Category != "Simulator")
head(data_df2)

#data_df$snapshot<-factor(data_df$snapshot, levels = rev(unique(data_df$snapshot)))
df$snapshot<-factor(df$snapshot, levels = unique(df$snapshot))
df2$snapshot<-factor(df2$snapshot, levels = unique(df2$snapshot))

scientific_10 <- function(x) {
  parse(text=gsub("e", " %*% 10^", scales::scientific_format()(x)))
}
ggplot() + 
  geom_boxplot(data = df, aes(group=snapshot, group=snapshot, x=snapshot, y=CLOC))+
  geom_point(data = df2, aes(x=snapshot, y=Cumulative_CLOC), size = 1, color = 'steelblue') +
  geom_line(data = df2, aes(x=snapshot, y=Cumulative_CLOC, lty = 'changed lines of code'), color = 'grey', group = 1, na.rm = TRUE) +
  ylab('Changed lines of code (cloc)')+
  scale_y_continuous(sec.axis = sec_axis(~., name = 'cumulative of average changed lines of code')) +
  theme(axis.text.y.right=element_blank(),
         axis.ticks.y.right=element_blank(),
         axis.title.x=element_blank(),
         axis.title.y.right = element_text(color = "steelblue")
  ) +
  #theme(legend.position="top")+
  theme(legend.position = "none")+
  facet_wrap(~Category, scale="free") # , scale="free"
