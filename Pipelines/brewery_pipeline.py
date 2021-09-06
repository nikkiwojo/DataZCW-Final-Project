import pandas as pd
import requests
import json

# Load in the data using an API
def loadData(url):
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
        dataDict = json.loads(content)
        data = pd.DataFrame(dataDict)
    else:
        print("Error loading file.")
    return data


# Load in the brewery specific data and filter out unneccessary information
def breweryLocation(url, city, state):
    city = city.lower()
    rawData = loadData('https://api.openbrewerydb.org/breweries?by_city=' + city)
    dropColumns = rawData.drop(columns=['obdb_id', 'address_2', 'address_3', 'county_province','country', 'longitude', 'latitude', 'updated_at', 'created_at'])
    byState = dropColumns[dropColumns['state'] == state]
    finalData = byState.drop_duplicates(subset=['street'])
    return finalData

