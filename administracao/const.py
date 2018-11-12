# Constantes globais

TAMANHO_NOMES = 200
TAMANHO_OPCOES = 2
TAMANHO_CODIGOS = 5


# Constantes do modelo Aluno

SEXO = (
    ('0', 'Masculino'),
    ('1', 'Feminino'),
    ('2', 'Outro'),
    ('3', 'Prefiro não responder'),
)

RACA = (
    ('0', 'Amarela'),
    ('1', 'Branca'),
    ('2', 'Indígena'),
    ('3', 'Parda'),
    ('4', 'Preta'),
)

ESCOLA = (
    ('Escola municipal Antônio Carlos Jobim', 'Escola municipal Antônio Carlos Jobim'),
    ('Escola municipal Antônio G. de Carvalho Filho', 'Escola municipal Antônio G. de Carvalho Filho'),
    ('Escola municipal Anne Frank', 'Escola municipal Anne Frank'),
    ('Escola municipal Darcy Ribeiro', 'Escola municipal Darcy Ribeiro'),
    ('Escola municipal Henrique Talone Pinheiro', 'Escola municipal Henrique Talone Pinheiro'),
    ('Escola municipal de T.I. Vinícius de Moraes', 'Escola municipal de T.I. Vinícius de Moraes'),
    ('Escola municipal Beatriz Rodrigues da Silva', 'Escola municipal Beatriz Rodrigues da Silva'),
    ('Escola municipal Mestre Pacífico S. Campos', 'Escola municipal Mestre Pacífico S. Campos'),
    ('Escola municipal Luiz Gonzaga', 'Escola municipal Luiz Gonzaga'),
    ('Escola municipal de T.I. Padre Josimo M. Tavares', 'Escola municipal de T.I. Padre Josimo M. Tavares'),
    ('Escola municipal de T.I. Daniel Batista', 'Escola municipal de T.I. Daniel Batista'),
    ('Escola municipal de T.I. Monsenhor Pedro P. Piagem', 'Escola municipal de T.I. Monsenhor Pedro P. Piagem'),
    ('Escola municipal Jorge Amado', 'Escola municipal Jorge Amado'),
    ('Escola municipal Maria Rosa de Castro Sales', 'Escola municipal Maria Rosa de Castro Sales'),
    ('Escola municipal Professor Sávia F. Jacome', 'Escola municipal Professor Sávia F. Jacome'),
    ('Escola municipal de T.I. Caroline C. C. da Silva', 'Escola municipal de T.I. Caroline C. C. da Silva'),
    ('Escola municipal Aurélio Buarque de Holanda', 'Escola municipal Aurélio Buarque de Holanda'),
    ('Escola municipal Maria Júlia Amorim Rodrigues', 'Escola municipal Maria Júlia Amorim Rodrigues'),
    ('Escola municipal Thiago Barbosa', 'Escola municipal Thiago Barbosa'),
    ('Escola municipal de T.I. Euridice F. de Mello', 'Escola municipal de T.I. Euridice F. de Mello'),
    ('Escola municipal de T.I. Margarida Gonçalves', 'Escola municipal de T.I. Margarida Gonçalves'),
    ('Escola municipal Crispim Pereira de Alencar', 'Escola municipal Crispim Pereira de Alencar'),
    ('Escola municipal de T.I. Aprigio T. de Matos', 'Escola municipal de T.I. Aprigio T. de Matos'),
    ('Escola municipal de T.I. João Beltrão', 'Escola municipal de T.I. João Beltrão'),
    ('Escola municipal de T.I. Luiz Nunes de Oliveira', 'Escola municipal de T.I. Luiz Nunes de Oliveira'),
    ('Escola municipal de T.I. Sueli Pereira A. Reche', 'Escola municipal de T.I. Sueli Pereira A. Reche'),
    
    ('Escola Silverio Ribeiro Matos', 'Escola Silverio Ribeiro Matos'),
    ('Escola de teste', 'Escola de teste'),
)

PERIODO = (
    ('0', 'Matutino'),
    ('1', 'Vespertino'),
    ('2', 'Noturno'),
    ('3', 'Tempo Integral')
)

TURMA = (
    ('0', 'A'),
    ('1', 'B'),
    ('2', 'C'),
    ('3', 'D')
)

MUNICIPIO = (
    ('0', 'Palmas'),
)


# Constantes dos modelos relacionados a exame

FLUOROSE = (
    ('0', 'Normal'),
    ('1', 'Questionável'),
    ('2', 'Muito leve'),
    ('3', 'Leve'),
    ('4', 'Moderada'),
    ('5', 'Grave'),
    ('9', 'Sem informação')
)

TRAUMATISMO = (
    ('0', 'Nenhum traumatismo'),
    ('1', 'Fratura de esmalte'),
    ('2', 'Fratura de esmalte e dentina'),
    ('3', 'Fratura de esmalte e dentina com exposição pulpar'),
    ('4', 'Ausência do dente devido a traumatismo'),
    ('9', 'Exame não realizado')
)

# Constantes relacionadas ao exame de edentulismo
USO_PROTESE = (
    ('0', 'Não usa prótese dentária'),
    ('1', 'Usa uma ponte fixa'),
    ('2', 'Usa mais do que uma ponte fixa'),
    ('3', 'Usa prótese parcial removível'),
    ('4', 'Usa uma ou mais pontes fixas e uma ou mais próteses parciais removíveis'),
    ('5', 'Usa prótese dentária total'),
    ('9', 'Sem informação')
)

NECESSIDADE_PROTESE = (
    ('0', 'Não necessita de prótese dentária'),
    ('1', 'Necessita uma prótese, fixa ou removível, para substituição de um elemento'),
    ('2', 'Necessita uma prótese, fixa ou removível, para substituição de mais de um elemento'),
    ('3', 'Necessita uma combinação de próteses, fixas e/ou removíveis, para substituição de um e/ou mais de um elemento'),
    ('4', 'Necessita prótese dentária total'),
    ('9', 'Sem informação')
)

