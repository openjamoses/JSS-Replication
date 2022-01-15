library(ggplot2)
library(forcats)

## Load the csv file...
df<-read.csv("/Volumes/Cisco/Fall2021/quantum-revision/Analysis/RQ2/evolution/csv/Quantum-Chemistry.csv")
head(df)

# Visualization
ggplot(df, aes(x = Snapshots, y = TDR_Smells)) + 
  geom_line(aes(color = Project)) + #, linetype = Project
  ylab('TDR (% percentage)')+
  #xlab('No. snapshots')+
  #scale_y_continuous(labels=scales::percent)+
  scale_y_continuous(labels = function(TDR_Smells) paste0(TDR_Smells, ".0%"))+
  #scale_y_continuous(labels = scales::percent_format(TDR = 1))+
  #scale_color_viridis(discrete = TRUE) +
  #ggtitle("Popularity of American names in the previous 30 years") +
  #theme_ipsum() +
  #theme_bw()+
  theme(axis.title.x = element_blank())+
  theme_bw()+
  theme(plot.background = element_rect(fill = "lightgray"))##BFD5E3
  #theme_wsj()+ scale_colour_wsj("colors6")
  #facet_wrap(~Category, scale="free")
  #theme(legend.position="top")
  #facet_grid(~Type, scale="free")
  
#+ scale_color_manual(values = c("darkred", "steelblue"))


df<-read.csv("/Volumes/Cisco/Fall2021/quantum-revision/Analysis/general/plots/repos_commits_loc_interval_metrics.csv")
head(df)

# grouped boxplot
# make V1 an ordered factor
#df$interval <- factor(df$interval, levels = df$interval)
df$interval<-factor(df$interval, levels = rev(unique(df$interval)))
ggplot(df, aes(x=fct_inorder(interval), y=commits, group=interval)) + 
  geom_boxplot()+
  #theme_bw()+
  ylab('Number of commits')+
  xlab('Time frame (in days)')+
  #theme(axis.title.x = element_blank())+
  #stat_boxplot(fill = NA) +
  #theme_bw()+
  theme(legend.position="top")+
  #scale_x_continuous(limits=df$interval)+
  #theme(axis.title.x = element_blank())+
  #theme(axis.ticks.x = element_blank(),
  #      axis.text.x = element_blank())+
  #theme(axis.text.x = element_text(angle = 45, vjust = 0.5, hjust=1))+
  facet_wrap(~categories, scale="free") # , scale="free"



# grouped boxplot
# make V1 an ordered factor
#df$interval <- factor(df$interval, levels = df$interval)
df$interval<-factor(df$interval, levels = rev(unique(df$interval)))
ggplot(df, aes(x=fct_inorder(interval), y=cloc, group=interval)) + 
  geom_boxplot()+
  #theme_bw()+
  ylab('Number of commits')+
  xlab('Time frame (in days)')+
  #theme(axis.title.x = element_blank())+
  #stat_boxplot(fill = NA) +
  #theme_bw()+
  theme(legend.position="top")+
  #scale_x_continuous(limits=df$interval)+
  #theme(axis.title.x = element_blank())+
  #theme(axis.ticks.x = element_blank(),
  #      axis.text.x = element_blank())+
  #theme(axis.text.x = element_text(angle = 45, vjust = 0.5, hjust=1))+
  facet_wrap(~categories, scale="free") # , scale="free"



## Grouped snapshots CLOC
df<-read.csv("/Volumes/Cisco/Fall2021/quantum-revision/Analysis/bugs/snapshots_loc_2.csv")
head(df)

