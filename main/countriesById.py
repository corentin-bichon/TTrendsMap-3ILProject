import json

# Corréler l'ID du tweet et le pays associé
with open('../data/world-countries-code.json') as handle:
    country_geo_code = json.loads(handle.read())

def getcountriesbyid(id_country_tweet):
    for i in country_geo_code:
        if i['woeid'] == id_country_tweet:
            country_geo_name = i['country']
            break
    return country_geo_name

def getcountriesId(country_name):
    for j in country_geo_code:
        if j['country'] == country_name:
            country_geo_id = j['woeid']
            break
    return country_geo_id