# Constantes relacionadas ao exame periodontal
CPI_SANGRAMENTO = (
    ('0', 'Ausência'),
    ('1', 'Presença'),
    ('X', 'Sextante excluído'),
    ('9', 'Não examinado')
)

CPI_CALCULO = (
    ('0', 'Ausência'),
    ('1', 'Presença'),
    ('X', 'Sextante excluído'),
    ('9', 'Não examinado')
)

CPI_BOLSA = (
    ('0', 'Ausência'),
    ('1', 'Presença de bolsa rasa'),
    ('2', 'Presença de bolsa profunda'),
    ('X', 'Sextante excluído'),
    ('9', 'Não examinado')
)

PIP = (
    ('0', 'Perda de inserção entre 0 e 3 mm'),
    ('1', 'Perda de inserção entre 4 mm e 5 mm'),
    ('2', 'Perda de inserção entre 5 mm e 8 mm'),
    ('3', 'Perda de inserçao entre 9 mm e 11 mm'),
    ('4', 'Perda de inserção entre 12 mm ou mais'),
    ('X', 'Sextante excluído'),
    ('9', 'Não examinado')
)

# Constantes relacionadas ao exame de cárie

CARIE_COROA = (
    # Códigos para dentes decíduos
    ('A', 'Hígido'),
    ('B', 'Cariado'),
    ('C', 'Restaurado mas com cárie'),
    ('D', 'Restaurado e sem cárie'),
    ('E', 'Perdido devido à cárie'),
    ('F', 'Perdido por outras razões'),
    ('G', 'Apresenta selante'),
    ('H', 'Apoio de ponte ou coroa'),
    ('K', 'Não erupcionado - raiz não exposta'),
    ('T', 'Trauma (fratura)'),
    ('L', 'Dente excluído'),
    
    # Códigos para dentes permanentes
    ('0', 'Hígido'),
    ('1', 'Cariado'),
    ('2', 'Restaurado mas com cárie'),
    ('3', 'Restaurado e sem cárie'),
    ('4', 'Perdido devido à cárie'),
    ('5', 'Perdido por outras razões'),
    ('6', 'Apresenta selante'),
    ('7', 'Apoio de ponte ou coroa'),
    ('8', 'Não erupcionado - raiz não exposta'),
    ('T', 'Trauma (fratura)'),
    ('9', 'Dente excluído')
)

CARIE_RAIZ = (
    ('0', 'Hígido'),
    ('1', 'Cariado'),
    ('2', 'Restaurado mas com cárie'),
    ('3', 'Restaurado e sem cárie'),
    ('7', 'Apoio de ponte ou coroa'),
    ('8', 'Não erupcionado - raiz não exposta'),
    ('9', 'Dente excluído')
)

CARIE_TRATAMENTO = (
    ('0', 'Nenhum'),
    ('1', 'Restauração de 1 superfície'),
    ('2', 'Restauração de 2 ou mais superfícies'),
    ('3', 'Coroa por qualquer razão'),
    ('4', 'Faceta estética'),
    ('5', 'Tratamento pulpar e restauração'),
    ('6', 'Extração'),
    ('7', 'Remineralização de mancha branca'),
    ('8', 'Selante'),
    ('9', 'Sem informação')
)


# Constantes do modelo Questionário

# Informações pessoais

ALUNO_1 = (
    ('0', 'Ensino Fundamental'),
    ('1', 'Ensino Médio'),
    ('2', 'Ensino Médio Técnico'),
    ('3', 'Ensino Superior'),
    ('4', 'Pós-graduação'),
    ('5', 'Não sei'),
)

ALUNO_2 = (
    ('0', 'Somente continuar estudando'),
    ('1', 'Somente trabalhar'),
    ('2', 'Continuar estudando e trabalhar'),
    ('3', 'Seguir outro plano'),
    ('4', 'Não sei'),
)

ALUNO_3 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_4 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_5 = (
    ('0', '1 pessoa (moro sozinho)'),
    ('1', '2 pessoas'),
    ('2', '3 pessoas'),
    ('3', '4 pessoas'),
    ('4', '5 pessoas'),
    ('5', '6 pessoas'),
    ('6', '7 pessoas'),
    ('7', '8 pessoas'),
    ('8', '9 pessoas'),
    ('9', '10 pessoas ou mais'),
)

ALUNO_6 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_7 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_8 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_9 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_10 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_11 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_12 = (
    ('0', 'Não tem banheiro com chuveiro dentro da minha casa'),
    ('1', '1 banheiro'),
    ('2', '2 banheiros'),
    ('3', '3 banheiros'),
    ('4', '4 banheiros ou mais'),
)

ALUNO_13 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_14 = (
    ('0', '1 a 2 dias por semana'),
    ('1', '3 ou mais dias por semana.'),
)

ALUNO_15 = (
    ('0', 'Minha mãe não estudou'),
    ('1', 'Minha mãe começou o ensino fundamental ou 1o grau, mas não terminou'),
    ('2', 'Minha mãe terminou o ensino fundamental ou 1o grau'),
    ('3', 'Minha mãe começou o ensino médio ou 2o grau, mas não terminou'),
    ('4', 'Minha mãe terminou o ensino médio ou 2o grau'),
    ('5', 'Minha mãe começou a faculdade (ensino superior), mas não terminou'),
    ('6', 'Minha mãe terminou a faculdade (ensino superior)'),
    ('7', 'Não sei'),
)

ALUNO_16 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_17 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_18 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_19 = (
    ('0', 'Sim, todos os dias'),
    ('1', 'Sim, 5 a 6 dias por semana'),
    ('2', 'Sim, 3 a 4 dias por semana'),
    ('3', 'Sim, 1 a 2 dias por semana'),
    ('4', 'Raramente'),
    ('5', 'Não'),
)

ALUNO_20 = (
    ('0', 'Sim, todos os dias'),
    ('1', 'Sim, 5 a 6 dias por semana'),
    ('2', 'Sim, 3 a 4 dias por semana'),
    ('3', 'Sim, 1 a 2 dias por semana'),
    ('4', 'Raramente'),
    ('5', 'Não'),
)