df2<-read.csv("/Volumes/Cisco/Fall2021/quantum-revision/Analysis/bugs/snapshots_cum_loc_2.csv")
head(df2)
# grouped boxplot
# make V1 an ordered factor
#df$interval <- factor(df$interval, levels = df$interval)
df$snapshot<-factor(df$snapshot, levels = rev(unique(df$snapshot)))
ggplot(df, aes(x=fct_inorder(snapshot), y=CLOC, group=snapshot)) + 
  geom_boxplot()+
  geom_line(data=df2, aes(x = snapshot, y = Cumulative_CLOC), color = "red") +
  scale_y_continuous("TDR", sec.axis = sec_axis(~ . Cumulative_CLOC, name = "CLOC")) +
  #theme_bw()+
  ylab('Thousands lines of code (CLOC)')+
  xlab('The first ten snapshots basing on 90 days interval')+
  #theme(axis.title.x = element_blank())+
  #stat_boxplot(fill = NA) +
  #theme_bw()+
  theme(legend.position="top")+
  #scale_x_continuous(limits=df$interval)+
  #theme(axis.title.x = element_blank())+
  #theme(axis.ticks.x = element_blank(),
  #      axis.text.x = element_blank())+
  #theme(axis.text.x = element_text(angle = 45, vjust = 0.5, hjust=1))+
  facet_wrap(~Category, scale="free") # , scale="free"



### Test boxplot and line plot
df$snapshot<-factor(df$snapshot, levels = rev(unique(df$snapshot)))
ggplot() + 
  geom_boxplot(data = df, aes(fill=snapshot, group=snapshot, x=snapshot, y=CLOC))+
  #geom_bar(data = df2, aes(fill=Category, x=snapshot, y=Median_CLOC/1000), position="stack", stat="identity") +
  geom_point(data = df2, aes(x=snapshot, y=Cumulative_CLOC/1000), size = 1, color = 'black') +
  geom_line(data = df2, aes(x=snapshot, y=Cumulative_CLOC/1000, lty = 'Percent Incorrect'), color = 'black', group = 1, na.rm = TRUE) +
  scale_fill_manual(values = c("Correct" = "#00C1AA", "Incorrect" = "#FF6666")) +
  #scale_linetype('') +
  scale_y_continuous("TDR", sec.axis = sec_axis(~ . Cumulative_CLOC/1000, name = "KLOC")) +
  #scale_y_continuous(name = 'Count',
  #                   #breaks = seq(0,250,25),
  #                   sec.axis = sec_axis(~./2, name = 'CLOC', breaks = seq(0,105,15))) +
  #labs(title = 'Logistic Regression Model Predicting on 2019',        subtitle = 'Prediction Performance by Current Days Not Flown Period',
  #     x = 'Current Days Not Flown',
  #     fill = '')+
  facet_wrap(~Category, scale="free") # , scale="free"




ggplot() + 
  geom_bar(data = df2, aes(fill=Category, x=snapshot, y=Median_CLOC/1000), position="stack", stat="identity") +
  geom_point(data = df2, aes(x=snapshot, y=Cumulative_CLOC/1000), size = 1, color = 'black') +
  geom_line(data = df2, aes(x=snapshot, y=Cumulative_CLOC/1000, lty = 'Percent Incorrect'), color = 'black', group = 1, na.rm = TRUE) +
  scale_fill_manual(values = c("Correct" = "#00C1AA", "Incorrect" = "#FF6666")) +
  #scale_linetype('') +
  scale_y_continuous(name = 'Count',
                     #breaks = seq(0,250,25),
                     sec.axis = sec_axis(~./2, name = 'Percent Incorrect', breaks = seq(0,105,15))) +
  labs(title = 'Logistic Regression Model Predicting on 2019',        subtitle = 'Prediction Performance by Current Days Not Flown Period',
       x = 'Current Days Not Flown',
       fill = '')+
  facet_wrap(~Category, scale="free") # , scale="free"

