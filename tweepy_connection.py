import tweepy

#Twitter API credentials are stored om config.py
# BEARER_TOKEN = '<token>'

# API_KEY = '<key>'
# SECRET_KEY = '<key>'

# ACCESS_TOKEN = '<token>'
# SECRET_TOKEN = '<token>'

#Import the file where above credentials are stored
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

auth = tweepy.OAuthHandler(config.API_KEY, config.SECRET_KEY)
auth.set_access_token(config.ACCESS_TOKEN, config.SECRET_TOKEN)
api = tweepy.API(auth)

#Get User Information
def get_user_info(twitter_usernames_list):
    users_info = client.get_users(usernames=twitter_usernames_list)
    return users_info.data
    #user_id = users_info.data[0].id

#Get User Tweets
def get_user_tweets(user_id):
    user_tweets = client.get_users_tweets(user_id)
    return user_tweets.data
    #user_tweet_text = user_tweets.data[0]

def get_tweet_liking_users(tweet_id):    
    tweet_likes = client.get_liking_users(tweet_id)
    return tweet_likes.data