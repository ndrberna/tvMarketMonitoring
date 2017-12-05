# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import csv
from django.shortcuts import render_to_response, render, redirect
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from time import sleep
import pandas as pd
import os
from collections import Counter
import math
import datetime
import time
import pymongo
from pymongo import MongoClient
client = MongoClient()
db = client.MonitoraggioTV
posts = db.posts
# Create your views here.
def mappa(request):
	

	data = pd.DataFrame(list(posts.find()))
	data.reset_index()
	data["keyword"] = data["keyword"].apply(lambda x: str(x).replace("\n","").encode("utf-8"))
	data["risultato"] = data["risultato"].apply(lambda x: int(str(x).replace(",","")))
	data["date"] = pd.to_datetime(data['date'].values, format='%d/%m/%y')
	
	today = datetime.date.today()
	shop = request.GET.get('shop', None)
	keyword= request.GET.get('keyword', None)
	date= request.GET.get('date', None)
	print shop, today,keyword
	
	raw_data=data.values.tolist()

	print "RES",data[(data["keyword"]==keyword)]

	if date:
		raw_data=data[(data["date"]==date)].values.tolist()

	if shop and keyword:
		print "*****"
		print keyword
		print shop
		
		raw_data=data[(data["shop"]==shop)&(data["keyword"]==keyword)].values.tolist()
		print raw_data

	if shop and not keyword:
		raw_data=data[(data["shop"]==shop)].values.tolist()

	if not shop and keyword:
		raw_data=data[(data["keyword"]==keyword)].values.tolist()
		
	
	new_date=[]
	for j in data.date.unique():
		new_date.append(str(j).split("T")[0])


	print new_date	
	context = {
	'raw_data':raw_data,
	'keyword':data.keyword.unique(),
	'date':new_date,
	'negozi':data.shop.unique(),
	}
	return render_to_response('marketPresence/mappa.html',context)


















