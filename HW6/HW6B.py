import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ') #http://py4e-data.dr-chuck.net/known_by_Todd.html
pos= int(input('Enter position: '))
count= int(input('Enter count: '))
# Retrieve all of the anchor tags
for x in range(count):
    h= urllib.request.urlopen(url, context=ctx).read()
    s= BeautifulSoup(h, 'html.parser')
    tags = s('a')
    print(tags[pos-1].get('href',None))
    url= tags[pos-1].get('href',None)
