# -*- coding: utf-8 -*-

from flask import Flask, make_response, request
from twitter import *
from twitter.stream import TwitterStream, Timeout, HeartbeatTimeout, Hangup
import tweepy
import os
from http import HTTPStatus
from json import dumps
from threading import Thread

from stream import Stream

app = Flask(__name__)

ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']

def getOauth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)


def body():
    data = request.json
    if data.get('handle'):
         data['screen_name'] = data.pop('handle')
    if data.get('user'):
         data['user_id'] = data.pop('user')
    return data


def response(res):
    # TODO res.rate_limit_remaining
    # TODO res.rate_limit_limit
    # TODO res.rate_limit_reset
    return dict(res)


@app.route('/tweet', methods=['POST'])
def tweet():
    t = getOauth()
    data = request.json
    if data.get('status') is None or data.get('status') == "":
        res = {
            'status': 'failed',
            'reason': "'status' parameter is missing",
        }
        response_code = 400
        return dumps(res), response_code
    return dumps(t.update_status(data.pop("status"))._json)


@app.route('/retweet', methods=['POST'])
def retweet():
    t = getOauth()
    data = request.json
    if data.get('tweet') is None or data.get('tweet') == "":
        res = {
            'status': 'failed',
            'reason': "'tweet' parameter is missing"
        }
        response_code = 400
        return dumps(res), response_code
    response = t.retweet(int(data.pop("tweet")))
    return dumps(response._json)


@app.route('/follow', methods=['POST'])
def follow():
    t = getOauth()
    data = body()
    if data.get('id') is not None and data.get('id') != "":
        return dumps(t.create_friendship(data.pop("id"),follow=True)._json)
    elif data.get('screen_name') is not None and data.get('screen_name') != "":
        return dumps(t.create_friendship(data.pop("screen_name"),follow=True)._json)
    else:
        res = {
            'status': 'failed',
            'reason': "At least one of 'id' or 'screen_name' must be specified."
        }
        response_code = 400
        return dumps(res), response_code


@app.route('/unfollow', methods=['POST'])
def unfollow():
    t = getOauth()
    data = body()
    if data.get('id') is not None:
        return dumps(t.destroy_friendship(data.pop("id"))._json)
    elif data.get('screen_name') is not None:
        return dumps(t.destroy_friendship(data.pop("screen_name"))._json)
    else:
        res = {
            'status': 'failed',
            'reason': "At least one of 'id' or 'screen_name' must be specified."
        }
        response_code = 400
        return dumps(res), response_code

@app.route('/followers', methods=['POST'])
def followers():
    t = getOauth()
    data = body()
    if ((data.get('user_id') is None or data.get('user_id') == "") 
        and (data.get('screen_name') is None or data.get('screen_name') == "")):
        res = {
            'status': 'failed',
            'reason': "At least one of 'handle' or 'user' must be specified."
        }
        response_code = 400
        return dumps(res), response_code

    if data.get('user_id') is None or data.get('user_id') == "":
        responseArray = t.followers(data.get("user_id"))
    if data.get('screen_name') is None or data.get('screen_name') == "":
        responseArray = t.followers(data.get("screen_name"))
    
    resultArray = []
    for i in range(len(responseArray)):
        resultArray.append(responseArray[i]._json)
    return dumps(resultArray)

subscriptions = {}


@app.route('/stream/subscribe', methods=['POST'])
def stream_subscribe():
    auth = OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    data = body()
    if data["data"].get("track") is None or data["data"].get("track") == "":
        res = {
            'status': 'failed',
            'reason': "'track' parameter is missing"
        }
        response_code = 400
        return dumps(res), response_code
    subscriptions.setdefault(data['id'], Stream(auth, data).start())
    return 'Subscribed'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
