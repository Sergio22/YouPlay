from bottle import route,run,template,view,static_file,get, post,request

import httplib2
import os
import sys

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser



DEVELOPER_KEY = "AIzaSyDdIpBtl23FbaOSOGz7YwsyViA5jIhpNZ4"

playlists = []
videos = []
channels = []
@route('/Busqueda', method='POST')
@view('busqueda')
def busqueda():
	
	
	busqueda = request.forms.get('buscar')
	#argparser.add_argument("--q", help="Search term", default=busqueda)
	#
	#args = argparser.parse_args()
	try:
		youtube_search(busqueda)
	except HttpError, e:
		print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
	return dict(misVideos=videos)

	



# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(busqueda):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=busqueda,#options.q,
    part="id,snippet",
    maxResults=25
  ).execute()
 

  # Add each result thumbnails'to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    print search_result, "\n"
   
    if search_result["id"]["kind"] == "youtube#video":
      video = []
      video.append(search_result["id"]["videoId"]) 
      video.append(search_result["snippet"]["title"])
      video.append(search_result["snippet"]["thumbnails"]["default"]["url"])
      videos.append(video)	
    elif search_result["id"]["kind"] == "youtube#channel":
      channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                   search_result["id"]["channelId"]))
    elif search_result["id"]["kind"] == "youtube#playlist":
      playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                                    search_result["id"]["playlistId"]))


 
 # print "Videos:\n", "\n".join(videos), "\n"
  print "Channels:\n", "\n".join(channels), "\n"
  print "Playlists:\n", "\n".join(playlists), "\n"



@route('/enlaceVideo/<id>')
@view('index')
def enlaceVideo(id):
  lista =  ["objeto uno", "objeto dos", "objeto tres"]
  lista.append(id)
  return dict(user='sergio', miLista = lista) 