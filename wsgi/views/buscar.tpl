% include('header.tpl', title='YouPlay')
    <center>
    <h1>Bienvenidos A YouPlay!!</h1>
    <h3> Por favor, introduce el nombre a tu vídeo favorito:</h3>
    
<form class="navbar-form navbar-center" role="search" action="/Busqueda" method="POST" >
  <div class="form-group">
    <input type="text" class="form-control" id="buscar" name="buscar"  />
  </div>
  <div class="form-group">
    <div class="checkbox">
      <label>
        <input type="checkbox" value="video" name="opciones" id="opcion1"/> Videos
      </label>
      <label>
        <input type="checkbox" value="lists" name="opciones" id="opcion2"/> Listas
        </label>
        <label>
        <input type="checkbox" value="channels" name="opciones" id="opcion3"/> Canales

      </label>
    </div>

  </div>
  <button type="submit" class="btn btn-primary">Buscar</button>
</form>
</center>

% include('footer.tpl')