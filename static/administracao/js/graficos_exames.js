// Funções para criação de gráficos

document.addEventListener("DOMContentLoaded", function() {
    criaGraficoQuestao("#situacao_coroa", carregaDados("#situacao_coroa"));
    criaGraficoQuestao("#tratamento_necessario", carregaDados("#tratamento_necessario"));
    criaGraficoQuestao("#condicao_periodontal", carregaDados("#condicao_periodontal"));
});

function criaGraficoQuestao(questao, dados) {
    var data = dados;
    
    $.plot($(questao), data, {
        series: {
            bars: {
                align: 'center',
                lineWidth: 0,
                show: true,
                barWidth: 0.6,
                fill: 0.9
            }
        },
        grid: {
            borderColor: '#eee',
            borderWidth: 1,
            hoverable: true,
            backgroundColor: '#fcfcfc'
        },
        tooltip: true,
        tooltipOpts: {
            content: function (label, x, y) { return x + ' : ' + y; }
        },
        xaxis: {
            tickColor: '#fcfcfc',
            mode: 'categories'
        },
        yaxis: {
            // position: 'right' or 'left'
            tickColor: '#eee'
        },
        shadowSize: 0
    });
}

function carregaDados(questao) {
    if (questao == "#situacao_coroa") {
        return [
            { label: "Não possui nenhum problema na coroa", data: situacao_coroa[0] },
            { label: "Apresenta dente cariado", data: situacao_coroa[1] },
            { label: "Apresenta dente restaurado mas com cárie", data: situacao_coroa[2] },
            { label: "Apresenta dente restaurado e sem cárie", data: situacao_coroa[3] },
            { label: "Apresenta dente perdido devido à cárie", data: situacao_coroa[4] },
            { label: "Apresenta dente perdido por outras razões", data: situacao_coroa[5] },
            { label: "Apresenta dente com selante", data: situacao_coroa[6] },
            { label: "Apresenta apoio de ponte ou coroa", data: situacao_coroa[7] },
            { label: "Apresenta dente não erupcionado - raiz não exposta", data: situacao_coroa[8] },
            { label: "Apresenta dente com trauma (fratura)", data: situacao_coroa[9] },
        ];
    } else if (questao == "#tratamento_necessario") {
        
        return [
            { label: "Nenhum tratamento indicado", data: tratamento_necessario[0] },
            { label: "Restauração de 1 superfície", data: tratamento_necessario[1] },
            { label: "Restauração de 2 ou mais superfícies", data: tratamento_necessario[2] },
            { label: "Coroa por qualquer razão", data: tratamento_necessario[3] },
            { label: "Faceta estética", data: tratamento_necessario[4] },
            { label: "Tratamento pulpar e restauração", data: tratamento_necessario[5] },
            { label: "Extração", data: tratamento_necessario[6] },
            { label: "Remineralização de mancha branca", data: tratamento_necessario[7] },
            { label: "Selante", data: tratamento_necessario[8] },
        ];
    } else if (questao == "#condicao_periodontal") {
        return [
            { label: "Não apresenta nenhum problema", data: condicao_periodontal[0] },
            { label: "Apresenta sangramento", data: condicao_periodontal[1] },
            { label: "Apresenta cálculo dentário", data: condicao_periodontal[2] },
            { label: "Apresenta bolsa periodontal", data: condicao_periodontal[3] },
        ];
    }
}
