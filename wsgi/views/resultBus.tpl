% include('header.tpl', title='YouPlay')
<body background="http://mayankagrawal.com/media/play_button.png">
<script>

function llamardatos(id){
	$.get ("../getVideoStatics/"+id,function(data){
		var info=data.items[0];
	
	

		$('.Duracion').html(info.contentDetails.duration);
		$('.Descripcion').html(info.snippet.description);
	});
}
    
  $(document).ready(function(){ 
    $('.botonAccion').bind('click',function(e){
    	var id = $(this).attr('name');

    	

    	llamardatos(id);
    });
  //  function(){
  //  
});
</script>
<h1><font color= red>Resultados de la b&uacute;squeda:</font color></h1>


<h2><font color= blue>Videos:</font color></h2>
%if 'numPag' in vars():
%if int(numPag)>0:
	<p><font color= blue> Mostrando resultados {{numPag-24}} - {{numPag}} de {{pageInfo['totalResults']}} resultados </font color></p>
%else:
<p> Se han encontrado {{pageInfo['totalResults']}} resultados </p>
%end
%else:
<p> Se han encontrado {{pageInfo['totalResults']}} resultados </p>
%end
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
			<button class="botonAccion btn btn-primary" name="{{item["id"]["videoId"]}}" type="button" data-toggle="collapse" data-target="#{{item["id"]["videoId"]}}" aria-expanded="false" aria-controls="collapseExample" >Ver detalles del vídeo</button>
  <div class="collapse" id="{{item["id"]["videoId"]}}">
  <div class="well">
    <p><strong>Duracion</strong><span class="Duracion"></span></p>
    <p><strong>Descripcion</strong><span class="Descripcion"></span></p>
    <p><strong></strong><span class=""></span></p>
    <p><strong></strong><span class=""></span></p>
  </div>
</div>


	</div>



</div>
% end
% end
<h2><font color= blue>Canales:</font color></h2>
% for item in items:
%if item["id"]["kind"] == "youtube#channel":
<div class="panel panel-primary">
	<div class="panel-heading">
		Titulo: {{item["snippet"]["title"]}}
	</div>
	<div class="panel-body"> 
	<img class="responsive img-circle" src="{{item["snippet"]["thumbnails"]["default"]["url"]}}" />
			<br></br>
			<p><a class="btn btn-primary" href="enlaceVideo/{{item["id"]["channelId"]}}">Enlace Al Canal</a></p>
	</div>

</div>
% end
% end
<h2><font color= blue>Listas de reproducción:</font color></h2>
% for item in items:
%if item["id"]["kind"] == "youtube#playlist":
<div class="panel panel-primary">
	<div class="panel-heading">
		Titulo: {{item["snippet"]["title"]}}
	</div>
	<div class="panel-body"> 
	<img class="responsive img-circle" src="{{item["snippet"]["thumbnails"]["default"]["url"]}}" />
			<br></br>
			<p><a class="btn btn-primary" href="enlaceVideo/{{item["id"]["playlistId"]}}">Enlace Al Video</a></p>
	</div>

</div>
% end
% end
<a class="btn btn-primary" href="../nextPage/{{nextPageToken}}">Resultados Siguientes</a>
% if 'prevPageToken' in vars():
<a class="btn btn-primary" href="../prevPage/{{prevPageToken}}">Resultados anteriores</a>
% else:
<a class="btn btn-primary disabled" href="">Resultados anteriores</a>
% end
% include('footer.tpl')