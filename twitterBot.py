import tweepy
import datetime


#publishes tweets from twitter API
apikey = ...

apisecret = ...

bearerToken = ...
access_token = ...

access_t_secret = ...

auth = tweepy.OAuthHandler(apikey, apisecret) 
auth.set_access_token(access_token, access_t_secret)
api = tweepy.API(auth)

def publictweet(x):
    
    tweettopublish = x
    
    api.update_status(tweettopublish)
    print("tweeted")
