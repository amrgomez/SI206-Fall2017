import itertools
import collections
import json
import requests
import api_info
import sqlite3
import datetime
import googlemaps
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
import numpy as np
import re
#Name: Amanda Gomez
#APIS: Facebook,Google Maps,News, Google Geocoding, Darksky

#Caching
CACHE_FNAME = "206ProjectCache.json" #creating json file
try:
    cache_file = open(CACHE_FNAME,'r')
    cache_contents = cache_file.read()
    cache_file.close()
    CACHE_DICTION = json.loads(cache_contents)
except: #if file is created, dont do anything
    CACHE_DICTION = {}

#caching links- News,Google Maps, DarkSky
def getWithCaching(baseURL, params={}):
    #using requests to fill in full url with access token and baseurl
  req = requests.Request(method = 'GET', url =baseURL, params = sorted(params.items()))
  prepped = req.prepare()
  fullURL = prepped.url#prepares url from params and base url
  #check to see if url is in cache
  if fullURL not in CACHE_DICTION:#adds url to dictionary
      response = requests.Session().send(prepped) #send prepped url to dictionary
      CACHE_DICTION[fullURL] = response.text#adds url to dictionary
      cache_file = open(CACHE_FNAME, 'w')
      cache_file.write(json.dumps(CACHE_DICTION))#puts url info into cache
      cache_file.close()
  return CACHE_DICTION[fullURL]

#News API
def get_headline(word):
    if word in CACHE_DICTION:#if word already in CACHE_DICTION, don't add it, print 'cached'
        print('cached')
        ndata=CACHE_DICTION[word]
    else:
        print('making new request')
        newskey= api_info.n_key #takes news key from api_info
        #took place on Dec. 10th
        nresponse= getWithCaching('https://newsapi.org/v2/everything?q={}&from2017-12-10&sortBy=popularity&apiKey={}'.format(word,newskey))#add params to base url
        ndata=json.loads(nresponse)
        CACHE_DICTION[word]=ndata#adds data from selected url to CACHE_DICTION
        jsd2= json.dumps(CACHE_DICTION)#places data into CACHE_DICTION
        cache_file= open(CACHE_FNAME, 'w')#opens cached file
        cache_file.write(jsd2)#writes data to CACHE_FNAME
        cache_file.close()#closes file
    return ndata
n=get_headline('dog')#grabs data for all headlines containing 'dog'
#Creation of Articles sql table
conn= sqlite3.connect('FinalProject.sqlite') #creation of 'FinalProject' SQL table
cur= conn.cursor()

cur.execute('DROP TABLE IF EXISTS Articles')#if Articles table exists, don't add another table
cur.execute('CREATE TABLE Articles (title TEXT, author TEXT, description TEXT, url TEXT, time_published TEXT)')
#create Articles table with title, author, description, url, time_published columns

for s in n:
    stuff='INSERT OR IGNORE INTO Articles (title, author, description, url, time_published) VALUES (?,?,?,?,?)'#inserts values into columns
    for y in range(10):#takes first 20 articles in data and returns given values
        tup= n['articles'][y]['title'],n['articles'][y]['author'],n['articles'][y]['description'],n['articles'][y]['url'],n['articles'][y]['publishedAt']
        #finds titles, authors, descriptions, urls, and date published
        cur.execute(stuff,tup)#Adds data to table Articles

conn.commit()#publishes data to SQL table

# #GoogleMaps API
def get_location(place):
    #check to see if city is in cached file
    if place in CACHE_DICTION:
        print('cached')
        g_results= CACHE_DICTION[place]
    else:
        print('making new request')
        Googlekey= api_info.gm_key#Google Maps key from api_info
        param= {'key': Googlekey, 'address': place}#Parameters included key and name of a place
        gresponse= getWithCaching('https://maps.googleapis.com/maps/api/geocode/json', params= param)
        g_results= json.loads(gresponse)#Creates string of info received in link above
        CACHE_DICTION[place]=g_results
        jsd2= json.dumps(CACHE_DICTION)
        cache_file= open(CACHE_FNAME, 'w')
        cache_file.write(jsd2)
        cache_file.close()
    return g_results #Returns the string retreived and stores in json cache file
p= get_location('Ann Arbor')#Retrieves location information of Ann Arbor

# #DarkSky API
def get_weather(lat,lng):
    if lat and lng in CACHE_DICTION:
        print('cached')
        d_result= CACHE_DICTION[place]
    else:
        print('making new request')
        darkkey=api_info.ds_key#DarkSky key
        dresponse= getWithCaching('https://api.darksky.net/forecast/{}/{},{}'.format(darkkey, lat,lng))
        d_result= json.loads(dresponse)
    return d_result
la=p['results'][0]['geometry']['location']['lat']#uses Ann Arbor location info to retreive lattitude and longitude
ln=p['results'][0]['geometry']['location']['lng']
u=get_weather(la,ln)#Receives Ann Arbor weekly forecast based on lattitude and longitude
#Creation of Weather SQL table
conn= sqlite3.connect('FinalProject.sqlite')#connects to FinalProject SQL table
cur= conn.cursor()

cur.execute('DROP TABLE IF EXISTS Weather')
cur.execute('CREATE TABLE Weather (time_ TEXT, summary TEXT)')#Creating Weather table

for w in u:
    stuff2='INSERT OR IGNORE INTO Weather (time_,summary) VALUES (?,?)'
    for k in range(6):#Returns 54 hourly updates (increments of 9, so 6x9=54)
        tup2= u['hourly']['data'][k]['time'],u['hourly']['data'][k]['summary']#retrieves time and summary of hourly updates
        cur.execute(stuff2,tup2)

conn.commit()

#Created visualization of articles w/ "dog" in title
cur.execute('SELECT time_published FROM Articles')#selects date and time article was published from SQL
dates=cur.fetchall()
f=[]
for it in dates:
    red=re.compile('\w+')#use regular expressions to find all characters a-z and 0-9
    f.append(int(red.match(it[0][5:7])[0]))#Find months from time_published tuple ex. '10'
trace=go.Histogram(x=f)#X-axis is month values
layout=go.Layout(title='Articles through the months with "dog" in title',
    xaxis=dict(
        title='Month',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='# Articles',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )))#Labels of x axis, y axis, and title
fig= go.Figure(data=[trace],layout=layout)#Creates figure with data of month values and layout labels
py.iplot(fig, filename= 'Article-data')#plots figure and saves into drive
