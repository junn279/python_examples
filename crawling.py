# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import re

address = "http://edition.cnn.com/specials/cnn-10---archive"
host_prefix = "http://edition.cnn.com"

def loadHTML (url):
    try:
        html = urllib2.urlopen(url)
    except urllib2.HTTPError as e:
        print(e)
        return -1
    else:
        # except 절에서 return이나 break를 사용했다면 이 절은 필요 없다
        bsObj = BeautifulSoup(html.read(), "html.parser")
        return bsObj

def findGupta(url):
    bsObj = loadHTML(url)
    paragraphList = bsObj.findAll("div",{"class":"zn-body__paragraph"},text=re.compile('[Gg][Uu][Pp][Tt][Aa]'))
    print("Count : " + str(len(paragraphList)))
    for paragraph in paragraphList:
        print(paragraph.get_text())

    return 0

bsObj = loadHTML(address)
print(bsObj)
nameList = bsObj.findAll("span",{"class":"cd__headline-text"})

print("### Start ###")
for name in nameList:
    print("@@ " + name.get_text() + " @@")
    findGupta(host_prefix + name.parent.attrs["href"])
