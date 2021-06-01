### Datasets
The folder contains provided by stakeholders, scraped, and transformed for several analysis datasets. The folder has also datasets with information about airports, COVID-19 cases, and populations that were used in the analysis.

### Scripts  
1. _FW_airports_merging:_ merging process of the airport information using several approaches. Different combinations of information about airport codes, airport name, city, and state were used as a primary key for joining. The outcome is a joined information about the airport code, city, state, and country for each record. 
2. _FW METAR data merging:_ merging process of the meteorological data (METAR) to the dataset with airport information using airport code, date, and time as a merging key. 
3. _FW_anomaly:_ Outlier classification(Yes/No) of duration and distance of flights based on the boxplot approach. 
4. _FW_ARIMA:_ building of an ARIMA model to predict the number of flights for each day.
5. _FW Tracker:_ creating a dataset for the tracking system in a Tableau.
6. _FW_IHC:_ subsetting and cleaning the dataset which contains information only about the "Intermountain Healthcare" service. Flights analysis of the "Intermountain Healthcare."  
7. _ILS and LPVorPV/Airport Analysis:_ Merging of additional airport information for the "ILS" and "LPV or PV" aviation systems analysis. Hypothesis testing of "ILS" and "LPV or PV" systems.
8. _FW cluster analysis:_ K-means cluster analysis of the flights.

### Tableau DB
The folder contains created dashboards in a Tableau Desktop. The dashboards represent exploratory data analysis. 

### images
The folder contains all created and used images in analysis, presentation, and report. 
