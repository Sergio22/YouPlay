# -*- coding: UTF-8 -*-
import requests, json

API_KEY = 'AIzaSyDdIpBtl23FbaOSOGz7YwsyViA5jIhpNZ4'

def busqueda_g(busqueda,opciones):
	query_part = {'part':["id,snippet"],'type':opciones,'maxResults':25,'q':busqueda,'key':API_KEY}
	request_mont = requests.get('https://www.googleapis.com/youtube/v3/search',params=query_part)
	jresp = json.loads(request_mont.text)
	return jresp

def	busqueda_next(busqueda,pageid,result_index):
	query_part = {'part':["id,snippet"],'pageToken':pageid,'maxResults':25,'q':busqueda,'key':API_KEY}
	request_mont = requests.get('https://www.googleapis.com/youtube/v3/search',params=query_part)
	jresp = json.loads(request_mont.text)
	jresp["numPag"]=result_index
	return jresp