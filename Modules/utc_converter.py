# # ===========================================================================
# #                            UTC time zone converter
# # ===========================================================================
# # The function takes a dataframe with 'departure' and 'arrival' columns. 
# # The input DateTime format should be "%I:%M%p %Z", e.g. 05:44PM CST.
# # The functions returns the same dataframe with added UTC time. 

def utc_converter(dataset):
    # import packages
    import pandas as pd
    import numpy as np
    
    data  = dataset.loc[:,['departure', 'arrival']]
    
    # split time zone and assign to new variable for departure
    data.loc[:,'dep_time_zone'] = data.departure.str.split(" ", n = 1, expand = True)[1]
    
    # remove time zome from departure
    data.departure = data.departure.str.split(" ", n = 1, expand = True)[0]
    
    # split time zone and assign to new variable for arrival
    data.loc[:,'arr_time_zone'] = data.arrival.str.split(" ", n = 1, expand = True)[1].str.split(" ", n = 1, expand = True)[0]
    
    # remove time zome from arrival
    data.arrival = data.arrival.str.split(" ", n = 1, expand = True)[0]
    
    # convert departure time to datetime format
    data.departure = pd.to_datetime(data.departure, format='%I:%M%p', errors='coerce')
    
    # convert arrival time to datetime format
    data.arrival = pd.to_datetime(data.arrival, format='%I:%M%p', errors='coerce')
    data.loc[data.arrival.notnull(), 'arrival'] = data.loc[data.arrival.notnull(), 'arrival']
    
    utc = pd.read_csv('https://gist.githubusercontent.com/alyssaq/f1f0ec50e79f1c089554d0de855dd09c/raw/ca2f858a1149a20aa9c7507e826eae5636e7cecd/timezone-abbreviations.csv')
    
    utc['direction'] = np.where(utc[' UTC offset'].str.contains("+", regex=False), "+", "-")
    utc[' UTC offset'] = utc[' UTC offset'].str.replace('+', '').str.replace('-', '')
    
    utc.loc[utc[' UTC offset'].str.contains('/'), ' UTC offset'] = utc.loc[utc[' UTC offset'].str.contains('/'), 
                                                                           ' UTC offset'].str.split(" / ", n=1, expand=True)[0]
    
    utc.loc[~utc[' UTC offset'].str.contains(':'), ' UTC offset'] = pd.to_datetime(utc.loc[~utc[' UTC offset'].str.contains(':'), ' UTC offset'], 
                                                                                   format=' %H', errors='coerce')
    
    utc.loc[utc[' UTC offset'].str.contains(':', na=False), ' UTC offset'] = pd.to_datetime(utc.loc[utc[' UTC offset'].str\
                                                                            .contains(':', na=False), ' UTC offset'], format = ' %H:%M', errors='coerce')
    
    utc[' UTC offset'] = pd.to_datetime(utc[' UTC offset'])
    utc = utc.drop([2, 5, 22], axis=0)
    utc = utc.drop_duplicates(subset=['Abbreviation.'])
    
    # merge with departure key 
    data = data.merge(utc.add_suffix("_dep"), how='left', left_on='dep_time_zone', right_on='Abbreviation._dep')
    
    # add to the local time offset hours
    data['dep_UTC_hour'] = np.where(data.direction_dep == '-', data.departure.dt.hour + data[' UTC offset_dep'].dt.hour, 
                                    data.departure.dt.hour - data[' UTC offset_dep'].dt.hour)
    
    # add to the local time offset minutes
    data['dep_UTC_min'] = np.where(data.direction_dep == '-', data.departure.dt.minute + data[' UTC offset_dep'].dt.minute, 
                                    data.departure.dt.minute - data[' UTC offset_dep'].dt.minute)
    
    # if minutes > 59 then add 1 hour
    data['dep_UTC_hour'] = np.where(data['dep_UTC_min'] > 59, data['dep_UTC_hour'] + 1, data['dep_UTC_hour'])
    
    # if minutes >59 subtract 60 minutes
    data['dep_UTC_min'] = np.where(data['dep_UTC_min'] > 59, data['dep_UTC_min'] - 60, data['dep_UTC_min'])
    
    # if hour > 23 subtract 24 hours
    data['dep_UTC_hour'] = np.where(data['dep_UTC_hour'] > 23, data['dep_UTC_hour'] - 24, data['dep_UTC_hour'])
    
    # conver hours to string
    data.loc[data.dep_UTC_hour.notnull(), 'dep_UTC_hour'] = data.loc[data.dep_UTC_hour.notnull(), 'dep_UTC_hour'].astype(int).astype(str)
    
    # conver minutes to string
    data.loc[data.dep_UTC_min.notnull(), 'dep_UTC_min'] = data.loc[data.dep_UTC_min.notnull(), 'dep_UTC_min'].astype(int)
    data.loc[data.dep_UTC_min < 10, 'dep_UTC_min'] = "0" + data.loc[data.dep_UTC_min < 10, 'dep_UTC_min'].astype(int).astype(str)
    
    # concat hours and minutes and convert to datetime
    data['dep_UTC_time'] = data.dep_UTC_hour.astype(str) + ":" + data.dep_UTC_min.astype(str)
    data['dep_UTC_time'] = pd.to_datetime(data['dep_UTC_time'], errors='coerce').dt.time
    
    # drop duplicated rows
    data = data.drop(data.columns[-7:-1], axis=1)
    
    # merge with arrival key
    data = data.merge(utc.add_suffix("_arr"), how='left', left_on='arr_time_zone', right_on='Abbreviation._arr')
    
    # add to the local time offset hours
    data['arr_UTC_hour'] = np.where(data.direction_arr == '-', data.arrival.dt.hour + data[' UTC offset_arr'].dt.hour, 
                                    data.arrival.dt.hour - data[' UTC offset_arr'].dt.hour)
    
    # add to the local time offset minutes
    data['arr_UTC_min'] = np.where(data.direction_arr == '-', data.arrival.dt.minute + data[' UTC offset_arr'].dt.minute, 
                                    data.arrival.dt.minute - data[' UTC offset_arr'].dt.minute)
    
    # if minutes > 59 then add 1 hour
    data['arr_UTC_hour'] = np.where(data['arr_UTC_min'] > 59, data['arr_UTC_hour'] + 1, data['arr_UTC_hour'])
    
    # if minutes >59 subtract 60 minutes
    data['arr_UTC_min'] = np.where(data['arr_UTC_min'] > 59, data['arr_UTC_min'] - 60, data['arr_UTC_min'])
    
    # if hour > 23 subtract 24 hours
    data['arr_UTC_hour'] = np.where(data['arr_UTC_hour'] > 23, data['arr_UTC_hour'] - 24, data['arr_UTC_hour'])
    
    # conver hours to string
    data.loc[data.arr_UTC_hour.notnull(), 'arr_UTC_hour'] = data.loc[data.arr_UTC_hour.notnull(), 'arr_UTC_hour'].astype(int).astype(str)
    data.loc[data.arr_UTC_min.notnull(), 'arr_UTC_min'] = data.loc[data.arr_UTC_min.notnull(), 'arr_UTC_min'].astype(int)
    
    # conver minutes to string
    data.loc[data.arr_UTC_min < 10, 'arr_UTC_min'] = "0" + data.loc[data.arr_UTC_min < 10, 'arr_UTC_min'].astype(int).astype(str)
    
    # concat hours and minutes and convert to datetime
    data['arr_UTC_time'] = data.arr_UTC_hour.astype(str) + ":" + data.arr_UTC_min.astype(str)
    data['arr_UTC_time'] = pd.to_datetime(data['arr_UTC_time'], errors='coerce').dt.time
    
    # drop duplicated rows
    data = data.drop(data.columns[-7:-1], axis=1)
    
    # join UTC time to dataset
    dataset = dataset.loc[:,:'departure'].join([data.loc[:,'dep_UTC_time'], dataset.loc[:,'arrival'],
                                           data.loc[:,'arr_UTC_time'], dataset.loc[:,'duration':]])
      
    return(dataset)