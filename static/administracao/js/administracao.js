// Funções para organização dos dados de formulários e criação de gráficos

document.addEventListener("DOMContentLoaded", function() {
  carregaQuestoes();
});

function salvaQuestoes() {
    $('#id_questao_60').val($('#select_questao_60').val());
    $('#id_questao_146').val($('#select_questao_146').val());
}

function carregaQuestoes() {
    var id_questao_146 = document.getElementById("id_questao_146").value;
    var select_questao_146 = document.getElementById("select_questao_146");
    
    console.log(id_questao_146);
    console.log(id_questao_146.length);
    
    for (var j = 0; j < id_questao_146.length; j++) {
        for (var i = 0; i < select_questao_146.length; i++) {
            if (select_questao_146[i].innerHTML == id_questao_146[j]) {
                select_questao_146[i].selected = true;
            }
        }
    }
}
