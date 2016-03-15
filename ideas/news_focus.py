#-*- encoding: utf-8 -*-
from xml.dom.minidom import *
import urllib.request

tree = urllib.request.urlopen("http://rss.focus.de/fol/XML/rss_folnews_eilmeldungen.xml").read()

tree = parseString(tree)

title = tree.getElementsByTagName("title")



for tit in title:
    if str(tit.firstChild.data) != "FOCUS-Online-Eilmeldungen":
        print(str(tit.firstChild.data))
