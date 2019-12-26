// Funções para o funcionamento do mapa de ações realizadas

function initMap() {
  var palmas = {lat: -10.244134, lng: -48.1920895};
  map = new google.maps.Map(document.getElementById('mapa-escolas'), {
    zoom: 11,
    center: palmas,
    // mapTypeId: google.maps.MapTypeId.SATELLITE,
  });
  setMarker(-10.156690000000000000, -48.328120000000000000, 'Escola municipal Luiz Gonzaga', '1.69', '503 Norte', 'Kanela', '1.66', 'Norte', '1.67', '1', ' 1.81');
  setMarker(-10.156270000000000000, -48.344930000000000000, 'Escola municipal Mestre Pacífico S. Campos', '2.64', '409 Norte', 'Kanela', '1.66', 'Norte', '1.67', '2', '  1.81');
  setMarker(-10.170240000000000000, -48.335380000000000000, 'Escola municipal de T.I. Padre Josimo M. Tavares', '0.87', '301 Norte', 'Kanela', '1.66', 'Norte', '1.67', '4', '  1.81');
  setMarker(-10.179730000000000000, -48.311120000000000000, 'Escola municipal Anne Frank', '1.62', '110 Norte', 'Apinajé', '1.70', 'Norte', '1.67', '5', '  1.81');
  setMarker(-10.194800000000000000, -48.310440000000000000, 'Escola municipal Henrique Talone Pinheiro', '1.72', '210 Sul', 'Xambioá', '2.95', 'Centro Sul', '1.84', '6', ' 1.81');
  setMarker(-10.331090000000000000, -48.320050000000000000, 'Escola municipal de T.I. Margarida Gonçalves', '0.92', 'Aureny I (Lago Sul)', 'Karajá', '1.56', 'Sul', '1.58', '8', '  1.81');
  setMarker(-10.265984971913538000, -48.323448640393850000, 'Escola municipal de T.I.Almirante Tamandare', '1.10', '1306 Sul', 'Krahô', '1.54', 'Centro Sul', '1.84', '62', ' 1.81');
  setMarker(-10.296330605057515000, -48.314563930034640000, 'Escola municipal de T.I. Anisio Spenola Teixeira', '2.05', 'Aureny IV(Bertavile)', 'Karajá', '1.56', 'Sul', '1.58', '63', '  1.81');
  setMarker(-10.358483851416153000, -48.188046813011170000, 'Escola Municipal de Tempo Integral Marcos Freire', '4.50', 'Walterly (T. Grande)', 'Pankararu', '3.57', 'Zona Rural', '3.57', '64', '  1.81');
  setMarker(-10.3320503, -48.2874656, 'Escola municipal de T.I. Caroline C. C. da Silva', '0.89', 'Santa Fé  2', 'Javaé', '1.85', 'Sul', '1.58', '61', '  1.81');
  setMarker(-10.3519378, -48.2949939, 'Escola municipal Professor Sávia F. Jacome', '3.03', 'Bela Vista', 'Javaé', '1.85', 'Sul', '1.58', '60', ' 1.81');
  setMarker(-10.2245109, -48.3208702, 'Escola municipal de T.I. Vinícius de Moraes', '2.27', '706 Sul', 'Xambioá', '2.95', 'Centro Sul', '1.84', '59', '  1.81');
  setMarker(-10.3121686, -48.3216785, 'Escola municipal de T.I. Euridice F. de Mello', '1.99', 'Aureny III(Taquaralto)', 'Xerente', '1.32', 'Sul', '1.58', '58', '  1.81');
  setMarker(-10.3274696, -48.3023334, 'Escola municipal Thiago Barbosa', '1.70', 'Aureny II(Taquaralto)', 'Karajá', '1.56', 'Sul', '1.58', '57', '  1.81');
  setMarker(-10.2843343, -48.1112861, 'Escola municipal de T.I. Sueli Pereira A. Reche', '2.24', 'Taquarussu', 'Pankararu', '3.57', 'Zona Rural', '3.57', '56', ' 1.81');
  setMarker(-10.1684416, -48.321987, 'Escola municipal de T.I. Monsenhor Pedro P. Piagem', '0.80', '404 Norte', 'Apinajé', '1.70', 'Norte', '1.67', '55', ' 1.81');
  setMarker(-10.341915, -48.2866555, 'Escola municipal Maria Rosa de Castro Sales', '2.40', 'Morada do Sol', 'Javaé', '1.85', 'Sul', '1.58', '54', '  1.81');
  setMarker(-10.3240285, -48.321423, 'Escola municipal Maria Júlia Amorim Rodrigues', '0.68', 'Aureny III(Taquaralto)', 'Xerente', '1.32', 'Sul', '1.58', '53', ' 1.81');
  setMarker(-10.2521439, -47.8883521, 'Escola municipal de T.I. Luiz Nunes de Oliveira', '3.18', 'Buritirana', 'Pankararu', '3.57', 'Zona Rural', '3.57', '52', ' 1.81');
  setMarker(-10.2477339, -48.2498216, 'Escola municipal de T.I. João Beltrão', '3.47', 'Walterly (T. Grande)', 'Pankararu', '3.57', 'Zona Rural', '3.57', '51', ' 1.81');
  setMarker(-10.3328327, -48.2978953, 'Escola municipal Jorge Amado', '1.17', 'Santa Fé', 'Javaé', '1.85', 'Sul', '1.58', '50', ' 1.81');
  setMarker(-10.239555, -48.3268826, 'Escola municipal Darcy Ribeiro', '3.55', '904 Sul', 'Xambioá', '2.95', 'Centro Sul', '1.84', '49', '  1.81');
  setMarker(-10.165243, -48.3083322, 'Escola municipal de T.I. Daniel Batista', '2.11', '508 Norte', 'Apinajé', '1.70', 'Norte', '1.67', '48', '  1.81');
  setMarker(-10.3167243, -48.1544495, 'Escola municipal Crispim Pereira de Alencar', '4.09', 'Taquarussu', 'Pankararu', '3.57', 'Zona Rural', '3.57', '47', ' 1.81');
  setMarker(-10.0317173, -48.3101651, 'Escola municipal de T.I. Aprigio T. de Matos', '2.10', 'Saida para lajeado(KM 17 - renda portuguesa)', 'Pankararu', '3.57', 'Zona Rural', '3.57', '46', '  1.81');
  setMarker(-10.317194, -48.3019974, 'Escola municipal Aurélio Buarque de Holanda', '1.62', 'Aureny I (Taquaralto)', 'Karajá', '1.56', 'Sul', '1.58', '45', ' 1.81');
  setMarker(-10.2517967, -48.3402742, 'Escola municipal Antônio G. de Carvalho Filho', '1.88', '1103 Sul', 'Krahô', '1.54', 'Centro Sul', '1.84', '44', ' 1.81');
  setMarker(-10.257200000000000000, -48.320970000000000000, 'Escola municipal Antônio Carlos Jobim', '1.56', '1206 Sul', 'Krahô', '1.54', 'Centro Sul', '1.84', '7', '  1.81');
  setMarker(-10.163180102001478000, -48.340374827384950000, 'Escola Municipal Beatriz Rodrigues da Silva', '1,81', '405 Norte', 'Kanela', '1.66', 'Norte', '1.67', '65', '  1.81');
}

