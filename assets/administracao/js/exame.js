// Funções para manipulação dos campos de exame

function valoresPadrao() {
    // Define os valores padrão para a coroa
    document.getElementById("id_carie_coroa_18").value = "9";
    document.getElementById("id_carie_coroa_17").value = "0";
    document.getElementById("id_carie_coroa_16").value = "0";
    document.getElementById("id_carie_coroa_15").value = "0";
    document.getElementById("id_carie_coroa_14").value = "0";
    document.getElementById("id_carie_coroa_13").value = "0";
    document.getElementById("id_carie_coroa_12").value = "0";
    document.getElementById("id_carie_coroa_11").value = "0";
    
    document.getElementById("id_carie_coroa_21").value = "0";
    document.getElementById("id_carie_coroa_22").value = "0";
    document.getElementById("id_carie_coroa_23").value = "0";
    document.getElementById("id_carie_coroa_24").value = "0";
    document.getElementById("id_carie_coroa_25").value = "0";
    document.getElementById("id_carie_coroa_26").value = "0";
    document.getElementById("id_carie_coroa_27").value = "0";
    document.getElementById("id_carie_coroa_28").value = "9";
    
    document.getElementById("id_carie_coroa_38").value = "9";
    document.getElementById("id_carie_coroa_37").value = "0";
    document.getElementById("id_carie_coroa_36").value = "0";
    document.getElementById("id_carie_coroa_35").value = "0";
    document.getElementById("id_carie_coroa_34").value = "0";
    document.getElementById("id_carie_coroa_33").value = "0";
    document.getElementById("id_carie_coroa_32").value = "0";
    document.getElementById("id_carie_coroa_31").value = "0";
    
    document.getElementById("id_carie_coroa_41").value = "0";
    document.getElementById("id_carie_coroa_42").value = "0";
    document.getElementById("id_carie_coroa_43").value = "0";
    document.getElementById("id_carie_coroa_44").value = "0";
    document.getElementById("id_carie_coroa_45").value = "0";
    document.getElementById("id_carie_coroa_46").value = "0";
    document.getElementById("id_carie_coroa_47").value = "0";
    document.getElementById("id_carie_coroa_48").value = "9";
    
    // Define os valores padrão para o tratamento
    document.getElementById("id_carie_tratamento_18").value = "9";
    document.getElementById("id_carie_tratamento_17").value = "0";
    document.getElementById("id_carie_tratamento_16").value = "0";
    document.getElementById("id_carie_tratamento_15").value = "0";
    document.getElementById("id_carie_tratamento_14").value = "0";
    document.getElementById("id_carie_tratamento_13").value = "0";
    document.getElementById("id_carie_tratamento_12").value = "0";
    document.getElementById("id_carie_tratamento_11").value = "0";
    
    document.getElementById("id_carie_tratamento_21").value = "0";
    document.getElementById("id_carie_tratamento_22").value = "0";
    document.getElementById("id_carie_tratamento_23").value = "0";
    document.getElementById("id_carie_tratamento_24").value = "0";
    document.getElementById("id_carie_tratamento_25").value = "0";
    document.getElementById("id_carie_tratamento_26").value = "0";
    document.getElementById("id_carie_tratamento_27").value = "0";
    document.getElementById("id_carie_tratamento_28").value = "9";
    
    document.getElementById("id_carie_tratamento_38").value = "9";
    document.getElementById("id_carie_tratamento_37").value = "0";
    document.getElementById("id_carie_tratamento_36").value = "0";
    document.getElementById("id_carie_tratamento_35").value = "0";
    document.getElementById("id_carie_tratamento_34").value = "0";
    document.getElementById("id_carie_tratamento_33").value = "0";
    document.getElementById("id_carie_tratamento_32").value = "0";
    document.getElementById("id_carie_tratamento_31").value = "0";
    
    document.getElementById("id_carie_tratamento_41").value = "0";
    document.getElementById("id_carie_tratamento_42").value = "0";
    document.getElementById("id_carie_tratamento_43").value = "0";
    document.getElementById("id_carie_tratamento_44").value = "0";
    document.getElementById("id_carie_tratamento_45").value = "0";
    document.getElementById("id_carie_tratamento_46").value = "0";
    document.getElementById("id_carie_tratamento_47").value = "0";
    document.getElementById("id_carie_tratamento_48").value = "9";
    
    // Define os valores padrão para os campos de condição periodontal
    document.getElementById("id_periodontal_sangramento_1716").value = "0";
    document.getElementById("id_periodontal_calculo_1716").value = "0";
    document.getElementById("id_periodontal_bolsa_1716").value = "9";
    
    document.getElementById("id_periodontal_sangramento_11").value = "0";
    document.getElementById("id_periodontal_calculo_11").value = "0";
    document.getElementById("id_periodontal_bolsa_11").value = "9";
    
    document.getElementById("id_periodontal_sangramento_2627").value = "0";
    document.getElementById("id_periodontal_calculo_2627").value = "0";
    document.getElementById("id_periodontal_bolsa_2627").value = "9";
    
    document.getElementById("id_periodontal_sangramento_3736").value = "0";
    document.getElementById("id_periodontal_calculo_3736").value = "0";
    document.getElementById("id_periodontal_bolsa_3736").value = "9";
    
    document.getElementById("id_periodontal_sangramento_31").value = "0";
    document.getElementById("id_periodontal_calculo_31").value = "0";
    document.getElementById("id_periodontal_bolsa_31").value = "9";
    
    document.getElementById("id_periodontal_sangramento_4647").value = "0";
    document.getElementById("id_periodontal_calculo_4647").value = "0";
    document.getElementById("id_periodontal_bolsa_4647").value = "9";
}

