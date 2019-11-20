// Funções para o funcionamento dos mapas de seleção de localização

function initMap() {
  var palmas = {lat: -10.1846246, lng: -48.3336719};
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 14,
    center: palmas
  });
  
  google.maps.event.addListener(map, 'click', function(event) {
    clearMarkers();
    addMarker(event.latLng, map);
  });
}

function addMarker(location, map) {
  marker = new google.maps.Marker({
    position: location,
    map: map
  });
  document.getElementById("id_latitude").value = marker.getPosition().lat();
  document.getElementById("id_longitude").value = marker.getPosition().lng();
}

function clearMarkers() {
  if (typeof marker !== 'undefined') {
    marker.setMap(null);
  }
}
