# coding: UTF-8
import csv
import urllib2
import re
import requests
from bs4 import BeautifulSoup
import sys

args = sys.argv
bid = args[1]

def get_entry_list(html):
    url_list = [html]
    while True:
        html = requests.get(html).content
        soup = BeautifulSoup(html, "html.parser")
        next_page = soup.find("a", {"class", "skinSimpleBtn pagingNext"})
        if isinstance(next_page, type(None)):
            #print("finish")
            return url_list
        else:
            url_list.append(next_page["href"])
            html = next_page["href"]


blog_id = bid
url = "http://ameblo.jp/{0}/entrylist.html".format(blog_id)

all_entry_list = get_entry_list(url)

times = []
for entry in all_entry_list:
   try:
      # アクセスするURL
      url = entry

      # URLにアクセスする htmlが帰ってくる
      html = urllib2.urlopen(url)

      # htmlをBeautifulSoupで扱う
      soup = BeautifulSoup(html, "html.parser")

      timelist = soup.find_all("time")

      for time in timelist:
         times.append(time.string)

   except urllib2.HTTPError, e:
      print(e.code)
      print(e.reason)
      print(e.read())

f = open(bid + '_time.txt', 'w')
f.write("\n".join(times))
f.close()

