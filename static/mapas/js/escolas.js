// Funções para o funcionamento do mapa de ações realizadas

function initMap() {
  var palmas = {lat: -10.244134, lng: -48.1920895};
  map = new google.maps.Map(document.getElementById('mapa-escolas'), {
    zoom: 11,
    center: palmas,
    // mapTypeId: google.maps.MapTypeId.SATELLITE,
  });
  setMarker(-10.156690000000000000, -48.328120000000000000, 'Escola municipal Luiz Gonzaga', '1.69', '0', '503 Norte', 'Kanela', 'Norte', '1',);
  setMarker(-10.156270000000000000, -48.344930000000000000, 'Escola municipal Mestre Pacífico S. Campos', '2.64', '0', '409 Norte', 'Kanela', 'Norte', '2',);
  setMarker(-10.170240000000000000, -48.335380000000000000, 'Escola municipal de T.I. Padre Josimo M. Tavares', '0.87', '0', '301 Norte', 'Kanela', 'Norte', '4',);
  setMarker(-10.179730000000000000, -48.311120000000000000, 'Escola municipal Anne Frank', '1.62', '0', '110 Norte', 'Apinajé', 'Norte', '5',);
  setMarker(-10.194800000000000000, -48.310440000000000000, 'Escola municipal Henrique Talone Pinheiro', '1.72', '0', '210 Sul', 'Xambioá', 'Centro Sul', '6',);
  setMarker(-10.331090000000000000, -48.320050000000000000, 'Escola municipal de T.I. Margarida Gonçalves', '0.92', '0', 'Aureny I (Lago Sul)', 'Karajá', 'Sul', '8',);
  setMarker(-10.265984971913538000, -48.323448640393850000, 'Escola municipal de T.I.Almirante Tamandare', '1.10', '0', '1306 Sul', 'Krahô', 'Centro Sul', '62');
  setMarker(-10.296330605057515000, -48.314563930034640000, 'Escola municipal de T.I. Anisio Spenola Teixeira', '2.05', '0', 'Aureny IV(Bertavile)', 'Karajá', 'Sul', '63');
  setMarker(-10.358483851416153000, -48.188046813011170000, 'Escola Municipal de Tempo Integral Marcos Freire', '4.50', '0', 'Walterly (T. Grande)', 'Pankararu', 'Zona Rural', '64');
  setMarker(-10.3320503, -48.2874656, 'Escola municipal de T.I. Caroline C. C. da Silva', '0.89', '0', 'Santa Fé  2', 'Javaé', 'Sul', '61');
  setMarker(-10.3519378, -48.2949939, 'Escola municipal Professor Sávia F. Jacome', '3.03', '0', 'Bela Vista', 'Javaé', 'Sul', '60');
  setMarker(-10.2245109, -48.3208702, 'Escola municipal de T.I. Vinícius de Moraes', '2.27', '0', '706 Sul', 'Xambioá', 'Centro Sul', '59');
  setMarker(-10.248554, -48.330413, 'Escola municipal de T.I. Euridice F. de Mello', '1.99', '0', 'Aureny III(Taquaralto)', 'Xerente', 'Sul', '58');
  setMarker(-10.3274696, -48.3023334, 'Escola municipal Thiago Barbosa', '1.70', '0', 'Aureny II(Taquaralto)', 'Karajá', 'Sul', '57');
  setMarker(-10.2843343, -48.1112861, 'Escola municipal de T.I. Sueli Pereira A. Reche', '2.24', '0', 'Taquarussu', 'Pankararu', 'Zona Rural', '56');
  setMarker(-10.1684416, -48.321987, 'Escola municipal de T.I. Monsenhor Pedro P. Piagem', '0.80', '0', '404 Norte', 'Apinajé', 'Norte', '55');
  setMarker(-10.341915, -48.2866555, 'Escola municipal Maria Rosa de Castro Sales', '2.40', '0', 'Morada do Sol', 'Javaé', 'Sul', '54');
  setMarker(-10.3240285, -48.321423, 'Escola municipal Maria Júlia Amorim Rodrigues', '0.68', '0', 'Aureny III(Taquaralto)', 'Xerente', 'Sul', '53');
  setMarker(-10.2521439, -47.8883521, 'Escola municipal de T.I. Luiz Nunes de Oliveira', '3.18', '0', 'Buritirana', 'Pankararu', 'Zona Rural', '52');
  setMarker(-10.2477339, -48.2498216, 'Escola municipal de T.I. João Beltrão', '3.47', '0', 'Walterly (T. Grande)', 'Pankararu', 'Zona Rural', '51');
  setMarker(-10.3328327, -48.2978953, 'Escola municipal Jorge Amado', '1.17', '0', 'Santa Fé', 'Javaé', 'Sul', '50');
  setMarker(-10.239555, -48.3268826, 'Escola municipal Darcy Ribeiro', '3.55', '0', '904 Sul', 'Xambioá', 'Centro Sul', '49');
  setMarker(-10.165243, -48.3083322, 'Escola municipal de T.I. Daniel Batista', '2.11', '0', '508 Norte', 'Apinajé', 'Norte', '48');
  setMarker(-10.3167243, -48.1544495, 'Escola municipal Crispim Pereira de Alencar', '4.09', '0', 'Taquarussu', 'Pankararu', 'Zona Rural', '47');
  setMarker(-10.0317173, -48.3101651, 'Escola municipal de T.I. Aprigio T. de Matos', '2.10', '0', 'Saida para lajeado(KM 17 - renda portuguesa)', 'Pankararu', 'Zona Rural', '46');
  setMarker(-10.317194, -48.3019974, 'Escola municipal Aurélio Buarque de Holanda', '1.62', '0', 'Aureny I (Taquaralto)', 'Karajá', 'Sul', '45');
  setMarker(-10.2517967, -48.3402742, 'Escola municipal Antônio G. de Carvalho Filho', '1.88', '0', '1103 Sul', 'Krahô', 'Centro Sul', '44');
  setMarker(-10.257200000000000000, -48.320970000000000000, 'Escola municipal Antônio Carlos Jobim', '1.56', '0', '1206 Sul', 'Krahô', 'Centro Sul', '7',);
  setMarker(-10.163180102001478000, -48.340374827384950000, 'Escola Municipal Beatriz Rodrigues da Silva',  '1,81', '0', '405 Norte', 'Kanela', 'Norte', '65');
}

function setMarker(latitude, longitude, nome, cpod, periodontal, quadra, territorio, macrorregiao, id) {
  var escola = {lat: latitude, lng: longitude};
  var marker = new google.maps.Marker({
    position: escola,
    map: map,
    title: nome,
    // label: nome,
  });
  
  google.maps.event.addDomListener(marker, 'click', function() {
    document.getElementById("escola-nome").innerHTML = nome;
    document.getElementById("escola-id").innerHTML = id;
    document.getElementById("escola-cpod").innerHTML = cpod;
    document.getElementById("escola-periodontal").innerHTML = periodontal;
    document.getElementById("escola-quadra").innerHTML = quadra;
    document.getElementById("escola-territorio").innerHTML = territorio;
    document.getElementById("escola-macrorregiao").innerHTML = macrorregiao;
    
    // Abre o balão com o id sempre que o marker for clicado
    var contentString = id + ' - ' + nome;
    var infowindow = new google.maps.InfoWindow({
      content: contentString,
    });
    infowindow.open(map, marker);
  });
  
}
