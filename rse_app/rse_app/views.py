from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
import json
import sys
import os
import collections
import app_source
# from app_source.log_handler import QueryLog
# from app_source.indicators_handler import Indicators
import app_source.config as config
# from app_source.export_excel import ExportExcel
# from app_source.export_data import ExportData


def home(request):
	return render(request, 'home.html')

def visualization(request):
	return render(request, 'visualization.html')

def get_facets(request):
	print 'aqqui0'