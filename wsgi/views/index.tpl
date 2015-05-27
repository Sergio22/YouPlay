% include('header.tpl', title='YouPlay')
<html>

<body background="http://mayankagrawal.com/media/play_button.png">
   <div class="jumbotron text-center"> 
    <h1><u><strong>Bienvenidos A YouPlay!!</strong></u></h1>
    <br></br>
    <h4> Aquí, podéis buscar los vídeos, canales y listas de reproducción, que más os guste y disfrutar de ellos, gracias a la api de YouTube!!</h4> 
    <h4>También, podeis ver los detalles del video que más os guste antes de hacer clic para verlo. La información que nos muestra es la duración y una pequeña descripción del video</h4>
    <h4>A continuación, en el siguiente enlace podrán empezar a buscar los videos que más deseen!!</h4>
    <br></br>
    <h4> Haz click en "Comenzar:"</h4>

<div class="col-md-4 col-lg-4 col-md-offset-4 col-lg-offset-4 col-xs-12 col-sm-12">
    <a href="/buscar">
        <button type="button" class="btn btn-primary btn-lg btn-block">Comenzar</button>
    </a>
</div>
</div>
</body>
</html>


% include('footer.tpl')
