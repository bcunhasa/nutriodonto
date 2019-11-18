// Funções para criação de gráficos

document.addEventListener("DOMContentLoaded", function() {
    criaGraficoQuestao("#aluno_por_escola", carregaDados("#aluno_por_escola"));
    criaGraficoQuestao("#sexo", carregaDados("#sexo"));
    criaGraficoQuestao("#participacao", carregaDados("#participacao"));
    criaGraficoQuestao("#raca", carregaDados("#raca"));
});

function carregaDados(questao) {
    if (questao == "#aluno_por_escola") {
        return [
            { label: "Antônio Carlos Jobim Municipal School ", data: aluno_por_escola[0] },
            { label: "Antônio G. de Carvalho Filho Municipal School ", data: aluno_por_escola[1] },
            { label: "Anne Frank Municipal School ", data: aluno_por_escola[2] },
            { label: "Darcy Ribeiro Municipal School ", data: aluno_por_escola[3] },
            { label: "Henrique Talone Pinheiro Municipal School ", data: aluno_por_escola[4] },
            { label: "Vinícius de Moraes Municipal School.", data: aluno_por_escola[5] },
            { label: "Beatriz Rodrigues da Silva Municipal School ", data: aluno_por_escola[6] },
            { label: "Mestre Pacífico S. Campos Municipal School ", data: aluno_por_escola[7] },
            { label: "Luiz Gonzaga Municipal School ", data: aluno_por_escola[8] },
            { label: "Padre Josimo M. Tavares Municipal School.", data: aluno_por_escola[9] },
            { label: "Daniel Batista Municipal School.", data: aluno_por_escola[10] },
            { label: "Monsenhor Pedro P. Piagem Municipal School.", data: aluno_por_escola[11] },
            { label: "Jorge Amado Municipal School ", data: aluno_por_escola[12] },
            { label: "Maria Rosa de Castro Sales Municipal School ", data: aluno_por_escola[13] },
            { label: "Professor Sávia F. Jacome Municipal School ", data: aluno_por_escola[14] },
            { label: "Caroline C. C. da Silva Municipal School.", data: aluno_por_escola[15] },
            { label: "Aurélio Buarque de Holanda Municipal School ", data: aluno_por_escola[16] },
            { label: "Maria Júlia Amorim Rodrigues Municipal School ", data: aluno_por_escola[17] },
            { label: "Thiago Barbosa Municipal School ", data: aluno_por_escola[18] },
            { label: "Euridice F. de Mello Municipal School.", data: aluno_por_escola[19] },
            { label: "Margarida Gonçalves Municipal School.", data: aluno_por_escola[20] },
            { label: "Crispim Pereira de Alencar Municipal School ", data: aluno_por_escola[21] },
            { label: "Aprigio T. de Matos Municipal School.", data: aluno_por_escola[22] },
            { label: "João Beltrão Municipal School.", data: aluno_por_escola[23] },
            { label: "Luiz Nunes de Oliveira Municipal School.", data: aluno_por_escola[24] },
            { label: "Sueli Pereira A. Reche Municipal School.", data: aluno_por_escola[25] },
            { label: "Marcos Freire Municipal School.", data: aluno_por_escola[26] },
            { label: "Anisio Spínola Teixeira Municipal School.", data: aluno_por_escola[27] },
            { label: "Almirante Tamandaré Municipal School.", data: aluno_por_escola[28] },
        ];
    } else if (questao == "#sexo") {
        return [
            { label: "Male", data: sexo[0] },
            { label: "Female", data: sexo[1] },
            { label: "Other", data: sexo[2] },
            { label: "I do not want to answer", data: sexo[3] },
            { label: "No answer", data: sexo[4] },
        ];
    } else if (questao == "#participacao") {
        return [
            { label: "Only questionnaire", data: participacao[0] },
            { label: "Only exam", data: participacao[1] },
            { label: "Questionnaire and exam", data: participacao[2] },
            { label: "Do not participate of anyone", data: participacao[3] },
        ];
    } else if (questao == "#raca") {
        return [
            { label: "Yellow", data: raca[0] },
            { label: "White", data: raca[1] },
            { label: "Indian", data: raca[2] },
            { label: "Mixed color", data: raca[3] },
            { label: "Black", data: raca[4] },
            { label: "No answer", data: raca[5] },
        ];
    }
}

document.getElementById("baixa-grafico-1").addEventListener("click", function() {
    html2canvas(document.querySelector('#aluno_por_escola')).then(function(canvas) {
        console.log(canvas);
        baixaImagem(canvas.toDataURL(), 'graph.png');
    });
});

document.getElementById("baixa-grafico-2").addEventListener("click", function() {
    html2canvas(document.querySelector('#sexo')).then(function(canvas) {
        console.log(canvas);
        baixaImagem(canvas.toDataURL(), 'graph.png');
    });
});

document.getElementById("baixa-grafico-3").addEventListener("click", function() {
    html2canvas(document.querySelector('#participacao')).then(function(canvas) {
        console.log(canvas);
        baixaImagem(canvas.toDataURL(), 'graph.png');
    });
});

document.getElementById("baixa-grafico-4").addEventListener("click", function() {
    html2canvas(document.querySelector('#raca')).then(function(canvas) {
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
                        return '<div class="flot-pie-label">' + Math.round(series.percent) +'% (' + series.data[0][1] + ')</div>';
                    },
                    background: { 
                        opacity: 0.5,
                        color: '#000000'
                    }
                }
            }
        },
        grid: {
            hoverable: true
        },
        tooltip: true,
        tooltipOpts: {
            content: "%s: %p.0% (%y.0)",
        },
    });
}
