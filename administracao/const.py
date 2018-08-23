# Constantes globais

TAMANHO_NOMES = 200
TAMANHO_OPCOES = 2
TAMANHO_CODIGOS = 5


# Constantes do modelo Aluno

SEXO = (
    ('0', 'Feminino'),
    ('1', 'Masculino')
)

ESCOLA = (
    ('0', 'Escola municipal Antônio Carlos Jobim'),
    ('1', 'Escola municipal Antônio G. de Carvalho Filho'),
    ('2', 'Escola municipal Anne Frank'),
    ('3', 'Escola municipal Darcy Ribeiro'),
    ('4', 'Escola municipal Henrique Talone Pinheiro'),
    ('5', 'Escola municipal de T.I. Vinícius de Moraes'),
    ('6', 'Escola municipal Beatriz Rodrigues da Silva'),
    ('7', 'Escola municipal Mestre Pacífico S. Campos'),
    ('8', 'Escola municipal Luiz Gonzaga'),
    ('9', 'Escola municipal de T.I. Padre Josimo M. Tavares'),
    ('10', 'Escola municipal de T.I. Daniel Batista'),
    ('11', 'Escola municipal de T.I. Monsenhor Pedro P. Piagem'),
    ('12', 'Escola municipal Jorge Amado'),
    ('13', 'Escola municipal Maria Rosa de Castro Sales'),
    ('14', 'Escola municipal Professor Sávia F. Jacome'),
    ('15', 'Escola municipal de T.I. Caroline C. C. da Silva'),
    ('16', 'Escola municipal Aurélio Buarque de Holanda'),
    ('17', 'Escola municipal Maria Júlia Amorim Rodrigues'),
    ('18', 'Escola municipal Thiago Barbosa'),
    ('19', 'Escola municipal de T.I. Euridice F. de Mello'),
    ('20', 'Escola municipal de T.I. Margarida Gonçalves'),
    ('21', 'Escola municipal Crispim Pereira de Alencar'),
    ('22', 'Escola municipal de T.I. Aprigio T. de Matos'),
    ('23', 'Escola municipal de T.I. João Beltrão'),
    ('24', 'Escola municipal de T.I. Luiz Nunes de Oliveira'),
    ('25', 'Escola municipal de T.I. Sueli Pereira A. Reche')
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

QUESTAO1 = (
    ('0', 'Branca'),
    ('1', 'Preta'),
    ('2', 'Amarela'),
    ('3', 'Parda'),
    ('4', 'Indígena')
)

QUESTAO2 = (
    ('0', '11 anos ou menos'),
    ('1', '12 anos'),
    ('2', '13 anos'),
    ('3', '14 anos'),
    ('4', '15 anos'),
    ('5', '16 anos'),
    ('6', '17 anos'),
    ('7', '18 anos'),
    ('8', '19 anos ou mais')
)

QUESTAO3 = (
    ('0', 'Janeiro'),
    ('1', 'Fevereiro'),
    ('2', 'Março'),
    ('3', 'Abril'),
    ('4', 'Maio'),
    ('5', 'Junho'),
    ('6', 'Julho'),
    ('7', 'Agosto'),
    ('8', 'Setembro'),
    ('9', 'Outubro'),
    ('10', 'Novembro'),
    ('11', 'Dezembro')
)

QUESTAO4 = (
    ('0', 'Antes de 1996'),
    ('1', '1996'),
    ('2', '1997'),
    ('3', '1998'),
    ('4', '1999'),
    ('5', '2000'),
    ('6', '2001'),
    ('7', '2002'),
    ('8', '2003'),
    ('9', '2004 ou mais')
)

# Informações gerais

QUESTAO5 = (
    ('0', 'Masculino'),
    ('1', 'Feminino'),
    ('2', 'Auto referenciado.'),
    ('3', 'Prefiro não responder.')
)

QUESTAO6 = (
    ('0', '6o ano / 5a série do Ensino Fundamental'),
    ('1', '7o ano / 6a série do Ensino Fundamental'),
    ('2', '8o ano / 7a série do Ensino Fundamental'),
    ('3', '9o ano / 8a série do Ensino Fundamental'),
    ('4', '1o ano Ensino Médio'),
    ('5', '2o ano Ensino Médio'),
    ('6', '3o ano Ensino Médio')
)

QUESTAO7 = (
    ('0', 'Manhã'),
    ('1', 'Intermediário'),
    ('2', 'Tarde'),
    ('3', 'Noite'),
    ('4', 'Integral')
)

QUESTAO8 = (
    ('0', 'Sim'),
    ('1', 'Não')
)

QUESTAO9 = (
    ('0', 'Sim'),
    ('1', 'Não')
)

QUESTAO10 = (
    ('0', 'Ensino Fundamental'),
    ('1', 'Ensino Médio'),
    ('2', 'Ensino Médio Técnico'),
    ('3', 'Ensino Superior'),
    ('4', 'Pós-graduação'),
    ('5', 'Não sei')
)

QUESTAO11 = (
    ('0', 'Somente continuar estudando'),
    ('1', 'Somente trabalhar'),
    ('2', 'Continuar estudando e trabalhar'),
    ('3', 'Seguir outro plano'),
    ('4', 'Não sei')
)

QUESTAO12 = (
    ('0', 'Sim'),
    ('1', 'Não')
)

QUESTAO13 = (
    ('0', 'Sim'),
    ('1', 'Não')
)

QUESTAO14 = (
    ('0', '1 pessoa (moro sozinho)'),
    ('1', '2 pessoas'),
    ('2', '3 pessoas'),
    ('3', '4 pessoas'),
    ('4', '5 pessoas'),
    ('5', '6 pessoas'),
    ('6', '7 pessoas'),
    ('7', '8 pessoas'),
    ('8', '9 pessoas'),
    ('9', '10 pessoas ou mais')
)

QUESTAO15 = (
    ('0', 'Sim'),
    ('1', 'Não')
)

QUESTAO16 = (
    ('0', 'Sim'),
    ('1', 'Não')
)

QUESTAO17 = (
    ('0', 'Sim'),
    ('1', 'Não')
)

QUESTAO18 = (
    ('0', 'Sim'),
    ('1', 'Não')
)

QUESTAO19 = (
    ('0', 'Sim'),
    ('1', 'Não')
)

QUESTAO20 = (
    ('0', 'Sim'),
    ('1', 'Não')
)

QUESTAO21 = (
    ('0', 'Não tem banheiro com chuveiro dentro da minha casa'),
    ('1', '1 banheiro'),
    ('2', '2 banheiros'),
    ('3', '3 banheiros'),
    ('4', '4 banheiros ou mais')
)

QUESTAO22 = (
    ('0', 'Sim'),
    ('1', 'Não')
)

QUESTAO23 = (
    ('0', 'Minha mãe não estudou'),
    ('1', 'Minha mãe começou o ensino fundamental ou 1o grau, mas não terminou'),
    ('2', 'Minha mãe terminou o ensino fundamental ou 1o grau'),
    ('3', 'Minha mãe começou o ensino médio ou 2o grau, mas não terminou'),
    ('4', 'Minha mãe terminou o ensino médio ou 2o grau'),
    ('5', 'Minha mãe começou a faculdade (ensino superior), mas não terminou'),
    ('6', 'Minha mãe terminou a faculdade (ensino superior)'),
    ('7', 'Não sei')
)

QUESTAO24 = (
    ('0', 'Sim'),
    ('1', 'Não')
)

QUESTAO25 = (
    ('0', 'Sim'),
    ('1', 'Não')
)

QUESTAO26 = (
    ('0', 'Sim'),
    ('1', 'Não')
)

QUESTAO27 = (
    ('0', 'Sim, todos os dias'),
    ('1', 'Sim, 5 a 6 dias por semana'),
    ('2', 'Sim, 3 a 4 dias por semana'),
    ('3', 'Sim, 1 a 2 dias por semana'),
    ('4', 'Raramente'),
    ('5', 'Não')
)

QUESTAO28 = (

)

QUESTAO29 = (

)

QUESTAO30 = (

)

QUESTAO31 = (

)

QUESTAO32 = (

)

QUESTAO33 = (

)

QUESTAO34 = (

)

QUESTAO35 = (

)

QUESTAO36 = (

)

QUESTAO37 = (

)

QUESTAO38 = (

)

QUESTAO39 = (

)

QUESTAO40 = (

)

QUESTAO41 = (

)

QUESTAO42 = (

)

QUESTAO43 = (

)
