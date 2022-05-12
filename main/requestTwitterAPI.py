import requests
import json

def add_file(file_name,text_append):
    fichier = open(file_name, "a", encoding="utf-8") #Créer le fichier s'il n'existe pas
    fichier.write(text_append) #Écrit la valeur de la variable a dans le fichier
    fichier.close()

def my_func(arg1="'",arg2='"',file_name='../output/resultat.json'):
    # Read in the file
    with open(file_name, 'r') as file :
     filedata = file.read()
    # Replace the target string
    filedata = filedata.replace(arg1, arg2)    
    # Write the file out again
    with open(file_name, 'w') as file:
     file.write(filedata)

def loop_processing_global(file_name,data):
    List_countries=[]
    fileObject = open(file_name, "r")
    jsonContent = fileObject.read()
    tweet_data = json.loads(jsonContent)
    nbr_countries=int(len(tweet_data))
    fileObject.close()
    for id in range(nbr_countries):
        id_countries = tweet_data[id][data]
        List_countries.append(id_countries)
    return List_countries

def loop_processing_countries(list_country,file_countries,data):
    List_countries=[]
    fileObject = open(file_countries, "r")
    jsonContent = fileObject.read()
    tweet_data = json.loads(jsonContent)
    nbr_countries=int(len(tweet_data))
    fileObject.close()

    for name_country in list_country:
        for id in range(nbr_countries):
            country=tweet_data[id]["country"]
            if name_country == country:
                id_countries = tweet_data[id][data]
                List_countries.append(id_countries)
    return List_countries

def exec_API(id_countries):
    id_countries=str(id_countries)
    url = "https://api.twitter.com/1.1/trends/place.json?id="+id_countries
    payload={}
    headers = {
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAKXHbgEAAAAAlQdTL3vxyIoG9bbF7h4Lv%2BIb93s%3DBryRpZOqWngmZWbn9CAFhdsf6DL45ybUzccBRPLisP3a8SwhK0',
    'Cookie': 'guest_id=v1%3A165177601086488368'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response