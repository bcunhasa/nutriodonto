// Funções para criação de gráficos

document.addEventListener("DOMContentLoaded", function() {
    criaGrafico("#situacao_coroa", carregaDados("#situacao_coroa"), "Ocorrências de problemas na coroa");
    criaGrafico("#tratamento_necessario", carregaDados("#tratamento_necessario"), "Ocorrências de indicação de tratamento");
    criaGrafico("#condicao_periodontal", carregaDados("#condicao_periodontal"), "Ocorrências de problemas periodontais");
});

function criaGrafico(questao, dados, label) {
    var data = [], ticks = [];  
    for (var i = 0; i < dados.length; i++) {
        data.push([i,dados[i][1]]);
        ticks.push([i,dados[i][0]]);
    }
    
    $.plot(
        $(questao), [{
            data : data,
            label: label,
            color: '#012D4C',
            bars: {
                align: 'center',
                lineWidth: 0,
                show: true,
                barWidth: 0.6,
                fill: 0.9
            },
            valueLabels: {
                show: true,
            }
        }],
        {
            grid: {
                borderColor: '#eee',
                borderWidth: 1,
                hoverable: true,
                backgroundColor: '#fcfcfc'
            },
            tooltip: true,
            tooltipOpts: {
                content: function (label, x, y) { return 'Ocorrências: ' + y; }
            },
            xaxis: {
                ticks: ticks,
            },
            yaxis: {
                tickColor: '#eee',
                minTickSize: 0,
                tickDecimals: 0,
            },
        }
    );
}

function carregaDados(questao) {
    if (questao == "#situacao_coroa") {
        return [
            ["Não possui nenhum problema na coroa", situacao_coroa[0]],
            ["Apresenta dente cariado", situacao_coroa[1]],
            ["Apresenta dente restaurado mas com cárie", situacao_coroa[2]],
            ["Apresenta dente restaurado e sem cárie", situacao_coroa[3]],
            ["Apresenta dente perdido devido à cárie", situacao_coroa[4]],
            ["Apresenta dente perdido por outras razões", situacao_coroa[5]],
            ["Apresenta dente com selante", situacao_coroa[6]],
            ["Apresenta apoio de ponte ou coroa", situacao_coroa[7]],
            ["Apresenta dente não erupcionado - raiz não exposta", situacao_coroa[8]],
            ["Apresenta dente com trauma (fratura)", situacao_coroa[9]],
        ];
    } else if (questao == "#tratamento_necessario") {
        return [
            ["Nenhum tratamento indicado", tratamento_necessario[0]],
            ["Restauração de 1 superfície", tratamento_necessario[1]],
            ["Restauração de 2 ou mais superfícies", tratamento_necessario[2]],
            ["Coroa por qualquer razão", tratamento_necessario[3]],
            ["Faceta estética", tratamento_necessario[4]],
            ["Tratamento pulpar e restauração", tratamento_necessario[5]],
            ["Extração", tratamento_necessario[6]],
            ["Remineralização de mancha branca", tratamento_necessario[7]],
            ["Selante", tratamento_necessario[8]],
        ];
    } else if (questao == "#condicao_periodontal") {
        return [
            ["Não apresenta nenhum problema", condicao_periodontal[0]],
            ["Apresenta sangramento", condicao_periodontal[1]],
            ["Apresenta cálculo dentário", condicao_periodontal[2]],
            ["Apresenta bolsa periodontal", condicao_periodontal[3]],
        ];
    }
}

document.getElementById("baixa-grafico-1").addEventListener("click", function() {
    html2canvas(document.querySelector('#situacao_coroa')).then(function(canvas) {
        console.log(canvas);
        baixaImagem(canvas.toDataURL(), 'grafico.png');
    });
});

document.getElementById("baixa-grafico-2").addEventListener("click", function() {
    html2canvas(document.querySelector('#tratamento_necessario')).then(function(canvas) {
        console.log(canvas);
        baixaImagem(canvas.toDataURL(), 'grafico.png');
    });
});

document.getElementById("baixa-grafico-3").addEventListener("click", function() {
    html2canvas(document.querySelector('#condicao_periodontal')).then(function(canvas) {
        console.log(canvas);
        baixaImagem(canvas.toDataURL(), 'grafico.png');
    });
});

function baixaImagem(uri, filename) {
    var link = document.createElement('a');
    
    if (typeof link.download === 'string') {
        link.href = uri;
        link.download = filename;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    } else {
        window.open(uri);
    }
}
