// Funções para o funcionamento dos mapas de seleção de localização

function initMap() {
  var palmas = {lat: -10.1846246, lng: -48.3336719};
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 13,
    center: palmas
  });
  
  setMarker(-10.2572, -48.32097, 'Escola municipal Antônio Carlos Jobim');
  setMarker(-10.21249, -48.33196, 'Escola municipal Antônio G. de Carvalho Filho');
  setMarker(-10.17973, -48.31112, 'Escola municipal Anne Frank');
  setMarker(-10.23955, -48.32688, 'Escola municipal Darcy Ribeiro');
  setMarker(-10.1948, -48.31044, 'Escola municipal Henrique Talone Pinheiro');
  setMarker(-10.22451, -48.32087, 'Escola municipal de T.I. Vinícius de Moraes');
  setMarker(-10.16359, -48.34067, 'Escola municipal Beatriz Rodrigues da Silva');
  setMarker(-10.15627, -48.34493, 'Escola municipal Mestre Pacífico S. Campos');
  setMarker(-10.15669, -48.32812, 'Escola municipal Luiz Gonzaga');
  setMarker(-10.17024, -48.33538, 'Escola municipal de T.I. Padre Josimo M. Tavares');
  setMarker(-10.16524, -48.30833, 'Escola municipal de T.I. Daniel Batista');
  setMarker(-10.16844, -48.32198, 'Escola municipal de T.I. Monsenhor Pedro P. Piagem');
  setMarker(-10.33283, -48.29789, 'Escola municipal Jorge Amado');
  setMarker(-10.33736, -48.28876, 'Escola municipal Maria Rosa de Castro Sales');
  setMarker(-10.24816, -48.32934, 'Escola municipal Professor Sávia F. Jacome');
  setMarker(-10.33205, -48.28746, 'Escola municipal de T.I. Caroline C. C. da Silva');
  setMarker(-10.31719, -48.30199, 'Escola municipal Aurélio Buarque de Holanda');
  setMarker(-10.32412, -48.32161, 'Escola municipal Maria Júlia Amorim Rodrigues');
  setMarker(-10.32741, -48.30232, 'Escola municipal Thiago Barbosa');
  setMarker(-10.31216, -48.32167, 'Escola municipal de T.I. Euridice F. de Mello');
  setMarker(-10.33109, -48.32005, 'Escola municipal de T.I. Margarida Gonçalves');
  setMarker(-10.33426, -48.30523, 'Escola municipal Crispim Pereira de Alencar');
  setMarker(-10.05347, -48.31731, 'Escola municipal de T.I. Aprigio T. de Matos');
  setMarker(-10.24773, -48.24982, 'Escola municipal de T.I. João Beltrão');
  setMarker(-10.25216, -47.88829, 'Escola municipal de T.I. Luiz Nunes de Oliveira');
  setMarker(-10.28433, -48.11128, 'Escola municipal de T.I. Sueli Pereira A. Reche');
}

function setMarker(latitude, longitude, nome) {
  var escola = {lat: latitude, lng: longitude};
  var marker = new google.maps.Marker({
    position: escola,
    map: map,
    title: nome
  });
}
