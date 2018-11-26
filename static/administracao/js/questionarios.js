/* Arquivo que controla as configurações das páginas de coleta de questionários */

document.addEventListener("DOMContentLoaded", function() {
  carregaQuestoes();
});

function salvaQuestoes() {
    $('#id_questao_1').val($('#select_questao_1').val());
    $('#id_questao_3').val($('#select_questao_3').val());
    $('#id_questao_28').val($('#select_questao_28').val());
    $('#id_questao_31').val($('#select_questao_31').val());
    $('#id_questao_33').val($('#select_questao_33').val());
    $('#id_questao_37').val($('#select_questao_37').val());
    $('#id_questao_39').val($('#select_questao_39').val());
}

function carregaQuestoes() {
    // Carrega a questão 1
    var questao_1 = JSON.parse("[" + document.getElementById("id_questao_1").value + "]");
    var select_questao_1 = document.getElementById("select_questao_1");
    
    for (var i = 0; i < questao_1.length; i++) {
        select_questao_1[questao_1[i]].selected = true;
    }
    
    // Carrega a questão 3
    var questao_3 = JSON.parse("[" + document.getElementById("id_questao_3").value + "]");
    var select_questao_3 = document.getElementById("select_questao_3");
    
    for (var i = 0; i < questao_3.length; i++) {
        select_questao_3[questao_3[i]].selected = true;
    }
    
    // Carrega a questão 28
    var questao_28 = JSON.parse("[" + document.getElementById("id_questao_28").value + "]");
    var select_questao_28 = document.getElementById("select_questao_28");
    
    for (var i = 0; i < questao_28.length; i++) {
        select_questao_28[questao_28[i]].selected = true;
    }
    
    // Carrega a questão 31
    var questao_31 = JSON.parse("[" + document.getElementById("id_questao_31").value + "]");
    var select_questao_31 = document.getElementById("select_questao_31");
    
    for (var i = 0; i < questao_31.length; i++) {
        select_questao_31[questao_31[i]].selected = true;
    }
    
    // Carrega a questão 33
    var questao_33 = JSON.parse("[" + document.getElementById("id_questao_33").value + "]");
    var select_questao_33 = document.getElementById("select_questao_33");
    
    for (var i = 0; i < questao_33.length; i++) {
        select_questao_33[questao_33[i]].selected = true;
    }
    
    // Carrega a questão 37
    var questao_37 = JSON.parse("[" + document.getElementById("id_questao_37").value + "]");
    var select_questao_37 = document.getElementById("select_questao_37");
    
    for (var i = 0; i < questao_37.length; i++) {
        select_questao_37[questao_37[i]].selected = true;
    }
    
    // Carrega a questão 39
    var questao_39 = JSON.parse("[" + document.getElementById("id_questao_39").value + "]");
    var select_questao_39 = document.getElementById("select_questao_39");
    
    for (var i = 0; i < questao_39.length; i++) {
        select_questao_39[questao_39[i]].selected = true;
    }
}
