# Modules
The represented modules are intended to scrape, convert, and extract datasets about flight history.

## How to use 
Place a module to a folder within your script and load it as a package:
<code> from [module name] import [module name] </code>

## airservice_info 
- Required packages: BeautifulSoup, urllib, pandas 
- The function takes a list of aircraft tail numbers, _e.g. airservice_info(['N101AE', 'N100KB'])_
- The function returns a Pandas Dataframe and a _"airservice_info.cvs"_ file. 
- All information retrieve from https://flightaware.com/

## flight_history 
- Required packages: cookiejar, mechanize, BeautifulSoup, pandas  
- The function takes FlightAware username, password, and list of Aircraft tail numbers, _e.g. flight_history(["username", "password", ['N101AE', 'N100KB'])_
- The function returns a Pandas Dataframe and a _"flight_history.cvs"_ file. 
- All information retrieve from https://flightaware.com/

## utc_converter
- Required packages: pandas, numpy
- The function takes a dataframe with 'departure' and 'arrival' columns, _e.g. utc_converter(dataframe[['departure', 'arrival']])_
- The input DateTime format should be __"%I:%M%p %Z"__, _e.g. 05:44PM CST_.
- The function returns the same dataframe with added UTC time for departure and arrival. 

## metar_decoder
- Required packages: metar
- The function takes a dataframe with 'METAR_origin' and 'METAR_destination' columns, _e.g. utc_converter(dataframe[['METAR_origin', 'METAR_destination']])_
- The input METAR format should be like _"METAR KXWA 202251Z AUTO 26013KT 10SM CLR 04/M07 A2978 RMK AO2 SLP121 T00441072="_.
- The function returns the same dataframe with added METAR decoded information. 

## metar_scraper_origin
- Required packages: os, glob, pandas, BeautifulSoup, urllib
- Function takes a dataframe with columns 'tail_number', 'ICAO_origin', 'date', 'dep_UTC_time', and returns a folder with _csv_ files for each tail number which contains METAR data information. 
- It also returns a concatenated _csv_ file.

## metar_scraper_destination
- Required packages: os, glob, pandas, BeautifulSoup, urllib
- Function takes a dataframe with columns 'tail_number', 'ICAO_destination', 'date', 'arr_UTC_time', and returns a folder with _csv_ files for each tail number which contains METAR data information. 
- It also returns a concatenated _csv_ file.
