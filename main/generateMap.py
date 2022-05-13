import folium

from readTopTweet import *
from mapCoordinate import *


# Crée une Map dans indexcountry.html à partir d'un nom de pays
def createMap():
    folium.LayerControl().add_to(map)
    map.save('../output/index-country.html')


# Ajoute la pays en surligné sur la carte et les tops tweets de se pays
def addMapCountry(list_country):
    map = folium.Map(location=[51.1657, 10.4515], zoom_start=3, min_zoom=1, max_zoom=7)

    for country_name in list_country:
        folium.Marker(
            location=getCityCoordinate(country_name),
            popup=getHtmlTopTweet(country_name),
            icon=folium.Icon(color='blue', icon='twitter', prefix='fa'),
        ).add_to(map)
        print(country_name)
        print(getCityCoordinate(country_name))
        print(getSingleCountry(country_name))

        folium.GeoJson(getSingleCountry(country_name), name=str(country_name)).add_to(map)

    folium.LayerControl().add_to(map)

    map.save('../output/index-country.html')

# Ajoute un seul pays à la map et zoom dessus
def addMapSingleCountry(country_name):

    map = folium.Map(location=getCityCoordinate(country_name), zoom_start=5, min_zoom=1, max_zoom=7)

    folium.Marker(
        location=getCityCoordinate(country_name),
        popup=getHtmlTopTweet(country_name),
        icon=folium.Icon(color='blue', icon='twitter', prefix='fa'),
    ).add_to(map)

    folium.GeoJson(getSingleCountry(country_name), name=str(country_name)).add_to(map)

    folium.LayerControl().add_to(map)

    map.save('../output/index-country.html')

#
def addMapGlobalCountry(list_country):
    map = folium.Map(location=[51.1657, 10.4515], zoom_start=3, min_zoom=1, max_zoom=7)

    for country_name in list_country:
        folium.Marker(
            location=getCityCoordinate(country_name),
            popup=getHtmlTopTweet(country_name),
            icon=folium.Icon(color='blue', icon='twitter', prefix='fa'),
        ).add_to(map)

        folium.GeoJson(getSingleCountry(country_name), name=str(country_name)).add_to(map)

    folium.LayerControl().add_to(map)

    map.save('../output/index-country.html')