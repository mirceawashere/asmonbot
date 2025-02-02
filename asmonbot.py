import google.generativeai as genai
import requests
from requests_oauthlib import OAuth1

# CREDENTIALS are ENV VARIABLES

# AI
genai.configure(api_key=GOOGLE_API)
model = genai.GenerativeModel("gemini-1.5-flash")
answer = model.generate_content("You're Asmongold, famous Twitch streamer. Be full of yourself, funny, ironic, snarky, be merciless.  Use his lingo and catch phrases and tone and keep up to date with the latest trends. Write a message for an X post, maximum 280 characters. It can be related to gaming or otherwise, keep the hashtags to a bear minimum (only if necessary) and don't say anything illegal or that would violate the terms of service.")


# X POST
auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
url = 'https://api.twitter.com/2/tweets'
tweet = {"text": answer.text}
response = requests.post(url, auth=auth, json=tweet)




