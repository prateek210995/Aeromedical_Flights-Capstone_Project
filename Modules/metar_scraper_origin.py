# =============================================================================
#                     METAR data scraping for Origin
# =============================================================================
# Function takes a dataframe with columns 'tail_number','ICAO_origin', 
# 'date', 'dep_UTC_time', and returns a folder with csv files for each tail 
# number which contains METAR data information. It also returns a concatenated 
# csv file.
  
def metar_scraper_origin(dataset):
    # import packages
    import os
    import glob
    import pandas as pd
    from bs4 import BeautifulSoup as soup
    from urllib.request import urlopen as uReq
# =============================================================================
#                 METAR data merging preparation for Origin
# =============================================================================
    # pick necessary variables
    data = dataset.loc[:,['tail_number','ICAO_origin', 'date', 'dep_UTC_time']]
    
    # convert to datetime
    data.date = pd.to_datetime(data.date)
    
    # drop null values
    data = data.dropna()
    
    # sort by tail number 
    data = data.sort_values('tail_number').reset_index(drop=True)

# =============================================================================
#                       METAR data scraping for Origin
# =============================================================================
    # create containers
    tail_number = []
    ICAO_origin = []
    date = []
    METAR = []
    
    for j in range(0,len(data)-1):
        url = "http://www.ogimet.com/display_metars2.php?lang=en&lugar=" + data.ICAO_origin.iloc[j] \
          + "&tipo=ALL&ord=REV&nil=SI&fmt=html&ano=" + str(data.date.dt.year.iloc[j]) \
          + "&mes=" + str(data.date.dt.month.iloc[j]) + "&day=" + str(data.date.dt.day.iloc[j]) \
          +"&hora=" + str(pd.to_datetime(data.dep_UTC_time, format='%H:%M:%S').dt.hour.iloc[j]) + "&anof=" + str(data.date.dt.year.iloc[j]) \
          + "&mesf="+ str(data.date.dt.month.iloc[j]) + "&dayf=" + str(data.date.dt.day.iloc[j]) \
        + "&horaf=" + str(pd.to_datetime(data.dep_UTC_time, format='%H:%M:%S').dt.hour.iloc[j] + 1) + "&minf=59&send=send"
    
        # BeautifulSoup Magic
        uClient = uReq(url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, 'html.parser')
        
        if data.tail_number.iloc[j] == data.tail_number.iloc[j+1]:
            for i in range(len(page_soup.findAll("tr", {"bgcolor":["#F0F0D0",'white']}))):
                tail_number += [data.tail_number.iloc[j]]
                ICAO_origin += [data.ICAO_origin.iloc[j]]
                date += [page_soup.findAll("tr", {"bgcolor":["#F0F0D0",'white']})[i].findAll('td')[1].text.replace('->','')]
                METAR += [page_soup.findAll("tr", {"bgcolor":["#F0F0D0",'white']})[i].findAll('td')[2].text.replace('\n          ', '')]
        
        if j == len(data)-2 and data.tail_number.iloc[j] == data.tail_number.iloc[j+1]:
            url = "http://www.ogimet.com/display_metars2.php?lang=en&lugar=" + data.ICAO_origin.iloc[-1] \
              + "&tipo=ALL&ord=REV&nil=SI&fmt=html&ano=" + str(data.date.dt.year.iloc[-1]) \
              + "&mes=" + str(data.date.dt.month.iloc[-1]) + "&day=" + str(data.date.dt.day.iloc[-1]) \
              +"&hora=" + str(pd.to_datetime(data.dep_UTC_time, format='%H:%M:%S').dt.hour.iloc[-1]) + "&anof=" + str(data.date.dt.year.iloc[-1]) \
              + "&mesf="+ str(data.date.dt.month.iloc[-1]) + "&dayf=" + str(data.date.dt.day.iloc[-1]) \
              + "&horaf=" + str(pd.to_datetime(data.dep_UTC_time, format='%H:%M:%S').dt.hour.iloc[-1] + 1) + "&minf=59&send=send"
            
            # BeautifulSoup Magic
            uClient = uReq(url)
            page_html = uClient.read()
            uClient.close()
            page_soup = soup(page_html, 'html.parser')
            
            for i in range(len(page_soup.findAll("tr", {"bgcolor":["#F0F0D0",'white']}))):
                tail_number += [data.tail_number.iloc[-1]]
                ICAO_origin += [data.ICAO_origin.iloc[-1]]
                date += [page_soup.findAll("tr", {"bgcolor":["#F0F0D0",'white']})[i].findAll('td')[1].text.replace('->','')]
                METAR += [page_soup.findAll("tr", {"bgcolor":["#F0F0D0",'white']})[i].findAll('td')[2].text.replace('\n          ', '')]
            
            # export as csv
            pd.DataFrame(list(zip(tail_number, ICAO_origin, date, METAR)), columns= ['tail_number', 'ICAO_origin', 'date', 'METAR'])\
            .to_csv(os.getcwd() + '/origin/' + data.tail_number.iloc[-1] + '.csv', index=False) 
            
        if data.tail_number.iloc[j] != data.tail_number.iloc[j+1] and j != len(data)-2:
            for i in range(len(page_soup.findAll("tr", {"bgcolor":["#F0F0D0",'white']}))):
                tail_number += [data.tail_number.iloc[j]]
                ICAO_origin += [data.ICAO_origin.iloc[j]]
                date += [page_soup.findAll("tr", {"bgcolor":["#F0F0D0",'white']})[i].findAll('td')[1].text.replace('->','')]
                METAR += [page_soup.findAll("tr", {"bgcolor":["#F0F0D0",'white']})[i].findAll('td')[2].text.replace('\n          ', '')]

            # export as csv             
            df = pd.DataFrame(list(zip(tail_number, ICAO_origin, date, METAR)), columns= ['tail_number', 'ICAO_origin', 'date', 'METAR'])
            outname = data.tail_number.iloc[j] + '.csv'
            outdir = './origin'
            if not os.path.exists(outdir):
                os.mkdir(outdir)    
            fullname = os.path.join(outdir, outname)    
            df.to_csv(fullname, index=False)
            
            tail_number = []
            ICAO_origin = []
            date = []
            METAR = []
            
# =============================================================================
#                            concat all files
# =============================================================================
    all_filenames = [i for i in glob.glob(os.getcwd() + '/origin/' + '*.{}'.format('csv'))]
    
    #combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
    
    #export to csv
    combined_csv.to_csv(os.getcwd() + '/origin/' + "METAR_origin.csv", index=False, encoding='utf-8-sig')
