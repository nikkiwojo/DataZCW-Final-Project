import sqlite3
import pandas as pd
from homePages import beerPage, homePage
import time


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
    if choice == '1':
        sql = 'SELECT name, style, abv FROM beerTable WHERE style IN ({seq}) ORDER BY RANDOM() LIMIT 5'.format(seq=','.join(['?']*len(fruit)))
        fruitList = cur.execute(sql, fruit).fetchall()
        recs = pd.DataFrame.from_records(data=fruitList, columns=['Name','Style','ABV'])
        print("\033[0;33;49mTry one of these!:")
        print(recs) 
        time.sleep(3)
        crisp()
    elif choice == '2':
        sql = 'SELECT name, style, abv FROM beerTable WHERE style IN ({seq}) ORDER BY RANDOM() LIMIT 5'.format(seq=','.join(['?']*len(malt)))
        maltList = cur.execute(sql, malt).fetchall()
        recs = pd.DataFrame.from_records(data=maltList, columns=['Name','Style','ABV'])
        print("\033[0;33;49mTry one of these!:")
        print(recs) 
        time.sleep(3)
        crisp()
    elif choice == '3':
        sql = 'SELECT name, style, abv FROM beerTable WHERE style IN ({seq}) ORDER BY RANDOM() LIMIT 5'.format(seq=','.join(['?']*len(hop)))
        hopList = cur.execute(sql, hop).fetchall()
        recs = pd.DataFrame.from_records(data=hopList, columns=['Name','Style','ABV'])
        print("\033[0;33;49mTry one of these!:")
        print(recs) 
        time.sleep(3)
        crisp()
    elif choice == 'b':
        beerPage()


def hoppy():
    beerTable = beerDatabase()

    earth = ('English Bitter', 'American Double / Imperial IPA', 'Belgian IPA','English Pale Ale', 'American IPA', 'American White IPA','Belgian Strong Pale Ale', 'Belgian Pale Ale', 'English India Pale Ale (IPA)')
    malt = ('Braggot', 'Mead', 'California Common / Steam Beer', "American Amber / Red Lager", 'American Barleywine')

    print("\033[1;35;49m----------------------------")
    print("--- \U0001F37A \033[1;37;49m Hoppy & Bitter \U0001F37A \033[1;35;49m---")
    print("----------------------------")
    print("\033[0;32;49mClick 'b' to choose a different flavor profile")
    print("\033[0;36;49mWhat are you in the mood for?")
    print("1) Earthy & Dry \n2) Malt-Forward")

    choice = input('')
    if choice == '1':
        sql = 'SELECT name, style, abv FROM beerTable WHERE style IN ({seq}) ORDER BY RANDOM() LIMIT 5'.format(seq=','.join(['?']*len(earth)))
        earthList = cur.execute(sql, earth).fetchall()
        recs = pd.DataFrame.from_records(data=earthList, columns=['Name','Style','ABV'])
        print("\033[0;33;49mTry one of these!:")
        print(recs) 
        time.sleep(3)
        hoppy()
    elif choice == '2':
        sql = 'SELECT name, style, abv FROM beerTable WHERE style IN ({seq}) ORDER BY RANDOM() LIMIT 5'.format(seq=','.join(['?']*len(malt)))
        maltList = cur.execute(sql, malt).fetchall()
        recs = pd.DataFrame.from_records(data=maltList, columns=['Name','Style','ABV'])
        print("\033[0;33;49mTry one of these!:")
        print(recs) 
        time.sleep(3)
        hoppy()
    elif choice == 'b':
        beerPage()


