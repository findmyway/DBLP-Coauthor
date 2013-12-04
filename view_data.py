# -*- coding: utf-8 -*-
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14) 
import codecs
import matplotlib.pyplot as plt
import numpy as np
data = codecs.open('authors_encoded.txt','r','utf-8')
word_counts = {}
maxCounts = 0
for line in data:
    line = line.split(',')
    for word in line[0:-1]:
        word_counts[word] = word_counts.get(word,0) + 1
        if word_counts[word] > maxCounts:
            maxCounts = word_counts[word]
            maxKey = word

xMax = maxCounts
data.close()
bins = {}
for k,v in word_counts.iteritems():
    bins[v] = bins.get(v,0) + 1

y = []
for i in range(40, 200):
    y.append(bins.get(i,0))
plt.plot(y,'-');
plt.grid()
plt.yticks(range(0,1000,100))
plt.xticks(range(0,160,20),range(40,200,20))
plt.xlabel(u'支持度',fontproperties=font)
plt.ylabel(u'对应支持度下的作者个数',fontproperties=font)
plt.title(u'作者数量与支持度之间的对应关系',fontproperties=font)
plt.show()