ALUNO_21 = (
    ('0', 'Sim, todos os dias'),
    ('1', 'Sim, 5 a 6 dias por semana'),
    ('2', 'Sim, 3 a 4 dias por semana'),
    ('3', 'Sim, 1 a 2 dias por semana'),
    ('4', 'Raramente'),
    ('5', 'Não'),
)

ALUNO_22 = (
    ('0', 'Sim'),
    ('1', 'Não'),
    ('2', 'Não sei'),
)

ALUNO_23 = (
    ('0', 'Sim, todos os dias'),
    ('1', 'Sim, 3 a 4 dias por semana'),
    ('2', 'Sim, 1 a 2 dias por semana'),
    ('3', 'Raramente'),
    ('4', 'Não'),
)

ALUNO_24 = (
    ('0', 'Nunca'),
    ('1', 'Raramente'),
    ('2', 'Às vezes'),
    ('3', 'Na maior parte das vezes'),
    ('4', 'Sempre'),
)

ALUNO_25 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_26 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_27 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_28 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_29 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_30 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_31 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_32 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_33 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_34 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_35 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_36 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_37 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_38 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_39 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_40 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_41 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_42 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_43 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_44 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_45 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_46 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_47 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_48 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_49 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_50 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_51 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_52 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_53 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_54 = (
    ('0', 'Nunca ou menos de uma vez por mês'),
    ('1', '1 a 3 vezes por mês'),
    ('2', '1 vez por semana'),
    ('3', '2 a 4 vezes por semana'),
    ('4', '6 a 8 vezes por semana'),
    ('5', '1 vez por dia'),
    ('6', '2 a 3 vezes por dia'),
    ('7', '4 a 6 vezes por dia'),
    ('8', 'Mais de 8 vezes por dia'),
)

ALUNO_55 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_56 = (
    ('0', 'Não. Meu filho nunca foi alimentado apenas de leite materno'),
    ('1', 'Sim. Meu filho foi alimentado apenas de leite materno:'),
    ('2', 'Até um mês ou menos;'),
    ('3', 'Até 2 meses;'),
    ('4', 'Até 3 meses;'),
    ('5', 'Até 4 meses;'),
    ('6', 'Até 5 meses;'),
    ('7', 'Até 6 meses ou mais.'),
)

ALUNO_57 = (
    ('0', 'Até 6 meses de idade;'),
    ('1', 'Até 7 meses de idade;'),
    ('2', 'Até 8 meses de idade;'),
    ('3', 'Até 9 meses de idade;'),
    ('4', 'Até 10 meses de idade;'),
    ('5', 'Até 11 meses de idade;'),
    ('6', 'Até 12 meses de idade;'),
    ('7', 'Mais de 12 meses até 18 meses de idade;'),
    ('8', 'Mais de 18 meses até 24 meses de idade.'),
)

ALUNO_58 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_59 = (
    ('0', 'Até um mês ou menos;'),
    ('1', 'Até 2 meses;'),
    ('2', 'Até 3 meses;'),
    ('3', 'Até 4 meses;'),
    ('4', 'Até 5 meses;'),
    ('5', 'Até 6 meses ou mais;'),
    ('6', 'Até 7 meses de idade;'),
    ('7', 'Até 8 meses de idade;'),
    ('8', 'Até 9 meses de idade;'),
    ('9', 'Até 10 meses de idade;'),
    ('10', 'Até 11 meses de idade;'),
    ('11', 'Até 12 meses de idade;'),
    ('12', 'Mais de 12 meses até 18 meses de idade;'),
    ('13', 'Mais de 18 meses até 24 meses de idade.'),
)

ALUNO_60 = (
    ('0', 'Leite + papinhas'),
    ('1', 'Leite + sopas'),
    ('2', 'Leite + frutas'),
)

ALUNO_61 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_62 = (
    ('1', 'Menos de 1 mês'),
    ('2', '1 e menos de 2 meses;'),
    ('3', '2 e menos de 3 meses'),
    ('4', '3 e menos de 4 meses;'),
    ('5', '4 e menos de 5 meses;'),
    ('6', '5 e menos de 6 meses'),
    ('7', '6 e menos de 7 meses;'),
    ('8', '7 e menos de 8 meses;'),
    ('9', '8 e menos de 9 meses;'),
    ('10', '9 e menos de 10 meses'),
    ('11', '10 e menos de 11 meses;'),
    ('12', '11 e menos de 12 meses;'),
    ('13', '12 e menos de 18 meses de idade;'),
    ('14', '18 e menos 24 meses de idade.'),
)

ALUNO_63 = (
    ('0', 'Nenhum dia nos últimos 7 dias (0 dia)'),
    ('1', '1 dia nos últimos 7 dias'),
    ('2', '2 dias nos últimos 7 dias'),
    ('3', '3 dias nos últimos 7 dias'),
    ('4', '4 dias nos últimos 7 dias'),
    ('5', '5 dias nos últimos 7 dias'),
    ('6', '5 dias mais sábado, nos últimos 7 dias'),
    ('7', '5 dias mais sábado e domingo, nos últimos 7 dias'),
)

ALUNO_64 = (
    ('0', 'Menos de 10 minutos por dia'),
    ('1', '10 a 19 minutos por dia'),
    ('2', '20 a 29 minutos por dia'),
    ('3', '30 a 39 minutos por dia'),
    ('4', '40 a 49 minutos por dia'),
    ('5', '50 a 59 minutos por dia'),
    ('6', '1 hora ou mais por dia'),
)

ALUNO_65 = (
    ('0', 'Nenhum dia nos últimos 7 dias (0 dia)'),
    ('1', '1 dia nos últimos 7 dias'),
    ('2', '2 dias nos últimos 7 dias'),
    ('3', '3 dias nos últimos 7 dias'),
    ('4', '4 dias nos últimos 7 dias'),
    ('5', '5 dias nos últimos 7 dias'),
    ('6', '5 dias mais sábado, nos últimos 7 dias'),
    ('7', '5 dias mais sábado e domingo, nos últimos 7 dias'),
)

