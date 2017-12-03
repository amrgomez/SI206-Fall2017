import itertools
import collections
import json
import requests
import api_info
import sqlite3
import facepy
#Name: Amanda Gomez
#APIS: Facebook, Google Maps, Darksky, DropBox, News, Twilio, Slack

#Caching
CACHE_FNAME = "206ProjectCache.json"
try:
    cache_file = open(CACHE_FNAME,'r')
    cache_contents = cache_file.read()
    cache_file.close()
    CACHE_DICTION = json.loads(cache_contents)
except:
    CACHE_DICTION = {}
def getWithCaching(baseURL, params={}):
  req = requests.Request(method = 'GET', url =baseURL, params = sorted(params.items()))
  prepped = req.prepare()
  fullURL = prepped.url
  if fullURL not in CACHE_DICTION:
      response = requests.Session().send(prepped)
      CACHE_DICTION[fullURL] = response.text
      cache_file = open(CACHE_FNAME, 'w')
      cache_file.write(json.dumps(CACHE_DICTION))
      cache_file.close()
  return CACHE_DICTION[fullURL]
#Facebook
api=
def get_fb_user(user):
    if user in CACHE_DICTION:
        print("cached")
        response = CACHE_DICTION[user]
    else:
        print('Making new request')
        response = api.public_profile(screen_name = user, count = 100)
        print(response)
        CACHE_DICTION[user] = response
        jsd = json.dumps(CACHE_DICTION)
        cache_file = open(CACHE_FNAME, 'w')
        cache_file.write(jsd)
        cache_file.close()
    return response

fb_feed= get_fb_user('Amanda Gomez')
