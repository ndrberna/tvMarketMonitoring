
import sys
sys.path.append("./lib/python2.7/site-packages/")
from bs4 import BeautifulSoup
import urllib
import requests
import os
import subprocess
import time
import datetime

import pymongo
from pymongo import MongoClient
client = MongoClient()
db = client.MonitoraggioTV


def get_value(url,selector,keyword,shop):
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'lxml')
    numero_prodotti=(soup.select(selector)[0].text)
    posts = db.posts
    
    if shop=="SUBITO.IT":
        numero_prodotti = numero_prodotti.split(",")[1].replace("\n","").replace("u'","").replace(" ","")
    
    if shop=="eprice.it":
        numero_prodotti=int(numero_prodotti.split(" articoli")[0].replace("(","").replace(" ",""))
        
    if shop=="kijiji.it":
        try:
            numero_prodotti=int(numero_prodotti.split(" Annunci")[0].replace(" ",""))
        except:
            pass
        
    print keyword + " " + str(numero_prodotti)
    post_data = {
        'date': str(datetime.datetime.now().strftime("%d/%m/%y")),
        'url': url,
        'risultato': numero_prodotti,
        'keyword':keyword,
        'shop': shop
    }
    if not posts.find_one(post_data ):
        result = posts.insert_one(post_data)    




shop="kijiji.it"
selector="body > div.content.left-rail.srp > div.main-container > div.main > div.srp-hed > div > h2"

url="https://www.kijiji.it/dvb-t2/"
keyword="DVB-T2"
get_value(url,selector,keyword,shop)

url="https://www.kijiji.it/dvb-t/"
keyword="DVB-T"
get_value(url,selector,keyword,shop)

url="https://www.kijiji.it/hevc/"
keyword="HEVC"
get_value(url,selector,keyword,shop)

url="https://www.kijiji.it/dvb-t2+hevc"
keyword="DVB-T2 HEVC"
get_value(url,selector,keyword,shop)


shop="PREZZOFORTE"
selector="#col_prodotti_numero > span.lista_prodotti_numero_prodotti"

url="https://www.prezzoforte.it/advanced_search_result.php?keywords=dvb-t"
keyword="DVB-T"
get_value(url,selector,keyword,shop)

url="https://www.prezzoforte.it/advanced_search_result.php?keywords=dvb-t2"
keyword="DVB-T2"
get_value(url,selector,keyword,shop)

url="https://www.prezzoforte.it/advanced_search_result.php?keywords=hevc"
keyword="HEVC"
get_value(url,selector,keyword,shop)

url="https://www.prezzoforte.it/advanced_search_result.php?keywords=dvb-t2+hevc"
keyword="DVB-T2 HEVC"
get_value(url,selector,keyword,shop)



selector="#productList > div:nth-of-type(1) > section > div > b"
shop="EURONICS"

keyword="DVB-T2"
url="https://www.euronics.it/acquistaonline/tv-led/cat110016/?q="+keyword
get_value(url,selector,keyword,shop)

keyword="DVB-T"    
url="https://www.euronics.it/acquistaonline/tv-led/cat110016/?q="+keyword
get_value(url,selector,keyword,shop)

keyword="DVB-T2 HEVC"
url="https://www.euronics.it/acquistaonline/tv-led/cat110016/?q="+keyword
get_value(url,selector,keyword,shop)

keyword="HEVC"
url="https://www.euronics.it/acquistaonline/tv-led/cat110016/?q="+keyword
get_value(url,selector,keyword,shop)


url="https://it.aliexpress.com/wholesale?spm=a2g0y.search0104.1.1.kasRbE&SearchText=dvb-t2"
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'lxml')

numero_prodotti=(soup.select('#we-wholesale-search-list > div.bread-block-wrap > div > div > div.search-result > p > strong')[0].text)
posts = db.posts

post_data = {
    'date': str(datetime.datetime.now().strftime("%d/%m/%y")),
    'url': url,
    'risultato': numero_prodotti,
    'keyword':"DVB-T2",
    'shop': "Aliexpress"
}

print post_data
if not posts.find_one(post_data ):
    result = posts.insert_one(post_data)

url="https://it.aliexpress.com/wholesale?catId=0&SearchText=dvb-t"
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'lxml')
numero_prodotti=(soup.select('#we-wholesale-search-list > div.bread-block-wrap > div > div > div.search-result > p > strong')[0].text)

post_data = {
    'shop': "Aliexpress",
    'date': str(datetime.datetime.now().strftime("%d/%m/%y")),
    'url': url,
    'risultato': numero_prodotti,
    'keyword':"DVB-T"
}

print post_data
if not posts.find_one(post_data ):
    result = posts.insert_one(post_data)    
    
url="https://it.aliexpress.com/wholesale?catId=0&initiative_id=SB_20171129054255&SearchText=dvb-t2++hevc"
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'lxml')
numero_prodotti=(soup.select('#we-wholesale-search-list > div.bread-block-wrap > div > div > div.search-result > p > strong')[0].text)

post_data = {
    'shop': "Aliexpress",
    'date': str(datetime.datetime.now().strftime("%d/%m/%y")),
    'url': url,
    'risultato': numero_prodotti,
    'keyword':"DVB-T2 HEVC"
}

print post_data
if not posts.find_one(post_data ):
    result = posts.insert_one(post_data)    

    
url="https://it.aliexpress.com/wholesale?catId=0&SearchText=hevc"
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'lxml')
numero_prodotti=(soup.select('#we-wholesale-search-list > div.bread-block-wrap > div > div > div.search-result > p > strong')[0].text)

post_data = {
    'shop': "Aliexpress",
    'date': str(datetime.datetime.now().strftime("%d/%m/%y")),
    'url': url,
    'risultato': numero_prodotti,
    'keyword':"HEVC"
}

print post_data
if not posts.find_one(post_data ):
    result = posts.insert_one(post_data)



url="https://www.subito.it/annunci-italia/vendita/audio-video/?q=dvb-t2"
selector='#template_content > main > div.subcontent > div.main > div.listing > ul.list_link.large > li:nth-of-type(1)'

keyword="DVB-T2"
shop="SUBITO.IT"
get_value(url,selector,keyword,shop)

url="https://www.subito.it/annunci-italia/vendita/audio-video/?q=hevc"
keyword="HEVC"
get_value(url,selector,keyword,shop)
 
url="https://www.subito.it/annunci-italia/vendita/audio-video/?q=dvb-t"
keyword="DVB-T"
get_value(url,selector,keyword,shop)

url="https://www.subito.it/annunci-italia/vendita/audio-video/?q=dvb-t2+hevc"
keyword="DVB-T2 HEVC"
get_value(url,selector,keyword,shop)



shop="eprice.it"
selector='#breadcrumb > span.numRes'


url="https://www.eprice.it/search/qs=hevc?mets=hevc"
keyword="HEVC"
get_value(url,selector,keyword,shop)

url="https://www.eprice.it/search/qs=dvb%20t?mets=dvb%20t"
keyword="DVB-T"
get_value(url,selector,keyword,shop)

url="https://www.eprice.it/search/sp=/audio-video-elettronica/home-video?qs=dvb%20t2&oq=dvb%20t2"
keyword="DVB-T2"
get_value(url,selector,keyword,shop)