ALUNO_66 = (
    ('0', 'Não fiz aula de educação física na escola nos últimos 7 dias.'),
    ('1', 'Menos de 10 minutos por dia'),
    ('2', '10 a 19 minutos por dia'),
    ('3', '20 a 29 minutos por dia'),
    ('4', '30 a 39 minutos por dia'),
    ('5', '40 a 49 minutos por dia'),
    ('6', '50 a 59 minutos por dia'),
    ('7', '1 hora ou mais por dia'),
)

ALUNO_67 = (
    ('0', 'Nenhum dia nos últimos 7 dias (0 dia)'),
    ('1', '1 dia nos últimos 7 dias'),
    ('2', '2 dias nos últimos 7 dias'),
    ('3', '3 dias nos últimos 7 dias'),
    ('4', '4 dias nos últimos 7 dias'),
    ('5', '5 dias nos últimos 7 dias'),
    ('6', '5 dias mais sábado, nos últimos 7 dias'),
    ('7', '5 dias mais sábado e domingo, nos últimos 7 dias'),
)

ALUNO_68 = (
    ('0', 'Menos de 10 minutos por dia'),
    ('1', '10 a 19 minutos por dia'),
    ('2', '20 a 29 minutos por dia'),
    ('3', '30 a 39 minutos por dia'),
    ('4', '40 a 49 minutos por dia'),
    ('5', '50 a 59 minutos por dia'),
    ('6', '1 hora ou mais por dia'),
)

ALUNO_69 = (
    ('0', 'Nenhum dia nos últimos 7 dias (0 dia)'),
    ('1', '1 dia nos últimos 7 dias'),
    ('2', '2 dias nos últimos 7 dias'),
    ('3', '3 dias nos últimos 7 dias'),
    ('4', '4 dias nos últimos 7 dias'),
    ('5', '5 dias nos últimos 7 dias'),
    ('6', '5 dias mais sábado, nos últimos 7 dias'),
    ('7', '5 dias mais sábado e domingo, nos últimos 7 dias'),
)

ALUNO_70 = (
    ('0', 'Não faria mesmo assim'),
    ('1', 'Faria atividade física em alguns dias da semana'),
    ('2', 'Faria atividade física na maioria dos dias da semana'),
    ('3', 'Já faço atividade física em alguns dias da semana'),
    ('4', 'Já faço atividade física na maioria dos dias da semana'),
)

ALUNO_71 = (
    ('0', 'Não assisto a TV'),
    ('1', 'Até 1 hora por dia'),
    ('2', 'Mais de 1 hora até 2 horas por dia'),
    ('3', 'Mais de 2 horas até 3 horas por dia'),
    ('4', 'Mais de 3 horas até 4 horas por dia'),
    ('5', 'Mais de 4 horas até 5 horas por dia'),
    ('6', 'Mais de 5 horas até 6 horas por dia'),
    ('7', 'Mais de 6 horas até 7 horas por dia'),
    ('8', 'Mais de 7 horas até 8 horas por dia'),
    ('9', 'Mais de 8 horas por dia'),
)

ALUNO_72 = (
    ('0', 'Até 1 hora por dia'),
    ('1', 'Mais de 1 hora até 2 horas por dia'),
    ('2', 'Mais de 2 horas até 3 horas por dia'),
    ('3', 'Mais de 3 horas até 4 horas por dia'),
    ('4', 'Mais de 4 horas até 5 horas por dia'),
    ('5', 'Mais de 5 horas até 6 horas por dia'),
    ('6', 'Mais de 6 horas até 7 horas por dia'),
    ('7', 'Mais de 7 horas até 8 horas por dia'),
    ('8', 'Mais de 8 horas por dia'),
)

ALUNO_73 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_74 = (
    ('0', '7 anos de idade ou menos'),
    ('1', '8 anos'),
    ('2', '9 anos'),
    ('3', '10 anos'),
    ('4', '11 anos'),
    ('5', '12 anos'),
    ('6', '13 anos'),
    ('7', '14 anos'),
    ('8', '15 anos'),
    ('9', '16 anos'),
    ('10', '17 anos'),
    ('11', '18 anos ou mais'),
)

ALUNO_75 = (
    ('0', 'Nenhum dia nos últimos 30 dias (0 dia)'),
    ('1', '1 ou 2 dias nos últimos 30 dias'),
    ('2', '3 a 5 dias nos últimos 30 dias'),
    ('3', '6 a 9 dias nos últimos 30 dias'),
    ('4', '10 a 19 dias nos últimos 30 dias'),
    ('5', '20 a 29 dias nos últimos 30 dias'),
    ('6', 'Todos os dias nos últimos 30 dias'),
)

ALUNO_76 = (
    ('0', 'Não fumei cigarros nos últimos 30 dias'),
    ('1', 'Eu os comprei numa loja ou botequim'),
    ('2', 'Eu os comprei num vendedor ambulante (camelô)'),
    ('3', 'Dei dinheiro para alguém comprá-los para mim'),
    ('4', 'Eu os pedi a alguém'),
    ('5', 'Eu peguei escondido'),
    ('6', 'Uma pessoa mais velha me deu'),
    ('7', 'Eu os consegui de outro modo'),
)

ALUNO_77 = (
    ('0', 'Não tentei comprar cigarros nos últimos 30 dias;'),
    ('1', 'Sim, alguém se recusou a me vender cigarros por causa de minha idade;'),
    ('2', 'Não, minha idade não me impediu de comprar cigarros.'),
)

ALUNO_78 = (
    ('0', 'Não uso outros produtos de tabaco'),
    ('1', 'Nenhum dia nos últimos 30 dias (0 dia)'),
    ('2', '1 ou 2 dias nos últimos 30 dias'),
    ('3', '3 a 5 dias nos últimos 30 dias'),
    ('4', '6 a 9 dias nos últimos 30 dias'),
    ('5', '10 a 19 dias nos últimos 30 dias'),
    ('6', '20 a 29 dias nos últimos 30 dias'),
    ('7', 'Todos os 30 dias nos últimos 30 dias'),
)