function setMarker(latitude, longitude, nome, cpod, quadra, territorio, cpod_territorio, macrorregiao, cpod_macrorregiao, id, cidade) {
  var escola = {lat: latitude, lng: longitude};
  var marker = new google.maps.Marker({
    position: escola,
    map: map,
    title: nome,
    // label: nome,
  });
  
  google.maps.event.addDomListener(marker, 'click', function() {
    document.getElementById("portugues-nome").innerHTML = nome;
    document.getElementById("portugues-id").innerHTML = id + ': ';
    document.getElementById("portugues-cpod").innerHTML = 'CPO-D (escola): ' + cpod;
    document.getElementById("portugues-quadra").innerHTML = quadra + ', ';
    document.getElementById("portugues-territorio").innerHTML = territorio;
    document.getElementById("portugues-cpod-territorio").innerHTML = 'CPO-D (média/território): ' + cpod_territorio;
    document.getElementById("portugues-macrorregiao").innerHTML = macrorregiao + ', ';
    document.getElementById("portugues-cpod-macrorregiao").innerHTML = 'CPO-D (média/região): ' + cpod_macrorregiao;
    document.getElementById("portugues-cidade").innerHTML = 'CPO-D (média/cidade): ' + cidade;
    
    document.getElementById("ingles-nome").innerHTML = nome;
    document.getElementById("ingles-id").innerHTML = id + ': ';
    document.getElementById("ingles-cpod").innerHTML = 'CPO-D (school): ' + cpod;
    document.getElementById("ingles-quadra").innerHTML = quadra + ', ';
    document.getElementById("ingles-territorio").innerHTML = territorio;
    document.getElementById("ingles-cpod-territorio").innerHTML = 'CPO-D (mean/territory): ' + cpod_territorio;
    document.getElementById("ingles-macrorregiao").innerHTML = macrorregiao + ', ';
    document.getElementById("ingles-cpod-macrorregiao").innerHTML = 'CPO-D (mean/region): ' + cpod_macrorregiao;
    document.getElementById("ingles-cidade").innerHTML = 'CPO-D (mean/city): ' + cidade;
    
    // Abre o balão com o id sempre que o marker for clicado
    var contentString = id + ' - ' + nome;
    var infowindow = new google.maps.InfoWindow({
      content: contentString,
    });
    infowindow.open(map, marker);
  });
  
}
