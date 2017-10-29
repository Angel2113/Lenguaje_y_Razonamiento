## #!/usr/bin/python
#-*- coding: utf-8 -*-
# Angel Callejas  Rodriguéz
# Octubre, 2017

# GetOldTweets: https://github.com/Jefferson-Henrique/GetOldTweets-python
#The MIT License (MIT)
#Copyright (c) 2016 Jefferson Henrique

'''
    Este codigo descarga tweets del usuario y por stream
    haciendo uso del GetOldTweets que no usa llaves

    Me parece que puede ser baneado, no abusar de
'''
#import .got3 as got
from . import got3 as got

# By username
def get_by_username(username, number):
    tweetCriteria = got.manager.TweetCriteria().setUsername(username).setMaxTweets(number)
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)
    return tweet

# By query search
def get_by_query(query, number):
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(query).setMaxTweets(number)
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)
    return tweet

# Username and bound
def get_by_username_bound(username, since, until, number):
    tweetCriteria = got.manager.TweetCriteria().setUsername(username).setSince(since).setUntil(until).setMaxTweets(number)
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)
    return (tweet)

# Top Ten by username
def get_top(username):
    tweetCriteria = got.manager.TweetCriteria().setUsername(username).setTopTweets(True).setMaxTweets(10)
    # first one
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)
    return (tweet)
