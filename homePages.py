import time


def homePage():
    print("\033[1;35;49m-----------------------------------------")
    print("--- \U0001F37B \033[1;37;49m Welcome to Nikki's Brewery \U0001F37B \033[1;35;49m---")
    print("-----------------------------------------")
    print("\033[0;36;49mWhat are you looking for?")
    print("a) Craft Beer \nb) Brewery Near Me")

    nextPage = input('')
    if nextPage == 'a':
        beerPage()
    elif nextPage == 'b':
        breweryPage()
    else:
        print("Invalid input. Please try again")
        time.sleep(1)
        homePage()


def beerPage():
    print("\033[1;35;49m--------------------------------")
    print("--- \U0001F37A \033[1;37;49m Find a Craft Beer \U0001F37A \033[1;35;49m---")
    print("--------------------------------")
    print("\033[0;32;49mClick 'x' to return to the home page")
    print("\033[0;36;49mSelect a flavor profile:")
    print("1) Crisp & Clean \n2) Hoppy & Bitter \n3) Malty & Sweet \n4) Dark & Roasty")
    print("5) Smokey \n6) Fruit & Spice \n7) Sour, Tart, & Funky")
    
    flavor = input('')
    if flavor == 'x':
        homePage()


def breweryPage():
    print("\033[1;35;49m-----------------------------")
    print("--- \U0001F30E \033[1;37;49m Find a Brewery \U0001F30E \033[1;35;49m---")
    print("-----------------------------")
    print("\033[0;32;49mClick 'x' to return to the home page")
    
    print("\033[0;36;49mPlease enter your city: ")
    city = input('')
    if city == 'x':
        homePage()
    else:
        print("\033[0;36;49mPlease enter your state: ")
        state = input('')
        print("Searching for breweries in " + city + ", " + state + "...")
        time.sleep(2)