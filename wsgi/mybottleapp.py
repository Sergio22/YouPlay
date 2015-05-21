from bottle import route,run,template,view,static_file,get, post, request,default_app
import requests
import os
import json
from bottle import TEMPLATE_PATH
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
#TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

#from oauth2client.client import flow_from_clientsecrets
API_KEY = 'AIzaSyDdIpBtl23FbaOSOGz7YwsyViA5jIhpNZ4'

@route('/')
def index():
	return  template('index.tpl')
	


@route('/buscar')
@view('buscar')
def buscar():
	return 

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')



# This must be added in order to do correct path lookups for the views

#import busqueda
@route('/Busqueda', method='POST')
@view('ejemplo')
def busqueda():
	busqueda = request.forms.get('buscar')
	opciones = request.forms.getlist('opciones')
	query_part = {'part':["id,snippet"],'type':opciones,'q':busqueda,'key':API_KEY}
	request_mont = requests.get('https://www.googleapis.com/youtube/v3/search',params=query_part)
	jresp = json.loads(request_mont.text,object_pairs_hook=dict)
	print jresp
	return jresp
'''	q_sf = {'id':"7lCDEYXw3mM",'key':"AIzaSyDdIpBtl23FbaOSOGz7YwsyViA5jIhpNZ4",'part':["snippet","contentDetails","statistics","status"]}
	r_sf = requests.get('https://www.googleapis.com/youtube/v3/videos',params=q_sf)
	jresp = json.loads(r_sf.text,object_pairs_hook=dict)
	print jresp
	return jresp '''


@route('/enlaceVideo/<id>')
@view('video')
def enlaceVideo(id): 
  return dict(video=id)




ON_OPENSHIFT = False
if os.environ.has_key('OPENSHIFT_REPO_DIR'):
	ON_OPENSHIFT = True
if ON_OPENSHIFT:
	TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_HOMEDIR'],'app-root/repo/wsgi/views/'))
	application=default_app()
else:
	run(host='localhost', port=8080)



