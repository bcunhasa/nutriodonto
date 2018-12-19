// Funções para o funcionamento do mapa que exibe a localização da UFT

function initMap() {
  var uft = {lat: -10.1771255, lng: -48.3617526};
  map = new google.maps.Map(document.getElementById('uft'), {
    zoom: 15,
    center: uft,
    mapTypeId: google.maps.MapTypeId.HYBRID,
  });
  setMarker(-10.1771255, -48.3617526, 'Fábrica de Software');
}

function setMarker(latitude, longitude, nome) {
  var escola = {lat: latitude, lng: longitude};
  var marker = new google.maps.Marker({
    position: escola,
    map: map,
    title: nome
  });
}