df<-read.csv("/Volumes/Cisco/Fall2021/quantum-revision/Analysis/bugs/snapshots_loc2.csv")
head(df)
# Visualization
ggplot(df, aes(x = snapshot, y = CLOC)) + 
  geom_line(aes(color = ProjectId)) + #, linetype = Project
  ylab('TDR (% percentage)')+
  #xlab('No. snapshots')+
  #scale_y_continuous(labels=scales::percent)+
  #scale_y_continuous(labels = function(CLOC) paste0(CLOC, ".0%"))+
  #scale_y_continuous(labels = scales::percent_format(TDR = 1))+
  #scale_color_viridis(discrete = TRUE) +
  #ggtitle("Popularity of American names in the previous 30 years") +
  #theme_ipsum() +
  #theme_bw()+
  theme(axis.title.x = element_blank())+
  theme_bw()+
  theme(plot.background = element_rect(fill = "lightgray")) +##BFD5E3
#theme_wsj()+ scale_colour_wsj("colors6")
facet_wrap(~Category, scale="free")
#theme(legend.position="top")
#facet_grid(~Type, scale="free")






df<-read.csv("/Volumes/Cisco/Fall2021/quantum-revision/Analysis/general/plots/projects_age_distribution.csv")
head(df)
# grouped boxplot
ggplot(df, aes(x=Category, y=Age, group=Category)) + 
  geom_boxplot()+
  #theme_bw()+
  ylab('Project\'s Age (days)')+
  #xlab('Training Number')+
  #theme(axis.title.x = element_blank())+
  #stat_boxplot(fill = NA) +
  theme_bw()+
  #theme(legend.position="top")+
  theme(axis.title.x = element_blank())+
  #theme(axis.ticks.x = element_blank(),
  #      axis.text.x = element_blank())
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))
  #facet_wrap(~Topic, scale="free") # , scale="free"


# Build the boxplot. In the 'fill' argument, give this column
ggplot( df,aes(x=Category, y=Age, fill=Category, alpha=Category)) + 
  geom_boxplot() +
  #scale_fill_manual(values=c("#69b3a2", "grey")) +
  #scale_alpha_manual(values=c(1,0.1)) +
  #theme_ipsum() +
  theme(legend.position = "none") +
  xlab("")



### Evolution

df_severity<-read.csv("/Volumes/Cisco/Fall2021/quantum-revision/Analysis/RQ2/overral/issues_severity_evolution.csv")
head(df_severity)
df_severity2<-read.csv("/Volumes/Cisco/Fall2021/quantum-revision/Analysis/RQ2/overral/issues_severity_evolution2.csv")
head(df_types)
# Area plot
ggplot(df_severity, aes(x = snapshot, y = TDR)) + 
  geom_area(aes(color = Severity, fill = Severity), 
            alpha = 0.4, position = position_dodge(0.8)) +
  geom_point(data = df_severity, aes(x=snapshot, y=KLOC/10), size = 0.3, color = 'black') +
  geom_line(data = df_severity, aes(x=snapshot, y=KLOC/10), color = 'black', size = 0.1, group = 1, na.rm = TRUE) +
  theme_bw()+
  ylab('TDR (%)')+
  scale_color_manual(values = c("red", 'steelblue', 'seagreen', 'wheat4'),name="Severity") +
  scale_fill_manual(values = c("red", 'steelblue', 'seagreen', 'wheat4'), name="Severity")+
  #scale_color_manual(values = c("#E7B800", "#00AFBB", "red"), name="Debt (mainline)") +
  #scale_fill_manual(values = c( "#E7B800","#00AFBB", "red"), name="Debt (mainline)")+
  #scale_y_continuous(sec.axis = sec_axis(trans=trans, name='KLOC'))+
  #scale_y_continuous(labels = scales::percent_format())+
  scale_y_continuous(sec.axis = sec_axis(~.*1, name = 'KLOC', labels = function(xx) { paste0(xx*100, "")})) +
  theme(
    axis.line.y.right = element_line(color = "black"), 
    axis.ticks.y.right = element_line(color = "black"),
    axis.text.y.right = element_text(color = "black"), 
    axis.title.y.right = element_text(color = "black"),
    #axis.line.y.left = element_line(color = "grey"), 
    #axis.ticks.y.left = element_line(color = "grey"),
    #axis.text.y.left = element_text(color = "grey"), 
    #axis.title.y.left = element_text(color = "grey")
  )+
  theme(axis.title.x = element_blank())+
  labs(subtitle = "Technical Debt by severity per snapshot",
       caption = "snapshots")+
  #theme(legend.position="top")+
  #scale_color_manual(values = c("#00AFBB", "#E7B800", "#E90800")) +
  #scale_fill_manual(values = c("#00AFBB", "#E7B800", "#E90800"))+
  facet_wrap(~Category, scale="free") # , scale="free"
