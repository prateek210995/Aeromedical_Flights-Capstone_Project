library(tidyverse)
library(ggplot2)

setwd("~/OneDrive - George Mason University/GMU/Spring 2021/DAEN_690/FW/Datasets/NEW")
fw_ihc = read.csv('FW_ihc.csv')

str(fw_ihc)
fw_ihc$weekends = factor(fw_ihc$weekends)
fw_ihc$day_name = factor(fw_ihc$day_name)

### duration
ggplot(data = fw_ihc, aes(x = duration_min, fill = tail_number)) + 
  geom_density(aes(alpha=0.8)) +
  labs(title = 'Histogram of duration in minutes by tail number',
       x = 'Duration (min)')

# is it correlated? (yes)
wilcox.test(duration_min ~ tail_number, fw_ihc)

# departure
ggplot(data = fw_ihc, aes(x = duration_min, fill = departure_shift)) + 
  geom_density(aes(alpha=0.8)) +
  labs(title = 'Histogram of duration in minutes by departure shift',
       x = 'Duration (min)')

# is it correlated? (no)
wilcox.test(duration_min ~ departure_shift, fw_ihc)

# arrival
ggplot(data = fw_ihc, aes(x = duration_min, fill = arrival_shift)) + 
  geom_density(aes(alpha=0.8)) +
  labs(title = 'Histogram of duration in minutes by arrival shift',
       x = 'Duration (min)')

# is it correlated? (no)
wilcox.test(duration_min ~ arrival_shift, fw_ihc)

# day name
ggplot(data = fw_ihc, aes(x = duration_min, fill = weekends)) + 
  geom_density(aes(alpha=0.8))  +
  labs(title = 'Histogram of duration in minutes by weekends (Yes-1/No-0)',
       x = 'Duration (min)')

# is it correlated? (no)
wilcox.test(duration_min ~ weekends, fw_ihc)

# day name
ggplot(data = fw_ihc, aes(x = duration_min, fill = day_name)) + 
  geom_density(aes(alpha=0.8))  +
  labs(title = 'Histogram of duration in minutes by week day',
       x = 'Duration (min)')

# is it correlated? (no)
kruskal.test(duration_min ~ day_name, fw_ihc)


## distance
ggplot(data = fw_ihc, aes(x = distance_mi, fill = tail_number)) + 
  geom_density(aes(alpha=0.8)) +
  labs(title = 'Histogram of distance in miles by tail number',
       x = 'Distance (miles)')

# is it correlated? (yes)
wilcox.test(distance_mi ~ tail_number, fw_ihc)

# departure
ggplot(data = fw_ihc, aes(x = distance_mi, fill = departure_shift)) + 
  geom_density(aes(alpha=0.8)) +
  labs(title = 'Histogram of distance in miles by departure shift',
       x = 'Distance (miles)')

# is it correlated? (no)
wilcox.test(distance_mi ~ departure_shift, fw_ihc)

# arrival_shift
ggplot(data = fw_ihc, aes(x = distance_mi, fill = arrival_shift)) + 
  geom_density(aes(alpha=0.8)) +
  labs(title = 'Histogram of distance in miles by arrival shift',
       x = 'Distance (miles)')

# is it correlated?  (no)
wilcox.test(distance_mi ~ arrival_shift, fw_ihc)

# day name
ggplot(data = fw_ihc, aes(x = distance_mi, fill = weekends)) + 
  geom_density(aes(alpha=0.8)) +
  labs(title = 'Histogram of distance in miles by weekends (Yes-1/No-0)',
       x = 'Distance (miles)')

# is it correlated? (No) 
wilcox.test(distance_mi ~ weekends, fw_ihc)

ggplot(data = fw_ihc, aes(x = distance_mi, fill = day_name)) + 
  geom_density(aes(alpha=0.8)) +
  labs(title = 'Histogram of distance in miles by week day',
       x = 'Distance (miles)')

# is it correlated? (No)
kruskal.test(distance_mi ~ day_name, fw_ihc)
