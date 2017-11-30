# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import csv
from django.shortcuts import render_to_response, render, redirect
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from time import sleep

import os
from collections import Counter
import math

import time
# Create your views here.
def mappa(request):
	
	return render_to_response('marketPresence/mappa.html')