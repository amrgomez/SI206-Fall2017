import re

m= open('mbox-short.txt','r')
r=[]
mlines = m.readlines()

for line in mlines:
    h= re.findall('From',line)
    l= re.findall('@',line)
    #word before @
    b= re.findall('^From([^ ]*)*@.',l)
    print(b)
#('^From .*@([^ ]*)',lin)
