# # ===========================================================================
#                   Aircraft Registration Information    
# # ===========================================================================
# # The function takes a list of aircraft tail numbers.
# # The function returns a Pandas Dataframe and a cvs file. 
# # All information retrieve from https://flightaware.com/

def airservice_info(tails):
    # load packages
    from bs4 import BeautifulSoup as soup
    from urllib.request import urlopen as uReq
    import pandas as pd
    
    # create containers
    tail_number = []
    Summary = []
    Owner = []
    Airworthiness_Class = []
    Serial_Number = []
    Engine = []
    Weight = []
    Speed = []
    Mode_S_Code = []
    Status = []
    Certificate_Issue_Date = []
    Airworthiness_Date = []
    Last_Action_Date = []
    Expiration = []
    Registry_Source = []
    
    # loop a list of tail numbers and scrape information
    for t in tails:
        url = 'https://flightaware.com/resources/registration/' + t
        uClient = uReq(url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, 'html.parser')
        table = page_soup.findAll("div", {"class":"medium-3 columns"})
        
        if len(table) != 0: 
            tail_number += [t]
            Summary += [table[0].text.replace('\n', '').replace('\t', '')]
            Owner += [table[1].text.replace('\n', '').replace('\t', '')]
            Airworthiness_Class += [table[2].text]
            Serial_Number += [table[3].text]
            Engine += [table[4].text.replace(' ', '')]
            Weight += [table[5].text]
            Speed += [table[6].text]
            Mode_S_Code += [table[7].text]
            Status += [table[8].text]
            Certificate_Issue_Date += [table[9].text]
            Airworthiness_Date += [table[10].text]
            Last_Action_Date += [table[11].text]
            Expiration += [table[12].text]
            Registry_Source += [table[13].text] 
        else:
            tail_number += [t]
            Summary += [None]
            Owner += [None]
            Airworthiness_Class += [None]
            Serial_Number += [None]
            Engine += [None]
            Weight += [None]
            Speed += [None]
            Mode_S_Code += [None]
            Status += [None]
            Certificate_Issue_Date += [None]
            Airworthiness_Date += [None]
            Last_Action_Date += [None]
            Expiration += [None]
            Registry_Source += [None]
    
    # concatenate containers to the Pandas DataFrame
    services_data = pd.DataFrame(list(zip(tail_number,Summary,Owner,Airworthiness_Class,Serial_Number,Engine,Weight,Speed,Mode_S_Code,Status,
                      Certificate_Issue_Date,Airworthiness_Date,Last_Action_Date,Expiration,Registry_Source)),
            columns=['tail_number','Summary','Owner','Airworthiness_Class','Serial_Number','Engine','Weight', 
                     'Speed','Mode_S_Code','Status','Certificate_Issue_Date','Airworthiness_Date', 'Last_Action_Date',
                    'Expiration','Registry_Source'])
        
    # export data as csv file
    services_data.to_csv('airservice_info.csv', index=False)
    
    # return Pandas DataFrame
    return(services_data)