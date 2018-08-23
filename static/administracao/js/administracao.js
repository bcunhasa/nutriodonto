// Funções para organização dos dados de formulários e criação de gráficos

document.addEventListener("DOMContentLoaded", function() {
  carregaHorario();
  carregaCalendario();
});

function organizaHorario() {
    $('#id_horas').val($('#select_horas').val());
}

function organizaCalendario() {
    $('#id_janeiro').val($('#select_janeiro').val());
    $('#id_fevereiro').val($('#select_fevereiro').val());
    $('#id_marco').val($('#select_marco').val());
    $('#id_abril').val($('#select_abril').val());
    $('#id_maio').val($('#select_maio').val());
    $('#id_junho').val($('#select_junho').val());
    $('#id_julho').val($('#select_julho').val());
    $('#id_agosto').val($('#select_agosto').val());
    $('#id_setembro').val($('#select_setembro').val());
    $('#id_outubro').val($('#select_outubro').val());
    $('#id_novembro').val($('#select_novembro').val());
    $('#id_dezembro').val($('#select_dezembro').val());
}

function carregaHorario() {
    var horas = $('#id_horas').val();
    var janeiro = $('#id_janeiro').val();
    var fevereiro = $('#id_fevereiro').val();
    var marco = $('#id_marco').val();
    var abril = $('#id_abril').val();
    var maio = $('#id_maio').val();
    var junho = $('#id_junho').val();
    var julho = $('#id_julho').val();
    var agosto = $('#id_agosto').val();
    var setembro = $('#id_setembro').val();
    var outubro = $('#id_outubro').val();
    var novembro = $('#id_novembro').val();
    var dezembro = $('#id_dezembro').val();
    
    for (var i = 0; i < selectObj.options.length; i++) {
        if (selectObj.options[i].text == valueToSet) {
            selectObj.options[i].selected = true;
        }
    }
    
    $("#select_horas").val("val2");
    
    
    
    
    document.getElementById("select_horas").value = horas;
    document.getElementById("select_janeiro").value = janeiro;
    document.getElementById("select_fevereiro").value = fevereiro;
    document.getElementById("select_marco").value = marco;
    document.getElementById("select_abril").value = abril;
    document.getElementById("select_maio").value = maio;
    document.getElementById("select_junho").value = junho;
    document.getElementById("select_julho").value = julho;
    document.getElementById("select_agosto").value = agosto;
    document.getElementById("select_setembro").value = setembro;
    document.getElementById("select_outubro").value = outubro;
    document.getElementById("select_novembro").value = novembro;
    document.getElementById("select_dezembro").value = dezembro;
}

function carregaCalendario() {
    var janeiro = $('#id_janeiro').val();
    var fevereiro = $('#id_fevereiro').val();
    var marco = $('#id_marco').val();
    var abril = $('#id_abril').val();
    var maio = $('#id_maio').val();
    var junho = $('#id_junho').val();
    var julho = $('#id_julho').val();
    var agosto = $('#id_agosto').val();
    var setembro = $('#id_setembro').val();
    var outubro = $('#id_outubro').val();
    var novembro = $('#id_novembro').val();
    var dezembro = $('#id_dezembro').val();
    
    document.getElementById("select_janeiro").value = janeiro;
    document.getElementById("select_fevereiro").value = fevereiro;
    document.getElementById("select_marco").value = marco;
    document.getElementById("select_abril").value = abril;
    document.getElementById("select_maio").value = maio;
    document.getElementById("select_junho").value = junho;
    document.getElementById("select_julho").value = julho;
    document.getElementById("select_agosto").value = agosto;
    document.getElementById("select_setembro").value = setembro;
    document.getElementById("select_outubro").value = outubro;
    document.getElementById("select_novembro").value = novembro;
    document.getElementById("select_dezembro").value = dezembro;
}

function setaValores(select, valor) {
    for (var i = 0; i < select.options.length; i++) {
        if (select.options[i].text == valor) {
            select.options[i].selected = true;
        }
    }
}
