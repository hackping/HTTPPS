#!/usr/bin/python
#encoding:utf-8

import re

lenlist = []
urllen = []
file = open('result.txt','r')
urls = file.readlines()
i = 0
for u in urls:
    urllen = []
    length = re.findall(r"Len---(.+?)---Len", u)
    urllen.append(u)
    urllen.append(length)
    lenlist.append(urllen)

res = open('result2.txt', 'a+')
result = sorted(lenlist,cmp=lambda x,y:cmp(x[1], y[1]))
for r in result:
    print(str(r).replace('\'','').replace('\\n','').replace('[','').replace(']',''))
    res.write(str(r).replace('\'','').replace('\\n','').replace('[','').replace(']','').replace(',','----------')+'\n')