def malty():
    beerTable = beerDatabase()

    toasty = ('Euro Dark Lager','English Brown Ale')
    fruity = ('Biere de Garde', 'Scotch Ale / Wee Heavy', 'Scottish Ale', 'English Barleywine','Irish Red Ale', 'Tripel', 'Extra Special / Strong Bitter (ESB)')

    print("\033[1;35;49m----------------------------")
    print("--- \U0001F37A \033[1;37;49m Malty & Sweet \U0001F37A \033[1;35;49m---")
    print("----------------------------")
    print("\033[0;32;49mClick 'b' to choose a different flavor profile")
    print("\033[0;36;49mWhat are you in the mood for?")
    print("1) Toasty & Nutty \n2) Fruit & Toffee/Caramel")

    choice = input('')
    if choice == '1':
        sql = 'SELECT name, style, abv FROM beerTable WHERE style IN ({seq}) ORDER BY RANDOM() LIMIT 5'.format(seq=','.join(['?']*len(toasty)))
        toastList = cur.execute(sql, toasty).fetchall()
        recs = pd.DataFrame.from_records(data=toastList, columns=['Name','Style','ABV'])
        print("\033[0;33;49mTry one of these!:")
        print(recs) 
        time.sleep(3)
        malty()
    elif choice == '2':
        sql = 'SELECT name, style, abv FROM beerTable WHERE style IN ({seq}) ORDER BY RANDOM() LIMIT 5'.format(seq=','.join(['?']*len(fruity)))
        fruitList = cur.execute(sql, fruity).fetchall()
        recs = pd.DataFrame.from_records(data=fruitList, columns=['Name','Style','ABV'])
        print("\033[0;33;49mTry one of these!:")
        print(recs) 
        time.sleep(3)
        malty()
    elif choice == 'b':
        beerPage()


def dark():
    beerTable = beerDatabase()

    soft = ('Milk / Sweet Stout', 'Foreign / Export Stout', 'Schwarzbier', 'Baltic Porter', 'Oatmeal Stout', 'American Porter', 'American Pale Ale (APA)', 'American Brown Ale', ' English Stout','Winter Warmer', 'Dubbel')
    dry = ('American Black Ale', 'American Stout', 'Russian Imperial Stout', 'American Double / Imperial Stout', 'Irish Dry Stout', 'American Double / Imperial Stout')

    print("\033[1;35;49m----------------------------")
    print("--- \U0001F37A \033[1;37;49m Dark & Roasty \U0001F37A \033[1;35;49m---")
    print("----------------------------")
    print("\033[0;32;49mClick 'b' to choose a different flavor profile")
    print("\033[0;36;49mWhat are you in the mood for?")
    print("1) Soft & Silky/Malty \n2) Dark & Dry")

    choice = input('')
    if choice == '1':
        sql = 'SELECT name, style, abv FROM beerTable WHERE style IN ({seq}) ORDER BY RANDOM() LIMIT 5'.format(seq=','.join(['?']*len(soft)))
        softList = cur.execute(sql, soft).fetchall()
        recs = pd.DataFrame.from_records(data=softList, columns=['Name','Style','ABV'])
        print("\033[0;33;49mTry one of these!:")
        print(recs) 
        time.sleep(3)
        dark()
    elif choice == '2':
        sql = 'SELECT name, style, abv FROM beerTable WHERE style IN ({seq}) ORDER BY RANDOM() LIMIT 5'.format(seq=','.join(['?']*len(dry)))
        dryList = cur.execute(sql, dry).fetchall()
        recs = pd.DataFrame.from_records(data=dryList, columns=['Name','Style','ABV'])
        print("\033[0;33;49mTry one of these!:")
        print(recs) 
        time.sleep(3)
        dark()
    elif choice == 'b':
        beerPage()


def smoke():
    beerTable = beerDatabase()

    smolder = tuple('Smoked Beer')
    meaty = tuple('Rauchbier')

    print("\033[1;35;49m----------------------------")
    print("--- \U0001F37A \033[1;37;49m Smokey \U0001F37A \033[1;35;49m---")
    print("----------------------------")
    print("\033[0;32;49mClick 'b' to choose a different flavor profile")
    print("\033[0;36;49mWhat are you in the mood for?")
    print("1) Subdued Smolder \n2) Spicy & Meaty")

    choice = input('')
    if choice == '1':
        sql = 'SELECT name, style, abv FROM beerTable WHERE style IN ({seq}) ORDER BY RANDOM() LIMIT 5'.format(seq=','.join(['?']*len(smolder)))
        smolderList = cur.execute(sql, smolder).fetchall()
        recs = pd.DataFrame.from_records(data=smolderList, columns=['Name','Style','ABV'])
        print("\033[0;33;49mTry one of these!:")
        print(recs) 
        time.sleep(3)
        smoke()
    elif choice == '2':
        sql = 'SELECT name, style, abv FROM beerTable WHERE style IN ({seq}) ORDER BY RANDOM() LIMIT 5'.format(seq=','.join(['?']*len(meaty)))
        dryList = cur.execute(sql, meaty).fetchall()
        recs = pd.DataFrame.from_records(data=meatyList, columns=['Name','Style','ABV'])
        print("\033[0;33;49mTry one of these!:")
        print(recs) 
        time.sleep(3)
        smoke()
    elif choice == 'b':
        beerPage()


