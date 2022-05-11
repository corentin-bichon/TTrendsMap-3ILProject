from generateMap import *
from generateJsonTweets import *

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
    #getJsonTweet()
    addMapCountry(list_country)
