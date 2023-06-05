from .config_files import APIkeys
import tweepy


def connect():
    client = tweepy.Client(APIkeys.BearerToken, APIkeys.APIKey,
                           APIkeys.APIKeySecret,
                           APIkeys.AccessToken, APIkeys.AccessTokenSecret)
    auth = tweepy.OAuth1UserHandler(APIkeys.APIKey, APIkeys.APIKeySecret,
                                    APIkeys.AccessToken,
                                    APIkeys.AccessTokenSecret)
    api = tweepy.API(auth)
    client_id = client.get_me().data.id
    return client, client_id, api
