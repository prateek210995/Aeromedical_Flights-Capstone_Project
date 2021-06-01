### Datasets
The folder contains provided by stakeholders, scraped, and transformed for several analysis datasets. The folder has also datasets with information about airports that were used in the analysis.

### Scripts  
1. _RW_airports_merging:_ merging process of the airport information using several approaches. Different combinations of information about airport codes, airport name, city, and state were used as a primary key for joining. The outcome is a joined information about the airport code, city, state, and country for each record. 
2. _RW METAR data merging:_ merging process of the meteorological data (METAR) to the dataset with airport information using airport code, date, and time as a merging key. 
3. _RW_anomaly:_ Outlier classification(Yes/No) of duration and distance of flights based on the boxplot approach. 
4. _RW_ARIMA:_ building of an ARIMA model to predict the number of flights for each day.
5. _RW Tracker:_ creating a dataset for the tracking system in a Tableau.
6. _RW_IHC:_ subsetting and cleaning the dataset which contains information only about the "Intermountain Healthcare" service. Flights analysis of the "Intermountain Healthcare."  

### Tableau DB
The folder contains created dashboards in a Tableau Desktop. The dashboards represent exploratory data analysis. 

### images
The folder contains all created and used images in analysis, presentation, and report. 
