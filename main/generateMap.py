import folium

from readTopTweet import *
from mapCoordinate import *


# Crée une Map dans indexcountry.html à partir d'un nom de pays
def createMap():
    folium.LayerControl().add_to(map)
    map.save('indexcountry.html')


# Ajoute la pays en surligné sur la carte et les tops tweets de se pays
def addMapCountry(list_country):
    map = folium.Map(location=[51.1657, 10.4515], zoom_start=3, min_zoom=1, max_zoom=7)

    for country_name in list_country:
        folium.Marker(
            location=getCityCoordinate(country_name),
            popup=getTopTweet(country_name),
            icon=folium.Icon(color='blue', icon='ok-sign'),
        ).add_to(map)

        folium.GeoJson(getSingleCountry(country_name), name=str(country_name)).add_to(map)

    folium.LayerControl().add_to(map)

    map.save('indexcountry.html')
