from typing import List
from urllib import response
from requestTwitterAPI import *

file_countries = "../data/world-countries-code.json"
output_file_name = "../output/resultat.json"
data = 'woeid'


def getJsonTweetGlobal():
    n = 0
    list_countries = loop_processing_global(file_countries, data)
    fichier = open(output_file_name, "w")  # Créer le fichier s'il n'existe pas
    fichier.close()
    add_file(output_file_name, '{ "Top tweets": [')
    add_file(output_file_name, '\n')
    for id_countries in list_countries:
        n = n + 1
        response = exec_API(id_countries)
        text_append = response.text
        add_file(output_file_name, text_append)
        if n != len(list_countries):
            add_file(output_file_name, ',')
        add_file(output_file_name, '\n')
    add_file(output_file_name, ']}')
    my_func("\/", "/")

def getJsonTweetByCountry(list_country):
    n = 0
    list_countries = loop_processing_countries(list_country,file_countries,data)
    fichier = open(output_file_name, "w")  # Créer le fichier s'il n'existe pas
    fichier.close()
    add_file(output_file_name, '{ "Top tweets": [')
    add_file(output_file_name, '\n')
    for id_countries in list_countries:
        n = n + 1
        response = exec_API(id_countries)
        text_append = response.text
        add_file(output_file_name, text_append)
        if n != len(list_countries):
            add_file(output_file_name, ',')
        add_file(output_file_name, '\n')
    add_file(output_file_name, ']}')
    my_func("\/", "/")
