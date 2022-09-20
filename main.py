from dataclasses import dataclass
from http import client
from pydoc import cli
from scripts.twitter_response import TwitterResponseAPI
# from config.config_files import APIkeys
import tweepy
import time

def connect():
    client = tweepy.Client(BearerToken, APIKey, APIKeySecret, AccessToken, AccessTokenSecret)
    auth = tweepy.OAuth1UserHandler(APIKey, APIKeySecret, AccessToken, AccessTokenSecret)
    api = tweepy.API(auth)
    client_id = client.get_me().data.id
    return client, client_id

    # tweet = TwitterResponseAPI(twitterUser='Charlie')

    # print(tweet.say_hello())


class TwitterAPI:
    def __init__(self, client, client_id):
        self.start_id = 1
        self.client = client 
        self.response = client.get_users_mentions(client_id, since_id=self.start_id)

    def __post_init__(self):
        print("Connection has been established..")
        self.check_tweets()


    def check_tweets(self):
        while True:
            if self.response.data != None:
                for tweet in self.response:
                    try:
                        print(tweet.text)
                        self.client.create_tweet(in_reply_to_tweet_id=tweet.id, text='hello')
                        self.start_id = tweet.id
                    except Exception as error:
                        print(error)
                        
            time.sleep(5)

if __name__ == '__main__':
    client, client_id = connect()
    TwitterAPI(client, client_id)

   

    
