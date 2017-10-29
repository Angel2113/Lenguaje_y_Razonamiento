#!/usr/bin/python
#-*- coding: utf-8 -*-
# Angel Callejas  Rodriguéz
# Octubre, 2017


'''
    Este codigo descarga tweets del usuario y por stream
    haciendo uso del api de twitter

'''
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener

c_key = 'YpbwMBNHgnkGTeQNboKZzSI4B'
c_secret = 'RET20Mmesz3JPT3YzWrmAZHlm6kqjikDqgNyyKQUbxNoxRjyX6'

a_token = '3179474136-J4icCODyJSHQ6NmnTryxMzOrUyVoEZc0kC5BdIy'
a_secret = 'cUdH23ULO5kbCfj4N8D5ovDGxSTVeidcbAy5I2TWjZ6z9'

# By streaming
class StreamListener(StreamListener):
    def on_status(self, status):
        print (status.text)
        return True

    def on_error(self, status):
        if status == 420:
            return False
        print (status)

def streaming_tweets(busqueda = None):
    # Inicio de session
    auth = tweepy.OAuthHandler(consumer_key=c_key, consumer_secret=c_secret)
    auth.set_access_token(a_token, a_secret)

    api = tweepy.API(auth)

    # Inicia el stream
    listener = StreamListener()
    myStream = tweepy.Stream(auth = auth, listener=listener)

    myStream.filter(track=busqueda)

# Tweets User
def user_tweets(username):
    # Limite de 3 mil tweets

    # Inicia la session
    auth = tweepy.OAuthHandler(consumer_key=c_key, consumer_secret=c_secret)
    auth.set_access_token(a_token, a_secret)

    api = tweepy.API(auth)

    # Lista de tweets
    all_tweets = []

    # primeros 200
    tweets = api.user_timeline(screen_name = username, count = 200)

    all_tweets.extend(tweets)

    # Obtener el ultimo id
    last_id = all_tweets[-1].id -1

    # Ciclo
    while len(tweets) > 0:
        # Obtener 200
        tweets = api.user_timeline(screen_name = username, count = 200, max_id=last_id)

        # Agregar los tweets
        all_tweets.extend(tweets)

        # Obtener el ultimo id
        last_id = all_tweets[-1].id -1
    return all_tweets
