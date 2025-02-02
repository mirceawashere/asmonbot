from fastapi import FastAPI
import os
import google.generativeai as genai
import requests
import random
from requests_oauthlib import OAuth1

app = FastAPI()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
google_key = os.getenv("GOOGLE_API")


@app.get("/post")
def post_to_X():
    genai.configure(api_key=google_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    random_number = random.randint(1,3)
    if random_number == 1:
        answer = model.generate_content("You're Asmongold, famous Twitch streamer. Be full of yourself, funny, ironic, snarky, be merciless.  Use his lingo and catch phrases and tone. Write an X post, maxium 280 characters. Keep the hashtags to a bear minimum (only if necessary) and don't say anything illegal or that would violate the terms of service. The post should be about gaming.")
    elif random_number ==2:
        answer = model.generate_content("You're Asmongold, famous Twitch streamer. Be full of yourself, funny, ironic, snarky, be merciless.  Use his lingo and catch phrases and tone. Write an X post, maxium 280 characters. Keep the hashtags to a bear minimum (only if necessary) and don't say anything illegal or that would violate the terms of service. The post should be about non-gaming news.")
    else:
        answer = model.generate_content("You're Asmongold, famous Twitch streamer. Be full of yourself, funny, ironic, snarky, be merciless.  Use his lingo and catch phrases and tone. Write an X post, maxium 280 characters. Keep the hashtags to a bear minimum (only if necessary) and don't say anything illegal or that would violate the terms of service. The post should be about politics.")
    message = answer.text
    auth = OAuth1(api_key, api_secret, access_token, access_token_secret)
    url = 'https://api.twitter.com/2/tweets'
    tweet = {"text": message}
    requests.post(url, auth=auth, json=tweet)
