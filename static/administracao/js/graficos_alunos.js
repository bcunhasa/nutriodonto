// Funções para criação de gráficos

document.addEventListener("DOMContentLoaded", function() {
    criaGraficoQuestao("#aluno_por_escola", carregaDados("#aluno_por_escola"));
    criaGraficoQuestao("#sexo", carregaDados("#sexo"));
    criaGraficoQuestao("#participacao", carregaDados("#participacao"));
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

function carregaDados(questao) {
    if (questao == "#aluno_por_escola") {
        return [
            { label: "Escola municipal Antônio Carlos Jobim", data: aluno_por_escola[0] },
            { label: "Escola municipal Antônio G. de Carvalho Filho", data: aluno_por_escola[1] },
            { label: "Escola municipal Anne Frank", data: aluno_por_escola[2] },
            { label: "Escola municipal Darcy Ribeiro", data: aluno_por_escola[3] },
            { label: "Escola municipal Henrique Talone Pinheiro", data: aluno_por_escola[4] },
            { label: "Escola municipal de T.I. Vinícius de Moraes", data: aluno_por_escola[5] },
            { label: "Escola municipal Beatriz Rodrigues da Silva", data: aluno_por_escola[6] },
            { label: "Escola municipal Mestre Pacífico S. Campos", data: aluno_por_escola[7] },
            { label: "Escola municipal Luiz Gonzaga", data: aluno_por_escola[8] },
            { label: "Escola municipal de T.I. Padre Josimo M. Tavares", data: aluno_por_escola[9] },
            { label: "Escola municipal de T.I. Daniel Batista", data: aluno_por_escola[10] },
            { label: "Escola municipal de T.I. Monsenhor Pedro P. Piagem", data: aluno_por_escola[11] },
            { label: "Escola municipal Jorge Amado", data: aluno_por_escola[12] },
            { label: "Escola municipal Maria Rosa de Castro Sales", data: aluno_por_escola[13] },
            { label: "Escola municipal Professor Sávia F. Jacome", data: aluno_por_escola[14] },
            { label: "Escola municipal de T.I. Caroline C. C. da Silva", data: aluno_por_escola[15] },
            { label: "Escola municipal Aurélio Buarque de Holanda", data: aluno_por_escola[16] },
            { label: "Escola municipal Maria Júlia Amorim Rodrigues", data: aluno_por_escola[17] },
            { label: "Escola municipal Thiago Barbosa", data: aluno_por_escola[18] },
            { label: "Escola municipal de T.I. Euridice F. de Mello", data: aluno_por_escola[19] },
            { label: "Escola municipal de T.I. Margarida Gonçalves", data: aluno_por_escola[20] },
            { label: "Escola municipal Crispim Pereira de Alencar", data: aluno_por_escola[21] },
            { label: "Escola municipal de T.I. Aprigio T. de Matos", data: aluno_por_escola[22] },
            { label: "Escola municipal de T.I. João Beltrão", data: aluno_por_escola[23] },
            { label: "Escola municipal de T.I. Luiz Nunes de Oliveira", data: aluno_por_escola[24] },
            { label: "Escola municipal de T.I. Sueli Pereira A. Reche", data: aluno_por_escola[25] },
        ];
    } else if (questao == "#sexo") {
        return [
            { label: "Masculino", data: sexo[0] },
            { label: "Feminino", data: sexo[1] },
            { label: "Outro", data: sexo[2] },
            { label: "Prefiro não responder", data: sexo[3] },
            { label: "Sem resposta", data: sexo[4] },
        ];
    } else if (questao == "#participacao") {
        return [
            { label: "Participou apenas do questionário", data: participacao[0] },
            { label: "Participou apenas do exame", data: participacao[1] },
            { label: "Participou do questionário e do exame", data: participacao[2] },
            { label: "Não participou de nenhum dos dois", data: participacao[3] },
        ];
    }
}