ALUNO_79 = (
    ('0', 'Não usei nenhum produto do tabaco (os produtos do tabaco estão abaixo relacionados)'),
    ('1', 'Cigarros de cravo (conhecidos como cigarros de Bali).'),
    ('2', 'Cigarros enrolados à mão (conhecidos como cigarros de palha ou papel)'),
    ('3', 'Cigarrilhas'),
    ('4', 'Charutos, charutos pequenos.'),
    ('5', 'Fumo para mascar'),
    ('6', 'Narguilé (cachimbo de água)'),
    ('7', 'Cigarros indianos (bidis)'),
    ('8', 'Cigarro eletrônico (e-cigarette)'),
    ('9', 'Outros'),
)

ALUNO_80 = (
    ('0', 'Nenhum dia nos últimos 7 dias (0 dia)'),
    ('1', '1 ou 2 dias nos últimos 7 dias'),
    ('2', '3 ou 4 dias nos últimos 7 dias'),
    ('3', '5 ou 6 dias nos últimos 7 dias'),
    ('4', 'Todos os 7 dias'),
)

ALUNO_81 = (
    ('0', 'Nenhum deles'),
    ('1', 'Só meu pai ou responsável do sexo masculino'),
    ('2', 'Só minha mãe ou responsável do sexo feminino'),
    ('3', 'Meu pai e minha mãe ou responsáveis'),
    ('4', 'Não sei'),
)

ALUNO_82 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_83 = (
    ('0', '7 anos de idade ou menos'),
    ('1', '8 anos'),
    ('2', '9 anos'),
    ('3', '10 anos'),
    ('4', '11 anos'),
    ('5', '12 anos'),
    ('6', '13 anos'),
    ('7', '14 anos'),
    ('8', '15 anos'),
    ('9', '16 anos'),
    ('10', '17 anos'),
    ('11', '18 anos ou mais'),
)

ALUNO_84 = (
    ('0', 'Nenhum dia nos últimos 30 dias (0 dia)'),
    ('1', '1 ou 2 dias nos últimos 30 dias'),
    ('2', '3 a 5 dias nos últimos 30 dias'),
    ('3', '6 a 9 dias nos últimos 30 dias'),
    ('4', '10 a 19 dias nos últimos 30 dias'),
    ('5', '20 a 29 dias nos últimos 30 dias'),
    ('6', 'Todos os dias nos últimos 30 dias'),
)

ALUNO_85 = (
    ('0', 'Não tomei nenhuma bebida alcoólica nos últimos 30 dias (0 dia)'),
    ('1', 'Menos de um copo ou dose nos últimos 30 dias'),
    ('2', '1 copo ou 1 dose nos últimos 30 dias'),
    ('3', '2 copos ou 2 doses nos últimos 30 dias'),
    ('4', '3 copos ou 3 doses nos últimos 30 dias'),
    ('5', '4 copos ou 4 doses nos últimos 30 dias'),
    ('6', '5 copos ou mais ou 5 doses ou mais nos últimos 30 dias'),
)

ALUNO_86 = (
    ('0', 'Não tomei nenhuma bebida alcoólica nos últimos 30 dias (0 dia)'),
    ('1', 'Comprei no mercado, loja, bar ou supermercado'),
    ('2', 'Comprei de um vendedor de rua'),
    ('3', 'Dei dinheiro a alguém que comprou para mim'),
    ('4', 'Consegui com meus amigos'),
    ('5', 'Peguei na minha casa sem permissão'),
    ('6', 'Consegui com alguém em minha família'),
    ('7', 'Em uma festa'),
    ('8', 'Consegui de outro modo'),
)

ALUNO_87 = (
    ('0', 'Nenhuma vez na vida (0 vez)'),
    ('1', '1 ou 2 vezes na vida'),
    ('2', '3 a 5 vezes na vida'),
    ('3', '6 a 9 vezes na vida'),
    ('4', '10 ou mais vezes na vida'),
)

ALUNO_88 = (
    ('0', 'Nenhuma vez na vida (0 vez)'),
    ('1', '1 ou 2 vezes na vida'),
    ('2', '3 a 5 vezes na vida'),
    ('3', '6 a 9 vezes na vida'),
    ('4', '10 ou mais vezes na vida'),
)

ALUNO_89 = (
    ('0', 'Nenhum'),
    ('1', 'Poucos'),
    ('2', 'Alguns'),
    ('3', 'A maioria'),
    ('4', 'Todos'),
    ('5', 'Não sei'),
)

ALUNO_90 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_91 = (
    ('0', '7 anos ou menos'),
    ('1', '8 anos'),
    ('2', '9 anos'),
    ('3', '10 anos'),
    ('4', '11 anos'),
    ('5', '12 anos'),
    ('6', '13 anos'),
    ('7', '14 anos'),
    ('8', '15 anos'),
    ('9', '16 anos'),
    ('10', '17 anos'),
    ('11', '18 anos ou mais'),
)

ALUNO_92 = (
    ('0', 'Nenhum dia nos últimos 30 dias (0 dia)'),
    ('1', '1 ou 2 dias nos últimos 30 dias'),
    ('2', '3 a 5 dias nos últimos 30 dias'),
    ('3', '6 a 9 dias nos últimos 30 dias'),
    ('4', '10 ou mais dias nos últimos 30 dias'),
)

ALUNO_93 = (
    ('0', 'Nenhum dia nos últimos 30 dias (0 dia)'),
    ('1', '1 ou 2 dias nos últimos 30 dias'),
    ('2', '3 a 5 dias nos últimos 30 dias'),
    ('3', '6 a 9 dias nos últimos 30 dias'),
    ('4', '10 ou mais dias nos últimos 30 dias'),
)