function limpaCampos() {
    // Limpa todas os campos de coroa
    document.getElementById("id_carie_coroa_18").value = "";
    document.getElementById("id_carie_coroa_17").value = "";
    document.getElementById("id_carie_coroa_16").value = "";
    document.getElementById("id_carie_coroa_15").value = "";
    document.getElementById("id_carie_coroa_14").value = "";
    document.getElementById("id_carie_coroa_13").value = "";
    document.getElementById("id_carie_coroa_12").value = "";
    document.getElementById("id_carie_coroa_11").value = "";
    
    document.getElementById("id_carie_coroa_21").value = "";
    document.getElementById("id_carie_coroa_22").value = "";
    document.getElementById("id_carie_coroa_23").value = "";
    document.getElementById("id_carie_coroa_24").value = "";
    document.getElementById("id_carie_coroa_25").value = "";
    document.getElementById("id_carie_coroa_26").value = "";
    document.getElementById("id_carie_coroa_27").value = "";
    document.getElementById("id_carie_coroa_28").value = "";
    
    document.getElementById("id_carie_coroa_38").value = "";
    document.getElementById("id_carie_coroa_37").value = "";
    document.getElementById("id_carie_coroa_36").value = "";
    document.getElementById("id_carie_coroa_35").value = "";
    document.getElementById("id_carie_coroa_34").value = "";
    document.getElementById("id_carie_coroa_33").value = "";
    document.getElementById("id_carie_coroa_32").value = "";
    document.getElementById("id_carie_coroa_31").value = "";
    
    document.getElementById("id_carie_coroa_41").value = "";
    document.getElementById("id_carie_coroa_42").value = "";
    document.getElementById("id_carie_coroa_43").value = "";
    document.getElementById("id_carie_coroa_44").value = "";
    document.getElementById("id_carie_coroa_45").value = "";
    document.getElementById("id_carie_coroa_46").value = "";
    document.getElementById("id_carie_coroa_47").value = "";
    document.getElementById("id_carie_coroa_48").value = "";
    
    // Limpa todos os campos de tratamento
    document.getElementById("id_carie_tratamento_18").value = "";
    document.getElementById("id_carie_tratamento_17").value = "";
    document.getElementById("id_carie_tratamento_16").value = "";
    document.getElementById("id_carie_tratamento_15").value = "";
    document.getElementById("id_carie_tratamento_14").value = "";
    document.getElementById("id_carie_tratamento_13").value = "";
    document.getElementById("id_carie_tratamento_12").value = "";
    document.getElementById("id_carie_tratamento_11").value = "";
    
    document.getElementById("id_carie_tratamento_21").value = "";
    document.getElementById("id_carie_tratamento_22").value = "";
    document.getElementById("id_carie_tratamento_23").value = "";
    document.getElementById("id_carie_tratamento_24").value = "";
    document.getElementById("id_carie_tratamento_25").value = "";
    document.getElementById("id_carie_tratamento_26").value = "";
    document.getElementById("id_carie_tratamento_27").value = "";
    document.getElementById("id_carie_tratamento_28").value = "";
    
    document.getElementById("id_carie_tratamento_38").value = "";
    document.getElementById("id_carie_tratamento_37").value = "";
    document.getElementById("id_carie_tratamento_36").value = "";
    document.getElementById("id_carie_tratamento_35").value = "";
    document.getElementById("id_carie_tratamento_34").value = "";
    document.getElementById("id_carie_tratamento_33").value = "";
    document.getElementById("id_carie_tratamento_32").value = "";
    document.getElementById("id_carie_tratamento_31").value = "";
    
    document.getElementById("id_carie_tratamento_41").value = "";
    document.getElementById("id_carie_tratamento_42").value = "";
    document.getElementById("id_carie_tratamento_43").value = "";
    document.getElementById("id_carie_tratamento_44").value = "";
    document.getElementById("id_carie_tratamento_45").value = "";
    document.getElementById("id_carie_tratamento_46").value = "";
    document.getElementById("id_carie_tratamento_47").value = "";
    document.getElementById("id_carie_tratamento_48").value = "";
    
    // Limpa todos os campos de condição periodontal
    document.getElementById("id_periodontal_sangramento_1716").value = "";
    document.getElementById("id_periodontal_calculo_1716").value = "";
    document.getElementById("id_periodontal_bolsa_1716").value = "";
    
    document.getElementById("id_periodontal_sangramento_11").value = "";
    document.getElementById("id_periodontal_calculo_11").value = "";
    document.getElementById("id_periodontal_bolsa_11").value = "";
    
    document.getElementById("id_periodontal_sangramento_2627").value = "";
    document.getElementById("id_periodontal_calculo_2627").value = "";
    document.getElementById("id_periodontal_bolsa_2627").value = "";
    
    document.getElementById("id_periodontal_sangramento_3736").value = "";
    document.getElementById("id_periodontal_calculo_3736").value = "";
    document.getElementById("id_periodontal_bolsa_3736").value = "";
    
    document.getElementById("id_periodontal_sangramento_31").value = "";
    document.getElementById("id_periodontal_calculo_31").value = "";
    document.getElementById("id_periodontal_bolsa_31").value = "";
    
    document.getElementById("id_periodontal_sangramento_4647").value = "";
    document.getElementById("id_periodontal_calculo_4647").value = "";
    document.getElementById("id_periodontal_bolsa_4647").value = "";
}
