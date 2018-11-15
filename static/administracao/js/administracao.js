// Funções para organização dos dados de formulários e criação de gráficos

document.addEventListener("DOMContentLoaded", function() {
  carregaQuestoes();
});

function salvaQuestoes() {
    $('#id_questao_60').val($('#select_questao_60').val());
    $('#id_questao_146').val($('#select_questao_146').val());
}

function carregaQuestoes() {
    var id_questao_60 = $('#id_questao_60').val();
    var id_questao_146 = $('#id_questao_146').val();
    
    for (var i = 0; i < id_questao_146.length; i++) {
        if ($("#select_questao_146").options[0].text == id_questao_146[i])
            $("#select_questao_146").options[0].selected = true;
        if ($("#select_questao_146").options[1].text == id_questao_146[i])
            $("#select_questao_146").options[1].selected = true;
        if ($("#select_questao_146").options[2].text == id_questao_146[i])
            $("#select_questao_146").options[2].selected = true;
        if ($("#select_questao_146").options[3].text == id_questao_146[i])
            $("#select_questao_146").options[3].selected = true;
        if ($("#select_questao_146").options[4].text == id_questao_146[i])
            $("#select_questao_146").options[4].selected = true;
        if ($("#select_questao_146").options[5].text == id_questao_146[i])
            $("#select_questao_146").options[5].selected = true;
        if ($("#select_questao_146").options[6].text == id_questao_146[i])
            $("#select_questao_146").options[6].selected = true;
        if ($("#select_questao_146").options[7].text == id_questao_146[i])
            $("#select_questao_146").options[7].selected = true;
    }
    
    console.log($("#select_questao_60").val());
    console.log($("#select_questao_146").val());
}
