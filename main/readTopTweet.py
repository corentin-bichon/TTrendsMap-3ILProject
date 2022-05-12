from countriesById import *

resultat_tweet = open('../output/resultat.json', 'r', encoding="utf-8").read()


# Renvoi une liste des 10 top tweets du pays passé en paramètre
def getTopTweet(country_name):
    id_country = getcountriesId(country_name)
    top_tweet_list = json.loads(resultat_tweet)

    tweetlist = ['Top tweet ' + getcountriesbyid(id_country)]
    tweet_count = 0

    for tweets_country in top_tweet_list['Top tweets']:
        for tweets in tweets_country:
            for tweetlocation in tweets['locations']:
                if tweetlocation['woeid'] == id_country:
                    for singletweet in tweets['trends']:
                        tweetlist.append(singletweet['name'])
                        tweet_count += 1
                        if tweet_count == 10:
                            break
            break
    return tweetlist


# Renvoi une liste des 10 top tweets du pays passé en paramètre en format HTML
def getHtmlTopTweet(country_name):
    id_country = getcountriesId(country_name)
    top_tweet_list = json.loads(resultat_tweet)

    # Titre de la popup
    tweethtml = "<h2 style='text-align:center; min-width:105px; margin-bottom:2px; color:#3388FF'> Trends </h2>" + "<h4 style='text-align:center; margin-top:0px'>" + getcountriesbyid(
        id_country) + "</h4>"
    # On ouvre la liste
    tweethtml += "<ul style='text-align:center; list-style-type:none; padding:0'>"
    tweet_count = 0

    for tweets_country in top_tweet_list['Top tweets']:
        for tweets in tweets_country:
            for tweetlocation in tweets['locations']:
                if tweetlocation['woeid'] == id_country:
                    for singletweet in tweets['trends']:
                        tweethtml += "<li> <a href='" + singletweet['url'] + "' target='blank'>" + singletweet[
                            'name'] + "</a> </li>"
                        tweet_count += 1
                        if tweet_count == 10:
                            break
            break

    tweethtml += "</ul>"

    return tweethtml


# Retourne tous les noms des pays qui ont des tendances
def getAllCountry():
    list_world_country = []
    top_tweet_list = json.loads(resultat_tweet)

    for tweets_country in top_tweet_list['Top tweets']:
        for tweets in tweets_country:
            for tweet_location in tweets['locations']:
                if tweet_location['woeid'] != 1:
                    list_world_country.append(getcountriesbyid(tweet_location['woeid']))
            break

    return list_world_country
