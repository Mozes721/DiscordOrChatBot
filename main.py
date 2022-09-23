from dataclasses import dataclass
from http import client
import os
from scripts.twitter_response import TwitterResponseAPI
from config.config_files import APIkeys
import tweepy
import time


def connect():
    client = tweepy.Client(APIkeys.BearerToken, APIkeys.APIKey, APIkeys.APIKeySecret, APIkeys.AccessToken, APIkeys.AccessTokenSecret)
    auth = tweepy.OAuth1UserHandler(APIkeys.APIKey, APIkeys.APIKeySecret, APIkeys.AccessToken, APIkeys.AccessTokenSecret)
    api = tweepy.API(auth)
    client_id = client.get_me().data.id
    return client, client_id

    # tweet = TwitterResponseAPI(twitterUser='Charlie')

    # print(tweet.say_hello())
@dataclass
class TwitterAPI:
    client: list
    client_id: str
    start_id: int
    response: str
        

    def __post_init__(self):
        print("Connection has been established..")
        print("%s this is a client", self.client)
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
    start_id = 1
    while True:
        response = client.get_users_mentions(client_id, since_id=start_id)
        TwitterAPI(client, client_id, start_id, response)

   

    