#ggsave(paste(plot_variants, "types-variant.pdf"))






df_severity<-read.csv("/Volumes/Cisco/Fall2021/quantum-revision/Analysis/RQ2/overral/issues_severity_evolution.csv")
head(df_severity)
df_severity2<-read.csv("/Volumes/Cisco/Fall2021/quantum-revision/Analysis/RQ2/overral/issues_severity_evolution2.csv")
head(df_types)
df_debt<-read.csv("/Volumes/Cisco/Fall2021/quantum-revision/Analysis/RQ2/overral/issues_types_evolution.csv")
head(df_types)
ggplot(df_debt, aes(x = snapshot, y = TDR)) + 
  geom_area(aes(color = Debt, fill = Debt), 
            alpha = 0.4, position = position_dodge(0.8)) +
  geom_point(data = df_debt, aes(x=snapshot, y=KLOC), size = 0.3, color = 'black') +
  geom_line(data = df_debt, aes(x=snapshot, y=KLOC), color = 'black', size = 0.1, group = 1, na.rm = TRUE) +
  theme_bw()+
  ylab('TDR (%)')+
  #scale_fill_discrete(name="Debt (mainline)")+
  scale_color_manual(values = c("#E7B800", "#00AFBB", "red"), name="Debt (mainline)") +
  scale_fill_manual(values = c( "#E7B800","#00AFBB", "red"), name="Debt (mainline)")+
  #scale_y_continuous(sec.axis = sec_axis(trans=trans, name='KLOC'))+
  #scale_y_continuous(labels = scales::percent_format())+
  scale_y_continuous(sec.axis = sec_axis(~.*1, name = 'KLOC', labels = function(xx) { paste0(xx*10, "")})) +
  theme(
    axis.line.y.right = element_line(color = "black"), 
    axis.ticks.y.right = element_line(color = "black"),
    axis.text.y.right = element_text(color = "black"), 
    axis.title.y.right = element_text(color = "black"),
    #axis.line.y.left = element_line(color = "grey"), 
    #axis.ticks.y.left = element_line(color = "grey"),
    #axis.text.y.left = element_text(color = "grey"), 
    #axis.title.y.left = element_text(color = "grey")
  )+
  theme(axis.title.x = element_blank())+
  labs(subtitle = "Technical Debt by types in mainline per snapshot",
       caption = "mainline snapshots")+
  #theme(legend.position="top")+
  #scale_color_manual(values = c("#00AFBB", "#E7B800", "#E90800")) +
  #scale_fill_manual(values = c("#00AFBB", "#E7B800", "#E90800"))+
  facet_wrap(~Category, scale="free") # , scale="free"
#ggsave(paste(plot_variants, "types-variant.pdf"))


