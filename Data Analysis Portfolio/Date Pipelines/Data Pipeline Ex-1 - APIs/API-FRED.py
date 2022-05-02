import pandas as pd
import json 
import matplotlib.pyplot as plt
import requests

with open('API-FRED-KEY.json', 'r') as f:
    secrets = json.load(f)
api_key = secrets[0]["api_key"]

class FredPy:
    def __init__(self, token=None):
        self.token = token
        self.url = "https://api.stlouisfed.org/fred/series/observations" + \
                    "?series_id={seriesID}&api_key={key}&file_type=json" + \
                    "&observation_start={start}&observation_end={end}&units={units}"

    def set_token(self, token):
        self.token = token 

    def get_series(self, seriesID, start, end, units):
        url_formatted = self.url.format(seriesID=seriesID, start=start, end=end, units=units, key=self.token)

        response = requests.get(url_formatted)
        if(self.token):
            if (response.status_code == 200):
                data = pd.DataFrame(response.json()['observations'])[['date','value']]\
                    .assign(date = lambda cols: pd.to_datetime(cols['date']))\
                    .assign(value = lambda cols: cols['value'].astype(float))\
                    .rename(columns= {'value': seriesID}) 
                return data
            else:
                raise Exception("Bad response from API, status code = {}".format(response.status_code))
        else:
            raise Exception("You did not specify an API Key.")

fredpy = FredPy() #instantiate the fredpy object

fredpy.set_token(api_key)#Set the API Key

data = fredpy.get_series(seriesID = 'GDP', start='2005-01-01', end='2021-12-31', units = 'pc1') #Test getting the GDP series

print(data)


     