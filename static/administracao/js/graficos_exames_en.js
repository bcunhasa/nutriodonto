// Funções para criação de gráficos

document.addEventListener("DOMContentLoaded", function() {
    criaGrafico("#situacao_coroa", carregaDados("#situacao_coroa"), "Dental problems occurrence");
    criaGrafico("#tratamento_necessario", carregaDados("#tratamento_necessario"), "Treatment indication occurrence");
    criaGrafico("#condicao_periodontal", carregaDados("#condicao_periodontal"), "Periodontal problems occurrence");
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
                content: function (label, x, y) { return 'Occurrences: ' + y; }
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
            ["Does not have any dental problem", situacao_coroa[0]],
            ["Decayed", situacao_coroa[1]],
            ["Restored, but with caries", situacao_coroa[2]],
            ["Restored without caries", situacao_coroa[3]],
            ["Lost because of caries", situacao_coroa[4]],
            ["Lost for another reason", situacao_coroa[5]],
            ["Has sealant", situacao_coroa[6]],
            ["Tooth-supported bridge or tooth crown", situacao_coroa[7]],
            ["Unerupted - unexposed root", situacao_coroa[8]],
            ["Trauma (fracture)", situacao_coroa[9]],
        ];
    } else if (questao == "#tratamento_necessario") {
        return [
            ["Does not have any indicated treatment", tratamento_necessario[0]],
            ["Restauration of 1 surface", tratamento_necessario[1]],
            ["Restauration of 2 or more surfaces", tratamento_necessario[2]],
            ["Crown for any reason", tratamento_necessario[3]],
            ["Aesthetic facet", tratamento_necessario[4]],
            ["Pulp treatment and restoration", tratamento_necessario[5]],
            ["Extraction", tratamento_necessario[6]],
            ["White spot remineralization", tratamento_necessario[7]],
            ["Sealant", tratamento_necessario[8]],
        ];
    } else if (questao == "#condicao_periodontal") {
        return [
            ["Does not have ant periodontal problems", condicao_periodontal[0]],
            ["Gingival bleeding", condicao_periodontal[1]],
            ["Dental calculus", condicao_periodontal[2]],
            ["Periodontal prockets", condicao_periodontal[3]],
        ];
    }
}

document.getElementById("baixa-grafico-1").addEventListener("click", function() {
    html2canvas(document.querySelector('#situacao_coroa')).then(function(canvas) {
        console.log(canvas);
        baixaImagem(canvas.toDataURL(), 'graph.png');
    });
});

document.getElementById("baixa-grafico-2").addEventListener("click", function() {
    html2canvas(document.querySelector('#tratamento_necessario')).then(function(canvas) {
        console.log(canvas);
        baixaImagem(canvas.toDataURL(), 'graph.png');
    });
});

document.getElementById("baixa-grafico-3").addEventListener("click", function() {
    html2canvas(document.querySelector('#condicao_periodontal')).then(function(canvas) {
        console.log(canvas);
        baixaImagem(canvas.toDataURL(), 'graph.png');
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
