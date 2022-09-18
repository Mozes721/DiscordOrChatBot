from http import client
from pydoc import cli
from scripts.twitter_response import TwitterResponseAPI
from config.config_files import APIkeys
import tweepy
import time

def connect():
    client = tweepy.Client(APIkeys.BearerToken, APIkeys.APIKey, APIkeys.APIKeySecret, APIkeys.AccessToken, APIkeys.AccessTokenSecret)
    auth = tweepy.OAuth1UserHandler(APIkeys.APIKey, APIkeys.APIKeySecret, APIkeys.AccessToken, APIkeys.AccessTokenSecret)
    api = tweepy.API(auth)
    client_id = client.get_me().data.id
    return client_id

    tweet = TwitterResponseAPI(twitterUser='Charlie')

    print(tweet.say_hello())

def check_tweets(response):
    for tweet in response.data:
                try:
                    print(tweet.text)
                    client.create_tweet(in_reply_to_tweet_id=tweet.id, text='hello')
                    start_id = tweet.id
                except:
                    pass

if __name__ == '__main__':
    start_id = 1
    twitter_bot = connect()
    while True:
        response = twitter_bot.get_users_mentions(twitter_bot, since_id=start_id)
        if response.data != None:
            check_tweets(response)
        time.sleep(5)

    
