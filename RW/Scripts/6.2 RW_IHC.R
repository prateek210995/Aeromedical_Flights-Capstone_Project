library(ggplot2)
library(tidyverse)

setwd("~/OneDrive - George Mason University/GMU/Spring 2021/DAEN_690/RW/Datasets/NEW")
rw_ihc = read.csv('RW_ihc.csv')

str(rw_ihc)
rw_ihc$weekends = factor(rw_ihc$weekends)
rw_ihc$day_name = factor(rw_ihc$day_name)

### duration
ggplot(data = rw_ihc, aes(x = duration, fill = tail_number)) + 
  geom_density(aes(alpha=0.8)) +
  labs(title = 'Histogram of duration in minutes by tail number',
       x = 'Duration (min)')

# is it correlated? (yes)
kruskal.test(duration ~ tail_number, rw_ihc)

rw_ihc %>% group_by(tail_number) %>%
  summarise(count = n(),
            min_duration = min(duration),
            avg_duration = mean(duration),
            median_duration = median(duration),
            max_duration = max(duration),
            sd_duration = sd(duration))

# departure
ggplot(data = rw_ihc, aes(x = duration, fill = departure_shift)) + 
  geom_density(aes(alpha=0.8)) +
  labs(title = 'Histogram of duration in minutes by departure shift',
       x = 'Duration (min)')

# is it correlated? (no) 
wilcox.test(duration ~ departure_shift, rw_ihc)

# arrival
ggplot(data = rw_ihc, aes(x = duration, fill = arrival_shift)) + 
  geom_density(aes(alpha=0.8)) +
  labs(title = 'Histogram of duration in minutes by arrival shift',
       x = 'Duration (min)')

# is it correlated? (yes)
wilcox.test(duration ~ arrival_shift, rw_ihc)

rw_ihc %>% group_by(arrival_shift) %>%
  summarise(count = n(),
            min_duration = min(duration),
            avg_duration = mean(duration),
            median_duration = median(duration),
            max_duration = max(duration),
            sd_duration = sd(duration))

# day name
ggplot(data = rw_ihc, aes(x = duration, fill = weekends)) + 
  geom_density(aes(alpha=0.8))   +
  labs(title = 'Histogram of duration in minutes by weekends (Yes-1/No-0)',
       x = 'Duration (min)')

ggplot(data = rw_ihc, aes(x = duration, fill = day_name)) + 
  geom_density(aes(alpha=0.8))   +
  labs(title = 'Histogram of duration in minutes by week day',
       x = 'Duration (min)')

# is it correlated? (no)
wilcox.test(duration ~ weekends, rw_ihc)

# is it correlated? (no)
kruskal.test(duration ~ day_name, rw_ihc)

## distance
ggplot(data = rw_ihc, aes(x = distance_mi, fill = tail_number)) + 
  geom_density(aes(alpha=0.8)) +
  labs(title = 'Histogram of distance in miles by tail number',
       x = 'Distance (miles)')

# is it correlated? (no)
kruskal.test(distance_mi ~ tail_number, rw_ihc)

# departure
ggplot(data = rw_ihc, aes(x = distance_mi, fill = departure_shift)) + 
  geom_density(aes(alpha=0.8)) +
  labs(title = 'Histogram of distance in miles by departure shift',
       x = 'Distance (miles)')

# is it correlated? (no)
wilcox.test(distance_mi ~ departure_shift, rw_ihc)

# arrival_shift
ggplot(data = rw_ihc, aes(x = distance_mi, fill = arrival_shift)) + 
  geom_density(aes(alpha=0.8)) +
  labs(title = 'Histogram of distance in miles by arrival shift',
       x = 'Distance (miles)')

# is it correlated? (no)
wilcox.test(distance_mi ~ arrival_shift, rw_ihc)

# day name
ggplot(data = rw_ihc, aes(x = distance_mi, fill = weekends)) + 
  geom_density(aes(alpha=0.8)) +
  labs(title = 'Histogram of distance in miles by weekends (Yes-1/No-0)',
       x = 'Distance (miles)')

# is it correlated? (no)
wilcox.test(distance_mi ~ weekends, rw_ihc)
ggplot(data = rw_ihc, aes(x = distance_mi, fill = day_name)) + 
  geom_density(aes(alpha=0.8)) +
  labs(title = 'Histogram of distance in miles by week day',
       x = 'Distance (miles)')

# is it correlated? (no)
kruskal.test(distance_mi ~ day_name, rw_ihc)