ALUNO_94 = (
    ('0', 'Nenhum dia nos últimos 30 dias (0 dia)'),
    ('1', '1 ou 2 dias nos últimos 30 dias'),
    ('2', '3 a 5 dias nos últimos 30 dias'),
    ('3', '6 a 9 dias nos últimos 30 dias'),
    ('4', '10 ou mais dias nos últimos 30 dias'),
)

ALUNO_95 = (
    ('0', 'Nenhum'),
    ('1', 'Poucos'),
    ('2', 'Alguns'),
    ('3', 'A maioria'),
    ('4', 'Todos'),
    ('5', 'Não sei'),
)

ALUNO_96 = (
    ('0', 'Nenhum dia nos últimos 30 dias (0 dia)'),
    ('1', '1 ou 2 dias nos últimos 30 dias'),
    ('2', '3 a 5 dias nos últimos 30 dias'),
    ('3', '6 a 9 dias nos últimos 30 dias'),
    ('4', '10 ou mais dias nos últimos 30 dias'),
)

ALUNO_97 = (
    ('0', 'Nunca'),
    ('1', 'Raramente'),
    ('2', 'Às vezes'),
    ('3', 'Na maior parte do tempo'),
    ('4', 'Sempre'),
)

ALUNO_98 = (
    ('0', 'Nunca'),
    ('1', 'Raramente'),
    ('2', 'Às vezes'),
    ('3', 'Na maior parte do tempo'),
    ('4', 'Sempre'),
)

ALUNO_99 = (
    ('0', 'Nunca'),
    ('1', 'Raramente'),
    ('2', 'Às vezes'),
    ('3', 'Na maior parte do tempo'),
    ('4', 'Sempre'),
)

ALUNO_100 = (
    ('0', 'Nunca'),
    ('1', 'Raramente'),
    ('2', 'Às vezes'),
    ('3', 'Na maior parte do tempo'),
    ('4', 'Sempre'),
)

ALUNO_101 = (
    ('0', 'Nunca'),
    ('1', 'Raramente'),
    ('2', 'Às vezes'),
    ('3', 'Na maior parte do tempo'),
    ('4', 'Sempre'),
)

ALUNO_102 = (
    ('0', 'Nunca'),
    ('1', 'Raramente'),
    ('2', 'Às vezes'),
    ('3', 'Na maior parte do tempo'),
    ('4', 'Sempre'),
)

ALUNO_103 = (
    ('0', 'A minha cor ou raça'),
    ('1', 'A minha religião'),
    ('2', 'A aparência do meu rosto'),
    ('3', 'A aparência do meu corpo'),
    ('4', 'A minha orientação sexual'),
    ('5', 'A minha região de origem'),
    ('6', 'Outros motivos/causas'),
)

ALUNO_104 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_105 = (
    ('0', 'Sim'),
    ('1', 'Não'),
    ('2', 'Não sei o que é bullying'),
    ('3', 'Sempre'),
)

ALUNO_106 = (
    ('0', 'Nunca'),
    ('1', 'Raramente'),
    ('2', 'Às vezes'),
    ('3', 'Na maioria das vezes'),
    ('4', 'Sempre'),
)

ALUNO_107 = (
    ('0', 'Nenhum amigo (0)'),
    ('1', '1 amigo'),
    ('2', '2 amigos'),
    ('3', '3 ou mais amigos'),
)

ALUNO_108 = (
    ('0', 'Nunca'),
    ('1', 'Raramente'),
    ('2', 'Às vezes'),
    ('3', 'Na maioria das vezes'),
    ('4', 'Sempre'),
)

ALUNO_109 = (
    ('0', 'Nunca'),
    ('1', 'Raramente'),
    ('2', 'Às vezes'),
    ('3', 'Na maioria das vezes'),
    ('4', 'Sempre'),
)

ALUNO_110 = (
    ('0', 'Nunca'),
    ('1', 'Raramente'),
    ('2', 'Às vezes'),
    ('3', 'Na maioria das vezes'),
    ('4', 'Sempre'),
)

ALUNO_111 = (
    ('0', 'Não escovei meus dentes nos últimos 30 dias'),
    ('1', 'Não escovei meus dentes diariamente'),
    ('2', '1 vez por dia nos últimos 30 dias'),
    ('3', '2 vezes por dia nos últimos 30 dias'),
    ('4', '3 vezes por dia nos últimos 30 dias'),
    ('5', '4 ou mais vezes por dia nos últimos 30 dias'),
)

ALUNO_112 = (
    ('0', 'Sim'),
    ('1', 'Não'),
    ('2', 'Não sei / não me lembro'),
)

ALUNO_113 = (
    ('0', 'Nenhuma vez nos últimos 12 meses (0 vez)'),
    ('1', '1 vez nos últimos 12 meses'),
    ('2', '2 vezes nos últimos 12 meses'),
    ('3', '3 ou mais vezes nos últimos 12 meses'),
)

ALUNO_114 = (
    ('0', 'Nenhum dia nos últimos 30 dias (0 dia)'),
    ('1', '1 dia nos últimos 30 dias'),
    ('2', '2 dias nos últimos 30 dias'),
    ('3', '3 dias nos últimos 30 dias'),
    ('4', '4 dias nos últimos 30 dias'),
    ('5', '5 dias ou mais nos últimos 30 dias'),
)

ALUNO_115 = (
    ('0', 'Nenhum dia nos últimos 30 dias (0 dia)'),
    ('1', '1 dia nos últimos 30 dias'),
    ('2', '2 dias nos últimos 30 dias'),
    ('3', '3 dias nos últimos 30 dias'),
    ('4', '4 dias nos últimos 30 dias'),
    ('5', '5 dias ou mais nos últimos 30 dias'),
)

ALUNO_116 = (
    ('0', 'Não andei nesse tipo de veículo no banco da frente nos últimos 30 dias'),
    ('1', 'Nunca uso cinto de segurança'),
    ('2', 'Raramente'),
    ('3', 'Às vezes'),
    ('4', 'Na maior parte do tempo'),
    ('5', 'Sempre'),
)

