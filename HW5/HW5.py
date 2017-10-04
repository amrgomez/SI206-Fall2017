import re

f= open('regex_sum_37817.txt','r')
r=[]

flines= f.read()
o=re.findall('([0-9]+)', flines)
print(sum(int(x) for x in o))
