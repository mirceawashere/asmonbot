from fastapi import FastAPI
import os
import google.generativeai as genai
import requests
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
    answer = model.generate_content("You're Asmongold, famous Twitch streamer. Be full of yourself, funny, ironic, snarky, be merciless.  Use his lingo and catch phrases and tone and keep up to date with the latest trends. Write a message for an X post, maximum 280 characters. It can be related to gaming or otherwise, keep the hashtags to a bear minimum (only if necessary) and don't say anything illegal or that would violate the terms of service.")
    message = answer.text
    auth = OAuth1(api_key, api_secret, access_token, access_token_secret)
    url = 'https://api.twitter.com/2/tweets'
    tweet = {"text": message}
    requests.post(url, auth=auth, json=tweet)
