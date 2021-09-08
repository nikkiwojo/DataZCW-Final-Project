import sqlite3
import pandas as pd
from homePages import beerPage


# Create the connection/ cursor
con = sqlite3.connect('beerData.db')
cur = con.cursor()


def beerDatabase():
    # Read csv file, organize the data
    rawData = pd.read_csv('beers.csv')
    dropData = rawData.drop(columns=['ibu', 'ounces','brewery_id'])
    filterData = dropData.iloc[:, 1:]
    beers = pd.DataFrame(filterData)

    # Translate dataframe to sql table
    beerTable = beers.to_sql('beerTable', con, if_exists='replace',index=True)
    
    return beerTable
    

def crisp():
    beerTable = beerDatabase()

    fruit = ('Cream Ale', 'American Blonde Ale', 'Shandy', 'Czech Pilsener', 'American Pilsner', 'German Pilsener', 'American India Pale Lager', 'Kolsch', 'Wheat Ale','Cider', 'Grissette')
    malt = ('Marzen / Oktoberfest', 'American Adjunct Lager', 'Light Lager', 'Maibock / Helles Bock', 'Munich Dunkel Lager', 'Dortmunder / Export Lager', 'Altbier', 'Vienna Lager', 'Munich Helles Lager', 'Bock','Doppelbock','Old Ale','American Amber / Red Lager', 'Radler', 'American Amber / Red Ale')
    hop = ('Keller Bier / Zwickel Bier','Euro Pale Lager','American India Pale Lager', 'American Double / Imperial Pilsener', 'American Pale Lager')

    print("\033[1;35;49m----------------------------")
    print("--- \U0001F37A \033[1;37;49m Crisp & Clean \U0001F37A \033[1;35;49m---")
    print("----------------------------")
    print("\033[0;32;49mClick 'b' to choose a different flavor profile")
    print("\033[0;36;49mWhat are you in the mood for?")
    print("1) Clean/Delicate Fruit \n2) Malt-Accented \n3) Brisk Hop")

    choice = input('')
    if choice == 'b':
        beerPage()
    elif choice == '1':
       beerList = cur.execute('''SELECT * FROM beerTable ORDER BY RANDOM() LIMIT 5''').fetchall()
       
    
    

crisp()

