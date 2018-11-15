// Funções para organização dos dados de formulários e criação de gráficos

document.addEventListener("DOMContentLoaded", function() {
  carregaQuestoes();
});

function salvaQuestoes() {
    $('#id_questao_60').val($('#select_questao_60').val());
    $('#id_questao_146').val($('#select_questao_146').val());
}

function carregaQuestoes() {
    // Carrega a questão 60
    var questao_60 = JSON.parse("[" + document.getElementById("id_questao_60").value + "]");
    var select_questao_60 = document.getElementById("select_questao_60");
    
    for (var i = 0; i < questao_60.length; i++) {
        select_questao_60[questao_60[i]].selected = true;
    }
    
    // Carrega a questão 146
    var questao_146 = JSON.parse("[" + document.getElementById("id_questao_146").value + "]");
    var select_questao_146 = document.getElementById("select_questao_146");
    
    for (var i = 0; i < questao_146.length; i++) {
        select_questao_146[questao_146[i]].selected = true;
    }
}