# Area plot
ggplot(df_debt, aes(x = snapshot, y = TDR)) + 
  geom_area(aes(color = Debt, fill = Debt), 
            alpha = 0.4, position = position_dodge(0.8)) +
  geom_point(data = df_debt, aes(x=snapshot, y=KLOC/10), size = 0.3, color = 'black') +
  geom_line(data = df_debt, aes(x=snapshot, y=KLOC/10), color = 'black', size = 0.1, group = 1, na.rm = TRUE) +
  theme_bw()+
  ylab('TDR (%)')+
  scale_color_manual(values = c("red", 'steelblue', 'seagreen', 'wheat4'),name="Severity") +
  scale_fill_manual(values = c("red", 'steelblue', 'seagreen', 'wheat4'), name="Severity")+
  #scale_color_manual(values = c("#E7B800", "#00AFBB", "red"), name="Debt (mainline)") +
  #scale_fill_manual(values = c( "#E7B800","#00AFBB", "red"), name="Debt (mainline)")+
  #scale_y_continuous(sec.axis = sec_axis(trans=trans, name='KLOC'))+
  #scale_y_continuous(labels = scales::percent_format())+
  scale_y_continuous(sec.axis = sec_axis(~.*1, name = 'KLOC', labels = function(xx) { paste0(xx*100, "")})) +
  theme(
    axis.line.y.right = element_line(color = "black"), 
    axis.ticks.y.right = element_line(color = "black"),
    axis.text.y.right = element_text(color = "black"), 
    axis.title.y.right = element_text(color = "black"),
    #axis.line.y.left = element_line(color = "grey"), 
    #axis.ticks.y.left = element_line(color = "grey"),
    #axis.text.y.left = element_text(color = "grey"), 
    #axis.title.y.left = element_text(color = "grey")
  )+
  theme(axis.title.x = element_blank())+
  labs(subtitle = "Technical Debt by severity per snapshot",
       caption = "snapshots")+
  #theme(legend.position="top")+
  #scale_color_manual(values = c("#00AFBB", "#E7B800", "#E90800")) +
  #scale_fill_manual(values = c("#00AFBB", "#E7B800", "#E90800"))+
  facet_wrap(~Category, scale="free") # , scale="free"
#ggsave(paste(plot_variants, "types-variant.pdf"))








p2 <- ggplot(df_severity2, aes(x = snapshot, y = TDR)) + 
  geom_area(aes(color = df_severity2, fill = Severity), 
            alpha = 0.4, position = position_dodge(0.8)) +
  geom_point(data = df_severity2, aes(x=snapshot, y=KLOC), size = 0.3, color = 'black') +
  geom_line(data = df_severity2, aes(x=snapshot, y=KLOC), color = 'black', size = 0.1, group = 1, na.rm = TRUE) +
  #theme_bw()+
  ylab('TDR (%)')+
  #scale_fill_discrete(name="Severity (variant)")+
  scale_color_manual(values = c("red", 'steelblue', 'seagreen', 'wheat4'),name="Severity (variant)") +
  scale_fill_manual(values = c("red", 'steelblue', 'seagreen', 'wheat4'), name="Severity (variant)")+
  
  #scale_y_continuous(sec.axis = sec_axis(trans=trans, name='KLOC'))+
  #scale_y_continuous(labels = scales::percent_format())+
  scale_y_continuous(sec.axis = sec_axis(~.*1, name = 'KLOC', labels = function(xx) { paste0(xx*10, "")})) +
  theme(
    axis.line.y.right = element_line(color = "black"), 
    axis.ticks.y.right = element_line(color = "black"),
    axis.text.y.right = element_text(color = "black"), 
    axis.title.y.right = element_text(color = "black"),
    #axis.line.y.left = element_line(color = "grey"), 
    #axis.ticks.y.left = element_line(color = "grey"),
    #axis.text.y.left = element_text(color = "grey"), 
    #axis.title.y.left = element_text(color = "grey")
  )+
  #theme(axis.title.x = element_blank())+
  theme_bw()+
  theme(plot.background = element_rect(fill = "lightgray"))+ ##BFD5E3
  #theme(legend.position="top")+
  #theme(legend.text ="Severity (variant)")+
  #scale_fill_discrete(name="Debt (variant)")+
  theme(axis.title.x = element_blank())+
  labs(subtitle = "Technical Debt by severity in variants per snapshot",
       caption = "variant snapshots")+
  #theme(axis.ticks.x = element_blank(),
  #      axis.text.x = element_blank())+
  #scale_color_manual(values = c("#00AFBB", "#E7B800", "#E90800")) +
  #scale_fill_manual(values = c("#00AFBB", "#E7B800", "#E90800"))+
  facet_wrap(~Category, scale="free") # , scale="free"
#ggsave(paste(plot_variants, "types-variant.pdf"))
grid.arrange(p1, p2)

