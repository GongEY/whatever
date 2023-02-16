from facepy import GraphAPI
from os import path

defaultLimit = 100

file = open('test.txt', 'w')

def decodeData(data):
    return repr(data).decode('unicode-escape')

def getFeed(after = ''):
    return graph.get(
        path='yonseibamboo/feed',
        limit=defaultLimit,
        after=after
    )

def writeFeed(feedData):
    for feed in feedData:
        file.write(decodeData(feed['message']).encode('UTF-8'))

graph = GraphAPI('EAAEKalLy9d4BAGNZAYOUhaGQFt870AIjqni9F0eyGc13ZC5R23FJPQNdrTfVM8PaQIV40eoLz1ScJE83pe2UjypnoLH3roHNLwXn4oEifpefWok2rkPRQCEdpQy9fLtl31pyCUuQEWAiQ7GwLZBFo7HrY6K3MMpx1bBX6uPxwqt6fbAUz1g25skxjoOQzcZD')

after = ''
for x in range(0, 1):
    bambooData = getFeed(after)
    writeFeed(bambooData['data'])
    after = bambooData['paging']['cursors']['after']

file.close()

d = path.dirname(__file__)
text = open(path.join(d, 'test.txt')).read()

#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from collections import Counter
import urllib
import random
import webbrowser

from konlpy.tag import Hannanum
from konlpy.tag import Twitter
import pytagcloud # requires Korean font support
import sys


if sys.version_info[0] >= 3:
    urlopen = urllib.request.urlopen
else:
    urlopen = urllib.urlopen

r = lambda: random.randint(0,255)
color = lambda: (r(), r(), r())

def get_tags(text, ntags=50, multiplier=10):
    h = Hannanum()
    nouns = h.nouns(text)
    count = Counter(nouns)
    return [{ 'color': color(), 'tag': n, 'size': c*multiplier }
                for n, c in count.most_common(ntags)]

def draw_cloud(tags, filename, fontname='Noto Sans CJK', size=(800, 600)):
    pytagcloud.create_tag_image(tags, filename, fontname=fontname, size=size)
    webbrowser.open(filename)

tags = get_tags(text)
print(tags)
draw_cloud(tags, 'wordcloud.png')