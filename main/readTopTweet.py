from countriesById import *

resultat_tweet = open('../output/resultat.json', 'r', encoding="utf-8").read()

#Renvoi une liste des 10 top tweets du pays passé en paramètre
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