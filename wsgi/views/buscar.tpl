% include('header.tpl', title='YouPlay')
<div class="jumbotron text-center"> 
    <h1>Bienvenidos A YouPlay!!</h1>
    <h3> Por favor, introduce el nombre de tu vídeo favorito:</h3>
    
<form class="navbar-form navbar-center" role="search" action="/resultBus" method="POST" >
  <div class="form-group espacingv">
    <input type="text" class="form-control" id="buscar" name="buscar"  />
     <button type="submit" class="btn btn-primary">Buscar</button>
  </div>
<div>
  <div class="form-group">
    <div class="checkbox">
      <label>
        <input type="checkbox" value="video" name="opciones" id="opcion1" checked/> Videos
      </label>
      <label>
        <input type="checkbox" value="playlist" name="opciones" id="opcion2"/> Listas
        </label>
        <label>
        <input type="checkbox" value="channel" name="opciones" id="opcion3"/> Canales

      </label>
    </div>

  </div>
 </div>
</form>
</div>
% include('footer.tpl')