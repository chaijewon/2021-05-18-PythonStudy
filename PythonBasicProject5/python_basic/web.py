#-*- coding:utf-8 -*-
import urllib.request as req
from bs4 import BeautifulSoup
import requests
import sqlite3
import ssl
ssl._create_default_https_context=ssl._create_unverified_context
'''
def request(url):
    response=req.urlopen(url)
    byte_data=response.read()
    text_data=byte_data.decode('utf-8')
    return text_data
url='https://www.10000recipe.com/recipe/list.html?order=reco&page=2'
webpage=request(url)
#print(webpage)
'''
'''
  <div class="common_sp_thumb">
                    <a href="/recipe/6958074" class="common_sp_link">
                                                <img src="https://recipe1.ezmember.co.kr/cache/recipe/2021/05/09/5c094213de089bcc1f1574ec7d3b007b1_m.jpg">
                    </a>
                </div>
'''
url='https://www.10000recipe.com/recipe/list.html?order=reco&page=2'
res=req.urlopen(url)
soup=BeautifulSoup(res,'html.parser')
aList=soup.select('div.common_sp_thumb > a > img')
for img inaList
