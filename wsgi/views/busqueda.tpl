% include('header.tpl', title='YouPlay')
<h1>Resultados de la b&uacute;squeda:</h1>
<ul>
% for video in misVideos: 
<div class="panel panel-primary">
	<div class="panel-heading">Titulo: {{video[1]}}</div>
	<h3>Contenido:</h3>
	<div class="panel-body"> 
		
			<img class="responsive img-circle" src="{{video[2]}}" />
			<br></br>
			<p><a class="btn btn-primary" href="enlaceVideo/{{video[0]}}">Enlace Al Video</a></p>
	</div>

</div>

<!-- -->
% end
</ul>
% include('footer.tpl')
