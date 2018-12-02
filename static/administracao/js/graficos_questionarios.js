// Funções para criação de gráficos

document.addEventListener("DOMContentLoaded", function() {
    criaGraficoQuestao("#questao1", carregaDados("#questao1"));
    criaGraficoQuestao("#questao2", carregaDados("#questao2"));
});

function criaGraficoQuestao(questao, dados) {
    var data = dados;
    
    $.plot($(questao), data, { 
        series: {
            pie: {
                show: true,
                radius: 1,
                label: {
                    show: true,
                    radius: 0.9,
                    formatter: function (label, series) {
                        return '<div class="flot-pie-label">' + Math.round(series.percent) + '%</div>';
                    },
                    background: { 
                        opacity: 0.5,
                        color: '#000000'
                    }
                }
            }
        }
    });
}

function carregaDados(questao) {
    if (questao == "#questao1") {
        return [
            { label: "Ensino Fundamental", data: questao_1[0] },
            { label: "Ensino Médio", data: questao_1[1] },
            { label: "Ensino Médio Técnico", data: questao_1[2] },
            { label: "Ensino Superior", data: questao_1[3] },
            { label: "Pós-graduação", data: questao_1[4] },
            { label: "Não sei", data: questao_1[5] },
        ];
    } else if (questao == "#questao2") {
        return [
            { label: "Somente continuar estudando", data: questao_2[0] },
            { label: "Somente trabalhar", data: questao_2[1] },
            { label: "Continuar estudando e trabalhar", data: questao_2[2] },
            { label: "Seguir outro plano", data: questao_2[3] },
            { label: "Não sei", data: questao_2[4] },
        ];
    }
}
