# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.safestring import mark_safe
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
	chiave_data=request.GET.get('date', None)
	raw_data=data.values.tolist()

	print "RES",data[(data["keyword"]==keyword)]

	lista_giorno_dvb_t=[]
	new_date=[]
	dataviz=0

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
		
	
	for j in data.date.unique():
			new_date.append(str(j).split("T")[0])
			ts = pd.to_datetime(str(j)) 
			d = ts.strftime('%Y/%m/%d')
			lista_giorno_dvb_t.append(d.encode('ascii'))

	if shop:
		dataviz=1
		lista_negozio_dvb_t=[]
		lista_keyword_dvb_t=[]
		lista_number_dvb_t=[]

		lista_negozio_dvb_t2=[]
		lista_keyword_dvb_t2=[]
		lista_number_dvb_t2=[]

		lista_negozio_dvb_t2_hevc=[]
		lista_keyword_dvb_t2_hevc=[]
		lista_number_dvb_t2_hevc=[]

		lista_negozio_hevc=[]
		lista_keyword_hevc=[]
		lista_number_hevc=[]
		lista_giorno_dvb_t=[]
		new_date=[]
		for j in data[(data["shop"]==shop)].date.unique():
			new_date.append(str(j).split("T")[0])
			ts = pd.to_datetime(str(j)) 
			d = ts.strftime('%Y/%m/%d')
			lista_giorno_dvb_t.append(d.encode('ascii'))

		for i in raw_data:
			if (i[2]=="DVB-T"):	
				lista_keyword_dvb_t.append(i[2])
				lista_number_dvb_t.append(i[3])
				lista_negozio_dvb_t.append(i[4])
			if (i[2]=="DVB-T2"):	
				lista_keyword_dvb_t2.append(i[2])
				lista_number_dvb_t2.append(i[3])
				lista_negozio_dvb_t2.append(i[4])
			if (i[2]=="HEVC"):	
				lista_keyword_hevc.append(i[2])
				lista_number_hevc.append(i[3])
				lista_negozio_hevc.append(i[4])
			if (i[2]=="DVB-T2 HEVC"):	
				lista_keyword_dvb_t2_hevc.append(i[2])
				lista_number_dvb_t2_hevc.append(i[3])
				lista_negozio_dvb_t2_hevc.append(i[4])
			
		print lista_giorno_dvb_t,lista_number_dvb_t

		context = {
		'raw_data':raw_data,
		'keywords':data.keyword.unique(),
		'date':new_date,
		'negozi':data.shop.unique(),
		'shop':shop,
		'keyword':keyword,
		'lista_negozio_dvb_t':lista_negozio_dvb_t,
		'lista_number_dvb_t':lista_number_dvb_t,
		'lista_keyword_dvb_t':lista_keyword_dvb_t,
		'lista_giorno_dvb_t':mark_safe(lista_giorno_dvb_t),

		'lista_negozio_dvb_t2':lista_negozio_dvb_t2,
		'lista_number_dvb_t2':lista_number_dvb_t2,
		'lista_keyword_dvb_t2':lista_keyword_dvb_t2,
		
		'lista_negozio_dvb_t2_hevc':lista_negozio_dvb_t2_hevc,
		'lista_number_dvb_t2_hevc':lista_number_dvb_t2_hevc,
		'lista_keyword_dvb_t2_hevc':lista_keyword_dvb_t2_hevc,

		'lista_negozio_hevc':lista_negozio_hevc,
		'lista_number_hevc':lista_number_hevc,
		'lista_keyword_hevc':lista_keyword_hevc,
		'dataviz':dataviz,
		'chiave_data':chiave_data
		}
		return render_to_response('marketPresence/mappa.html',context)


	context = {
		'raw_data':raw_data,
		
		'date':new_date,
		'negozi':data.shop.unique(),
		'dataviz':dataviz,
		'keywords':data.keyword.unique(),
		'shop':shop,
		'keyword':keyword,
		'chiave_data':chiave_data

		}
	return render_to_response('marketPresence/mappa.html',context)















