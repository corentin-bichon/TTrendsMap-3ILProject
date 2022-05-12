import time

from generateMap import *
from generateJsonTweets import *


def enter_country():
    print('Enter country list : (enter \'OK\' for validate)')
    while True:
        country = input('Enter your country: ')
        if country != 'ok' and country != 'OK':
            list_country.append(country)
        else:
            break
    return list_country


# Interface IHM
if __name__ == '__main__':
    list_country = []
    country = ""

    print(' ----- TTrendsMAP ----- ')

    print(' Current options :')
    print(' 1. Shows World Trends ')
    print(' 2. Shows country Trend ')
    print(' 3. Shows list of country Trends ')

    option_selected = input('Enter your choice : ')

    print(' ----- Country Selection ----- ')

    if option_selected == '1':
        # getJsonTweetGlobal()
        print(getAllCountry())
        addMapCountry(getAllCountry())

    elif option_selected == '2':
        country = input('Enter your country: ')
        list_country.append(country)
        getJsonTweetByCountry(list_country)
        addMapSingleCountry(country)

    elif option_selected == '3':
        list_country = enter_country()
        getJsonTweetByCountry(list_country)
        time.sleep(5)
        addMapCountry(list_country)

    else:
        print(' Invalid entry ')

