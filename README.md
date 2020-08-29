# Twitter_OAuth1.0a
A script that grants your Twitter app read and write access to a Twitter account. 

## Getting started

- This implementation is designed to authorize a Twitter application with OAuth1.0a. With this script, you will be able to get read and write access to another account and control all your Twitter bots from your main developer account. You are welcomed to fill your own keys in and use the code accordingly.
- Remember that this script only includes the OAuth1.0a implementation. It will be useful to you only if you want to use your Twitter app from a profile other than your Twitter developer account, since I wrote the script assuming that owner of both accounts is the same person. For further information about other implementations please visit [Twitter Developer](https://developer.twitter.com/en/docs/ "Twitter Developer Documentations").

## Prerequisites
- You should have an approved Twitter developers account and provide your own API keys for your application.

- Installation of `Tweepy` library is necessary. (Open command prompt and type `pip install tweepy`.)

## Usage
- Run `get_token.py` first. It will generate the `authorization_url` for your application.
    ```
    https://api.twitter.com/oauth/authorize?oauth_token=HHiqAQAAAAABEhX0AAABcoaQ6F8 
    ```
- Please make sure you have signed in from the account that you would like to use as your bot profile before you click the link. This URL will prompt you to a page where you are asked whether you approve the authorization or not. 
   > <img src="https://i.hizliresim.com/EjVzyV.png" height="400" />

- When you click the `Authorize App` button, a single-use pin will be generated in the same page. You should enter the pin to the console, as this will be your `verifier` that will be used to generate the access tokens.
     
- After the app is authorized, you will have read-and-write access to the linked account. This permission level will allow you to post tweets, follow users, hide replies or update elements of a user’s profile information, so handle with care.  
    
    > <img src="https://i.hizliresim.com/ZZqBpx.png" height="150" />
    - You can revoke access anytime and you can have multiple accesses to different accounts with the same application, at the same time.

- Once you get the `access_token` and `access_token_secret`, copy and paste them to the relevant sections in `account_auth.py`. This is going to create the authentication and you will be able to use methods such as `update_status`. For other Tweepy methods, please check [ the API References](http://docs.tweepy.org/en/v3.8.0/api.html).

## Reminder
- Unless you want to regenerate the tokens for whatever reason, do not run `get_token.py` again for the same account. This is only going to create new tokens and make the former ones invalid. 
- I certainly advise you to store the access tokens safe for further use so that you don’t have to ask for access and verifier pin again and again. 

If you run into any errors, feel free to contact me and I'll try to help you out.
Enjoy your new bot account!
