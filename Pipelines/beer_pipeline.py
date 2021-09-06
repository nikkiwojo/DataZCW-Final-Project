import pandas as pd 

# Load in the raw data and filter out unneccessary columns
def loadData(file):
    rawData = pd.read_csv(file)
    filterData = rawData.drop(columns=['ibu', 'ounces','brewery_id'])
    filterData = filterData.iloc[:, 1:]
    return filterData


# Separating the data into flavor profiles, and creating smaller subsets per flavor subset
def crisp(file, flavor):
    bigData = loadData(file)
    fruit = ('Cream Ale', 'American Blonde Ale', 'Shandy', 'Czech Pilsener', 'American Pilsner', 'German Pilsener', 'American India Pale Lager', 'Kolsch', 'Wheat Ale','Cider', 'Grissette')
    malt = ('Marzen / Oktoberfest', 'American Adjunct Lager', 'Light Lager', 'Maibock / Helles Bock', 'Munich Dunkel Lager', 'Dortmunder / Export Lager', 'Altbier', 'Vienna Lager', 'Munich Helles Lager', 'Bock','Doppelbock','Old Ale','American Amber / Red Lager', 'Radler', 'American Amber / Red Ale')
    hop = ('Keller Bier / Zwickel Bier','Euro Pale Lager','American India Pale Lager', 'American Double / Imperial Pilsener', 'American Pale Lager')

    if flavor == 'fruit':
        beerList = pd.DataFrame(bigData[bigData['style'].isin(fruit)])
    elif flavor == 'malt':
        beerList = pd.DataFrame(bigData[bigData['style'].isin(malt)])
    elif flavor == 'hop':
        beerList = pd.DataFrame(bigData[bigData['style'].isin(hop)])
    
    return beerList.sample(n=5)


def hoppy(file, flavor):
    bigData = loadData(file)
    earth = ('English Bitter', 'American Double / Imperial IPA', 'Belgian IPA','English Pale Ale', 'American IPA', 'American White IPA','Belgian Strong Pale Ale', 'Belgian Pale Ale', 'English India Pale Ale (IPA)')
    malt = ('Braggot', 'Mead', 'California Common / Steam Beer', "American Amber / Red Lager", 'American Barleywine')

    if flavor == 'earth':
        beerList = pd.DataFrame(bigData[bigData['style'].isin(earth)])
    elif flavor == 'malt':
        beerList = pd.DataFrame(bigData[bigData['style'].isin(malt)])
    
    return beerList.sample(n=5)


def malty(file, flavor):
    bigData = loadData(file)
    toasty = ('Euro Dark Lager','English Brown Ale')
    fruity = ('Biere de Garde', 'Scotch Ale / Wee Heavy', 'Scottish Ale', 'English Barleywine','Irish Red Ale', 'Tripel', 'Extra Special / Strong Bitter (ESB)')

    if flavor == 'toasty':
        beerList = pd.DataFrame(bigData[bigData['style'].isin(toasty)])
    elif flavor == 'fruity':
        beerList = pd.DataFrame(bigData[bigData['style'].isin(fruity)])
    
    return beerList.sample(n=5)


def dark(file, flavor):
    bigData = loadData(file)
    soft = ('Milk / Sweet Stout', 'Foreign / Export Stout', 'Schwarzbier', 'Baltic Porter', 'Oatmeal Stout', 'American Porter', 'American Pale Ale (APA)', 'American Brown Ale', ' English Stout','Winter Warmer', 'Dubbel')
    dry = ('American Black Ale', 'American Stout', 'Russian Imperial Stout', 'American Double / Imperial Stout', 'Irish Dry Stout', 'American Double / Imperial Stout')

    if flavor == 'soft':
        beerList = pd.DataFrame(bigData[bigData['style'].isin(soft)])
    elif flavor == 'dry'
        beerList = pd.DataFrame(bigData[bigData['style'].isin(dry)])

    return beerList.sample(n=5)


def smoke(file, flavor):
    bigData = loadData(file)
    smolder = tuple('Smoked Beer')
    meaty = tuple('Rauchbier')

    if flavor == 'smolder':
        beerList = pd.DataFrame(bigData[bigData['style'].isin(smolder)])
    elif flavor == 'meaty':
        beerList = pd.DataFrame(bigData[bigData['style'].isin(meaty)])
    
    return beerList.sample(n=5)


def fruit(file, flavor):
    bigData = loadData(file)
    bright = ('Saison / Farmhouse Ale', 'Roggenbier', 'Hefeweizen','American Pale Wheat Ale','Herbed / Spiced Beer', 'English Pale Mild Ale',  'Kristalweizen', 'Witbier','Pumpkin Ale', 'Belgian Blonde Ale', 'Tripel')
    dark = ('Quadrupel (Quad)', 'Dunkelweizen', 'American Dark Wheat Ale', 'Rye Beer', 'Belgian Strong Dark Ale','English Dark Mild Ale', 'Dubbel')

    if flavor == 'bright':
        beerList = pd.DataFrame(bigData[bigData['style'].isin(bright)])
    elif flavor == 'dark':
        beerList = pd.DataFrame(bigData[bigData['style'].isin(dark)])
    
    return beerList.sample(n=5)


def sour(file,flavor):
    bigData = loadData(file)
    delicate = ('Gose','Berliner Weissbier')
    fruity = ('Flanders Red Ale','Flanders Oud Bruin','Fruit / Vegetable Beer')
    earthy = tuple('American Wild Ale')

    if flavor == 'delicate':
        beerList = pd.DataFrame(bigData[bigData['style'].isin(delicate)])
    elif flavor == 'fruity':
        beerList = pd.DataFrame(bigData[bigData['style'].isin(fruity)])
    elif flavor == 'earthy':
        beerList = pd.DataFrame(bigData[bigData['style'].isin(earthy)])

    return beerList.sample(n=5)
