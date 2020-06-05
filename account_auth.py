import tweepy   # For Twitter API call

# Use your API keys once again.
# Copy the keys that you obtained from get_token.py and paste here.
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret  = ''

# This creates the authentication using the keys.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Tweets from the user whose authentication keys were used above.
api.update_status('Test tweet.')
