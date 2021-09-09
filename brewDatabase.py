import sqlite3
import pandas as pd
import time
import requests
import json


# Create the connection/ cursor
con = sqlite3.connect('beerData.db')
cur = con.cursor()


# For the final page, allow the user to either select another location or go to home screen
def selection():
    from homePages import breweryPage, homePage
    print("\033[0;36;49mSelect another location? y/n")
    nextPage = input('')
    if nextPage == 'y':
        breweryPage()
    elif nextPage == 'n':
        homePage()
    else:
        print("Invalid input. Please try again.")
        time.sleep(1)
        selection()


# Load in the api, return as a dataframe
def loadData(url):
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
        dataDict = json.loads(content)
        data = pd.DataFrame(dataDict)
    else:
        print("Error loading file.")
    return data


# Wrangle the data, return as dataframe
def organizeData(city, state):
    city = city.lower()
    rawData = loadData('https://api.openbrewerydb.org/breweries?by_city=' + city)
    if rawData.empty:
        print("That place doesn't exist!")
        time.sleep(1)
        selection()
    else:
        dropColumns = rawData.drop(columns=['id','obdb_id', 'address_2', 'address_3', 'county_province','country', 'longitude', 'latitude', 'updated_at', 'created_at'])
        byState = dropColumns[dropColumns['state'] == state]
        noRepeats = byState.drop_duplicates(subset=['street'])
        return noRepeats
    
    
def brewLocator(city, state):
    # Set up sql table
    data = organizeData(city, state)
    brewTable = data.to_sql('brewTable', con, if_exists='replace',index=True)
    brewList = cur.execute('SELECT * FROM brewTable').fetchall()

    # Return nicely organized table with brewery info
    locations = pd.DataFrame.from_records(data=brewList, columns=['id', 'name', 'brewery_type', 'street', 'city','state','zipcode', 'phone', 'website'])
    print("\033[0;33;49mBreweries Near You:")
    print(locations) 
    time.sleep(1)
    selection()
    
 
    





