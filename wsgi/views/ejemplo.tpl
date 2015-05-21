% include('header.tpl', title='YouPlay')
<h1>Resultados de la b&uacute;squeda:</h1>

<h2>Videos:</h2>
% for item in items:
%if item["id"]["kind"] == "youtube#video":
<div class="panel panel-primary">
	<div class="panel-heading">
		Titulo: {{item["snippet"]["title"]}}
	</div>
	<div class="panel-body"> 
	<img class="responsive img-circle" src="{{item["snippet"]["thumbnails"]["default"]["url"]}}" />
			<br></br>
			<p><a class="btn btn-primary" href="enlaceVideo/{{item["id"]["videoId"]}}">Enlace Al Video</a></p>
	</div>

</div>
% end
% end
<h2>Canales:</h2>
<h2>Listas de reproducción:</h2>



% include('footer.tpl')