ALUNO_117 = (
    ('0', 'Não andei de motocicleta nos últimos 30 dias.'),
    ('1', 'Nunca uso capacete'),
    ('2', 'Raramente'),
    ('3', 'Às vezes'),
    ('4', 'Na maior parte do tempo'),
    ('5', 'Sempre'),
)

ALUNO_118 = (
    ('0', 'Nenhuma vez nos últimos 30 dias (0 vez)'),
    ('1', '1 vez nos últimos 30 dias'),
    ('2', '2 ou 3 vezes nos últimos 30 dias'),
    ('3', '4 ou 5 vezes nos últimos 30 dias'),
    ('4', '6 ou mais vezes nos últimos 30 dias'),
)

ALUNO_119 = (
    ('0', 'Nenhuma vez nos últimos 30 dias (0 vez)'),
    ('1', '1 vez nos últimos 30 dias'),
    ('2', '2 ou 3 vezes nos últimos 30 dias'),
    ('3', '4 ou 5 vezes nos últimos 30 dias'),
    ('4', '6 ou mais vezes nos últimos 30 dias'),
)

ALUNO_120 = (
    ('0', 'Nenhuma vez nos últimos 30 dias (0 vez)'),
    ('1', '1 vez nos últimos 30 dias'),
    ('2', '2 ou 3 vezes nos últimos 30 dias'),
    ('3', '4 ou 5 vezes nos últimos 30 dias'),
    ('4', '6 ou 7 vezes nos últimos 30 dias'),
    ('5', '8 ou 9 vezes nos últimos 30 dias'),
    ('6', '10 ou 11 vezes nos últimos 30 dias'),
    ('7', '12 vezes ou mais nos últimos 30 dias'),
)

ALUNO_121 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_122 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_123 = (
    ('0', 'Nenhuma vez nos últimos 12 meses (0 vez)'),
    ('1', '1 vez nos últimos 12 meses'),
    ('2', '2 a 3 vezes nos últimos 12 meses'),
    ('3', '4 a 5 vezes nos últimos 12 meses'),
    ('4', '6 a 7 vezes nos últimos 12 meses'),
    ('5', '8 a 9 vezes nos últimos 12 meses'),
    ('6', '10 a 11 vezes nos últimos 12 meses'),
    ('7', '12 ou mais vezes nos últimos 12 meses'),
)

ALUNO_124 = (
    ('0', 'Nenhuma vez nos últimos 12 meses (0 vez)'),
    ('1', '1 vez nos últimos 12 meses'),
    ('2', '2 a 3 vezes nos últimos 12 meses'),
    ('3', '4 a 5 vezes nos últimos 12 meses'),
    ('4', '6 a 7 vezes nos últimos 12 meses'),
    ('5', '8 a 9 vezes nos últimos 12 meses'),
    ('6', '10 a 11 vezes nos últimos 12 meses'),
    ('7', '12 ou mais vezes nos últimos 12 meses'),
)

ALUNO_125 = (
    ('0', 'Nenhuma vez nos últimos 12 meses (0 vez)'),
    ('1', '1 vez nos últimos 12 meses'),
    ('2', '2 a 3 vezes nos últimos 12 meses'),
    ('3', '4 a 5 vezes nos últimos 12 meses'),
    ('4', '6 a 7 vezes nos últimos 12 meses'),
    ('5', '8 a 9 vezes nos últimos 12 meses'),
    ('6', '10 a 11 vezes nos últimos 12 meses'),
    ('7', '12 ou mais vezes nos últimos 12 meses'),
)

ALUNO_126 = (
    ('0', 'Não tive ferimento/lesão séria nos últimos 12 meses'),
    ('1', 'Tive um osso quebrado ou junta deslocada'),
    ('2', 'Tive um corte ou perfuração'),
    ('3', 'Tive um traumatismo ou outra lesão na cabeça ou pescoço e desmaiei ou não consegui respirar'),
    ('4', 'Tive um ferimento à bala (arma de fogo)'),
    ('5', 'Tive uma queimadura grave'),
    ('6', 'Fui envenenado(a) ou tive overdose (consumi drogas em excesso)'),
    ('7', 'Tive outra lesão ou machucado'),
)

ALUNO_127 = (
    ('0', 'Foi um acidente ou atropelamento causado por veículo motorizado'),
    ('1', 'Foi algo que caiu sobre mim ou me atingiu'),
    ('2', 'Foi um ataque que sofri ou briga com alguém (com ou sem uso de arma)'),
    ('3', 'Foi um incêndio ou a proximidade com algo quente'),
    ('4', 'Foi a inalação ou algo que engoli e me fez mal'),
    ('5', 'Foi praticando alguma atividade física/exercício/esporte'),
    ('6', 'Foi um acidente que sofri quando estava trabalhando'),
    ('7', 'Foi um acidente enquanto andava de bicicleta'),
    ('8', 'Foi uma queda'),
    ('9', 'Foi outra causa'),
)

ALUNO_128 = (
    ('0', 'Não andei de bicicleta nos últimos 12 meses'),
    ('1', 'Andei de bicicleta e não sofri acidente'),
    ('2', 'Andei de bicicleta e sofri acidente'),
)

ALUNO_129 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_130 = (
    ('0', 'Namorado(a)/ex-namorado(a)'),
    ('1', 'Amigo(a)'),
    ('2', 'Pai/mãe/padrasto/madrasta'),
    ('3', 'Outros familiares'),
    ('4', 'Desconhecido(a)'),
    ('5', 'Outro (as)'),
)

ALUNO_131 = (
    ('0', 'Muito bom'),
    ('1', 'Bom'),
    ('2', 'Regular'),
    ('3', 'Ruim'),
    ('4', 'Muito ruim'),
)

ALUNO_132 = (
    ('0', 'Não faltei a escola nos últimos 12 meses por motivos de saúde'),
    ('1', '1 a 3 dias nos últimos 12 meses'),
    ('2', '4 a 7 dias nos últimos 12 meses'),
    ('3', '8 a 15 dias nos últimos 12 meses'),
    ('4', '16 dias ou mais nos últimos 12 meses'),
)

