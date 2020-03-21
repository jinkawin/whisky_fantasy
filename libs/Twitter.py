import tweepy
import requests
import json

from tweepy.binder import bind_api
from tweepy.api import API

from django.conf import settings
from django.urls import reverse
from django.http import HttpResponse, request
from django.shortcuts import redirect

class Twitter(API):

    MAX_TWEETS = 150

    def __init__(self, callback_url):
        self.callback = callback_url

        self.consumer_key = settings.TWITTER_API_KEY
        self.consumer_secret = settings.TWITTER_API_SECRET
        self.access_token = settings.TWITTER_ACCESS_TOKEN
        self.access_token_secret = settings.TWITTER_ACCESS_TOKEN_SECRET
        self.auth, self.api = self._auth()

    # Authentication by keys
    def _auth(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret, self.callback)
        auth.set_access_token(self.access_token, self.access_token_secret)

        api = tweepy.API(auth)
        return (auth, api)

    def login(self):
        try:
            redirect_url = self.auth.get_authorization_url()
            return redirect(redirect_url)
        except tweepy.TweepError as e:
            response_data = {"error": e}
            return HttpResponse(json.dumps(response_data), content_type="application/json")

    def me(self):
        data = {}
        result = self.api.me()
        data['name'] = result.name
        data['screen_name'] = result.screen_name
        data['id'] = result.id_str

        return data