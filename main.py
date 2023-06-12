from dataclasses import dataclass
from config.connection import connect
from api.requests import APIRequests
from scripts.twitter_response import TwitterResponses
import time
import tweepy


@dataclass
class TwitterAPI:
    api: tweepy.API
    start_id: int
   

    def __post_init__(self):
        print("Connection has been established..")
        print("This is a client", self.api)

    def check_tweets(self, response):
        for tweet in response:
            try:
                # print(tweet.user)
                twitter_responses = TwitterResponses(twitterUser='Casidy')
                reply_message = twitter_responses.reply_to_user
                # self.api.update_status(
                #             in_reply_to_status_id=tweet.id,
                #             status=reply_message
                #             )
                self.start_id = tweet.id
                # client.create_tweet(in_reply_to_tweet_id=tweet.id, text=reply_message)
            except Exception as error:
                raise error



if __name__ == '__main__':
    client, client_id, api = connect()
    start_id = 1
    twitter_api = TwitterAPI(api, start_id)
    api_requests = APIRequests()

    while True:
        response = client.get_users_mentions(client_id, since_id=start_id)

        if response.data != None:
            twitter_api.check_tweets(response.data)
        
        time.sleep(5)