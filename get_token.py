import tweepy  # For Twitter API calls.
import request  #  # To issue HTTP requests to API.

# Fill in your own API keys obtained from https://developer.twitter.com/
consumer_key = ''
consumer_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# This will create a url in which you will authorize your app for the account you're signed in.
# You should click 'authorize app' in order to get the pin.
try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print("Error! Failed to get the request token.")

# Store request token in session.
session = {'request_token': auth.request_token}

# Enter the pin here as input. This will be used as verifier in order to access token.
verifier = request.GET.get('oauth_verifier')
print(redirect_url)
verifier = input('Verifier: ')

# OAuth process with keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
token = session.get('request_token')
auth.request_token = token

# Get access token.
try:
    auth.get_access_token(verifier)
except:
    print('Error! Failed to get access token.')

# These are the keys for the account. 
# You can store them for later use without having to run this code again.
print(auth.access_token)
print(auth.access_token_secret)
