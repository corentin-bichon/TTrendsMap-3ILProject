import json

# Ouverture des json
with open('../data/world-countries.json') as handle:
    country_geo = json.loads(handle.read())

with open('../data/world-city.json') as handle:
    city_geo = json.loads(handle.read())


# Renvoi les coordonnées précis du Pays (tout le périmètre)
def getSingleCountry(name_country_tweet):
    country_coordinate = 'null'
    for i in country_geo['features']:
        if i['properties']['name'] == str(name_country_tweet):
            country_coordinate = i
            break
    return country_coordinate


# Renvoi un point se situant au milieu du Pays entré en paramètre
def getCityCoordinate(name_country_tweet):
    city_coordinate = 'null'
    for j in city_geo:
        if j['name'] == name_country_tweet:
            city_coordinate = j['latlng']
            break
    return city_coordinate
