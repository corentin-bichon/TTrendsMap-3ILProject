from countriesById import *
from generateMap import *
from readTopTweet import *
from mapCoordinate import *


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Interface IHM
if __name__ == '__main__':
    list_country = []
    country = ""

    print('Enter country list : (enter \'OK\' for validate)')
    while True:
        country = input('Enter your country: ')
        if country != 'ok' and country != 'OK':
            list_country.append(country)
        else:
            break

    print(list_country)

    addMapCountry(list_country)