def fruity():
    beerTable = beerDatabase()

    bright = ('Saison / Farmhouse Ale', 'Roggenbier', 'Hefeweizen','American Pale Wheat Ale','Herbed / Spiced Beer', 'English Pale Mild Ale',  'Kristalweizen', 'Witbier','Pumpkin Ale', 'Belgian Blonde Ale', 'Tripel')
    dark = ('Quadrupel (Quad)', 'Dunkelweizen', 'American Dark Wheat Ale', 'Rye Beer', 'Belgian Strong Dark Ale','English Dark Mild Ale', 'Dubbel')

    print("\033[1;35;49m----------------------------")
    print("--- \U0001F37A \033[1;37;49m Fruit & Spice \U0001F37A \033[1;35;49m---")
    print("----------------------------")
    print("\033[0;32;49mClick 'b' to choose a different flavor profile")
    print("\033[0;36;49mWhat are you in the mood for?")
    print("1) Bright & Yeasty \n2) Dark")

    choice = input('')
    if choice == '1':
        sql = 'SELECT name, style, abv FROM beerTable WHERE style IN ({seq}) ORDER BY RANDOM() LIMIT 5'.format(seq=','.join(['?']*len(bright)))
        brightList = cur.execute(sql, bright).fetchall()
        recs = pd.DataFrame.from_records(data=brightList, columns=['Name','Style','ABV'])
        print("\033[0;33;49mTry one of these!:")
        print(recs) 
        time.sleep(3)
        fruity()
    elif choice == '2':
        sql = 'SELECT name, style, abv FROM beerTable WHERE style IN ({seq}) ORDER BY RANDOM() LIMIT 5'.format(seq=','.join(['?']*len(dark)))
        darkList = cur.execute(sql, dark).fetchall()
        recs = pd.DataFrame.from_records(data=darkList, columns=['Name','Style','ABV'])
        print("\033[0;33;49mTry one of these!:")
        print(recs) 
        time.sleep(3)
        fruity()
    elif choice == 'b':
        beerPage()


def sour():
    beerTable = beerDatabase()

    delicate = ('Gose','Berliner Weissbier')
    fruity = ('Flanders Red Ale','Flanders Oud Bruin','Fruit / Vegetable Beer')
    earthy = tuple('American Wild Ale')

    print("\033[1;35;49m----------------------------")
    print("--- \U0001F37A \033[1;37;49m Sour, Tart, & Funky \U0001F37A \033[1;35;49m---")
    print("----------------------------")
    print("\033[0;32;49mClick 'b' to choose a different flavor profile")
    print("\033[0;36;49mWhat are you in the mood for?")
    print("1) Delicate \n2) Fruity & Vinous \n3) Earthy")

    choice = input('')
    if choice == '1':
        sql = 'SELECT name, style, abv FROM beerTable WHERE style IN ({seq}) ORDER BY RANDOM() LIMIT 5'.format(seq=','.join(['?']*len(delicate)))
        delicateList = cur.execute(sql, delicate).fetchall()
        recs = pd.DataFrame.from_records(data=delicateList, columns=['Name','Style','ABV'])
        print("\033[0;33;49mTry one of these!:")
        print(recs) 
        time.sleep(3)
        sour()
    elif choice == '2':
        sql = 'SELECT name, style, abv FROM beerTable WHERE style IN ({seq}) ORDER BY RANDOM() LIMIT 5'.format(seq=','.join(['?']*len(fruity)))
        fruityList = cur.execute(sql, fruity).fetchall()
        recs = pd.DataFrame.from_records(data=fruityList, columns=['Name','Style','ABV'])
        print("\033[0;33;49mTry one of these!:")
        print(recs) 
        time.sleep(3)
        sour()
    elif choice == '3':
        sql = 'SELECT name, style, abv FROM beerTable WHERE style IN ({seq}) ORDER BY RANDOM() LIMIT 5'.format(seq=','.join(['?']*len(earthy)))
        earthyList = cur.execute(sql, earthy).fetchall()
        recs = pd.DataFrame.from_records(data=earthyList, columns=['Name','Style','ABV'])
        print("\033[0;33;49mTry one of these!:")
        print(recs) 
        time.sleep(3)
        sour()
    elif choice == 'b':
        beerPage()