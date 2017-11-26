import requests
import facebook #pip install facebook-sdk
import json

print("Welcome")
access_token= #tokennumber #if expires, go to https://developers.facebook.com/tools/explorer
if access_token is None:
    access_token= input('\nCopy and paste token from https://developers.facebook.com/tools/explorer')

graph= facebook.GraphAPI(access_token)
all_fields= ['messahe', 'created_time', 'description', 'caption', 'likes']
all_fields=','.join(all_fields)
profile= graph.get_object('me', fields= 'name,location{location}')
print(json.dumps(profile,indent= 4))

while True:
    try:
        with open('my_posts.json', 'a') as f:
            for post in posts['data']:
                f.write(json.dumps(post)+ '\n')
            posts= requests.get(posts['paging']['next'].json())
    except KeyError:
        #when posts run out
        break