ALUNO_133 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_134 = (
    ('0', 'Unidade Básica de Saúde (Centro ou Posto de saúde ou Unidade de Saúde da Família/PSF)'),
    ('1', 'Consultório médico particular ou clínica particular'),
    ('2', 'Consultório odontológico'),
    ('3', 'Consultório de outro profissional de saúde (fonoaudiólogo, psicólogo etc.)'),
    ('4', 'Serviço de especialidades médicas ou Policlínica'),
    ('5', 'Pronto-socorro, emergência ou UPA'),
    ('6', 'Hospital'),
    ('7', 'Laboratório ou clínica para exames complementares'),
    ('8', 'Serviço de atendimento domiciliar'),
    ('9', 'Farmácia'),
    ('10', 'Outro'),
)

ALUNO_135 = (
    ('0', 'Sim'),
    ('1', 'Não'),
    ('2', 'Não procurei uma Unidade Básica de Saúde'),
)

ALUNO_136 = (
    ('0', 'Apoio para controle de peso (ganhar ou perder)'),
    ('1', 'Apoio para parar de fumar'),
    ('2', 'Acidente ou lesão'),
    ('3', 'Reabilitação ou terapia'),
    ('4', 'Doença'),
    ('5', 'Problema odontológico'),
    ('6', 'Vacinação'),
    ('7', 'Consulta para métodos contraceptivos (preservativos, pílula, DIU etc.)'),
    ('8', 'Buscar contracepção de emergência (pílula do dia seguinte)'),
    ('9', 'Teste para HIV, Sífilis ou Hepatite B'),
    ('10', 'Pré-natal / Teste para gravidez'),
    ('11', 'Solicitação de atestado médico'),
    ('12', 'Outro'),
)

ALUNO_137 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_138 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_139 = (
    ('0', 'Muito importante'),
    ('1', 'Importante'),
    ('2', 'Pouco importante'),
    ('3', 'Sem importância'),
)

ALUNO_140 = (
    ('0', 'Muito satisfeito(a)'),
    ('1', 'Satisfeito(a)'),
    ('2', 'Indiferente'),
    ('3', 'Insatisfeito(a)'),
    ('4', 'Muito insatisfeito(a)'),
)

ALUNO_141 = (
    ('0', 'Muito magro(a)'),
    ('1', 'Magro(a)'),
    ('2', 'Normal'),
    ('3', 'Gordo(a)'),
    ('4', 'Muito Gordo(a)'),
)

ALUNO_142 = (
    ('0', 'Não estou fazendo nada'),
    ('1', 'Estou tentando perder peso'),
    ('2', 'Estou tentando ganhar peso'),
    ('3', 'Estou tentando manter o mesmo peso'),
)

ALUNO_143 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_144 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_145 = (
    ('0', 'Sim'),
    ('1', 'Não'),
)

ALUNO_146 = (
    ('0', 'Fácil'),
    ('1', 'Difícil'),
    ('2', 'Chato'),
    ('3', 'Legal'),
    ('4', 'Interessante'),
    ('5', 'Informativo'),
    ('6', 'Cansativo'),
    ('7', 'Constrangedor'),
)

# Diretor


DIRETOR_1 = (

)

DIRETOR_2 = (

)

DIRETOR_3 = (

)

DIRETOR_4 = (

)

DIRETOR_5 = (

)

DIRETOR_6 = (

)

DIRETOR_7 = (

)

DIRETOR_8 = (

)

DIRETOR_9 = (

)

DIRETOR_10 = (

)

DIRETOR_11 = (

)

DIRETOR_12 = (

)

DIRETOR_13 = (

)

DIRETOR_14 = (

)

DIRETOR_15 = (

)

DIRETOR_16 = (

)

DIRETOR_17 = (

)

DIRETOR_18 = (

)

DIRETOR_19 = (

)

DIRETOR_20 = (

)

DIRETOR_21 = (

)

DIRETOR_22 = (

)

DIRETOR_23 = (

)

DIRETOR_24 = (

)

DIRETOR_25 = (

)

DIRETOR_26 = (

)

DIRETOR_27 = (

)

DIRETOR_28 = (

)

DIRETOR_29 = (

)

DIRETOR_30 = (

)

DIRETOR_31 = (

)

DIRETOR_32 = (

)

DIRETOR_33 = (

)

DIRETOR_34 = (

)

DIRETOR_35 = (

)

DIRETOR_36 = (

)

DIRETOR_37 = (

)

DIRETOR_38 = (

)

DIRETOR_39 = (

)

DIRETOR_40 = (

)

DIRETOR_41 = (

)

DIRETOR_42 = (

)

DIRETOR_43 = (

)

DIRETOR_44 = (

)

DIRETOR_45 = (

)

DIRETOR_46 = (

)

DIRETOR_47 = (

)

DIRETOR_48 = (

)

DIRETOR_49 = (

)

DIRETOR_50 = (

)

DIRETOR_51 = (

)

DIRETOR_52 = (

)

DIRETOR_53 = (

)

DIRETOR_54 = (

)

DIRETOR_55 = (

)

DIRETOR_56 = (

)

DIRETOR_57 = (

)

DIRETOR_58 = (

)

DIRETOR_59 = (

)

DIRETOR_60 = (

)

DIRETOR_61 = (

)

DIRETOR_62 = (

)

DIRETOR_63 = (

)

DIRETOR_64 = (

)

DIRETOR_65 = (

)

DIRETOR_66 = (

)

DIRETOR_67 = (

)

DIRETOR_68 = (

)

DIRETOR_69 = (

)

DIRETOR_70 = (

)

DIRETOR_71 = (

)

DIRETOR_72 = (

)

DIRETOR_73 = (

)

DIRETOR_74 = (

)

DIRETOR_75 = (

)

DIRETOR_76 = (

)

DIRETOR_77 = (

)

DIRETOR_78 = (

)

DIRETOR_79 = (

)

DIRETOR_80 = (

)

DIRETOR_81 = (

)

DIRETOR_82 = (

)

DIRETOR_83 = (

)

DIRETOR_84 = (

)
