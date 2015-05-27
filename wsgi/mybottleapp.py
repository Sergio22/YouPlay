# -*- coding: UTF-8 -*-
from bottle import route,run,template,view,static_file,get, post, request,response,default_app
import os
import json
from bottle import TEMPLATE_PATH
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from functions import busqueda_g, busqueda_next,getVideoStats

API_KEY = 'AIzaSyDdIpBtl23FbaOSOGz7YwsyViA5jIhpNZ4'

@route('/')
def index():
	return  template('index.tpl')
	
#Enrutador a la ruta estática
@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/buscar')
@view('buscar')
def buscar():
	return

@route('/resultBus', method='POST')
@view('resultBus')
def busqueda():
	busqueda = request.forms.get('buscar')
	opciones = request.forms.getlist('opciones')
	response.set_cookie("busqueda", busqueda,path="/")
	response.set_cookie("result_index",str(25),path="/")
	return busqueda_g(busqueda,opciones)
'''	q_sf = {'id':"7lCDEYXw3mM",'key':"AIzaSyDdIpBtl23FbaOSOGz7YwsyViA5jIhpNZ4",'part':["snippet","contentDetails","statistics","status"]}
	r_sf = requests.get('https://www.googleapis.com/youtube/v3/videos',params=q_sf)
	jresp = json.loads(r_sf.text,object_pairs_hook=dict)
	print jresp
	return jresp '''


@route('/enlaceVideo/<id>')
@view('video')
def enlaceVideo(id): 
  return dict(video=id)

@route('/nextPage/<pageid>')
@view('resultBus')
def nexPage(pageid):
	busqueda = request.get_cookie("busqueda")
	result_index=int(request.cookies.get("result_index"))
	result_index += 25
	response.set_cookie("result_index",str(result_index),path="/")
	return busqueda_next(busqueda,pageid,result_index)

@route('/prevPage/<pageid>')
@view('resultBus')
def nexPage(pageid):
	busqueda = request.get_cookie("busqueda")
	result_index=int(request.cookies.get("result_index"))
	if result_index > 0:
		result_index -= 25
	response.set_cookie("result_index",str(result_index),path="/")
	return busqueda_next(busqueda,pageid,result_index)

@route('/busquedaDefault')
@view('resultBus')
def defaultBus():
	busqueda = ""
	opciones = ["videos"]
	response.set_cookie("result_index",str(25),path="/")
	return busqueda_g(busqueda,opciones)

@route('/getVideoStatics/<id>')
def getVideoStatics(id): 
	return getVideoStats(id)

ON_OPENSHIFT = False
if os.environ.has_key('OPENSHIFT_REPO_DIR'):
	ON_OPENSHIFT = True
if ON_OPENSHIFT:
	TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_HOMEDIR'],'app-root/repo/wsgi/views/'))
	application=default_app()
else:
	run(host='localhost', port=8080)

