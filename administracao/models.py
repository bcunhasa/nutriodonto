from django.db import models


class Campanha(models.Model):
    """Modelo que representa uma campanha de pesquisa"""
    nome = models.CharField(max_length=TAMANHO_NOMES, verbose_name='Nome')

    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.nome


class Acao(models.Model):
    """Modelo que representa uma acao de uma campanha"""
    campanha = models.ForeignKey('Campanha', on_delete=models.CASCADE)
    nome = models.CharField(max_length=TAMANHO_NOMES, verbose_name='Nome')

    class Meta:
        verbose_name = 'Acao'
        verbose_name_plural = 'Acoes'

    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.nome


class Escola(models.Model):
    """Modelo que representa uma escola de uma acao"""
    acao = models.ForeignKey('Acao', on_delete=models.CASCADE)
    nome = models.CharField(choices=ESCOLA, max_length=TAMANHO_NOMES, verbose_name='Nome')

    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.nome


class Aluno(models.Model):
    """Modelo que representa um aluno"""
    escola = models.ForeignKey('Escola', on_delete=models.CASCADE)

    nome = models.CharField(max_length=TAMANHO_NOMES, verbose_name='Nome')
    sexo = models.IntegerField(choices=SEXO, verbose_name='Sexo')
    nascimento = models.DateField(verbose_name="Data de nascimento")
    periodo = models.IntegerField(choices=PERIODO, verbose_name='Período')
    turma = models.IntegerField(choices=TURMA, verbose_name='Turma')
    municipio = models.IntegerField(choices=MUNICIPIO, verbose_name='Município')

    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.nome


class Questionario(models.Model):
    """Modelo que representa um questionário"""
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE)
    
    # Informações pessoais
    questao1 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='1. Qual é a sua cor ou raça?')
    questao2 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='2. Qual é a sua idade?')
    questao3 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='3. Qual é o mês do seu aniversário?')
    questao4 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='4. Em que ano você nasceu?')
    
    # Informações gerais
    questao5 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='5. Qual é o seu gênero?')
    questao6 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='6. Em que ano/série você está?')
    questao7 = models.ArrayField(models.IntegerField(choices=QUESTOES), null=True, verbose_name='7. Em que turno você estuda? (pode ser múltipla escola).')
    questao8 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='8. Você estuda em regime integral (tem atividades escolares por 7 horas ou mais diárias, durante todo o período escolar)?')
    questao9 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='9. Você estuda em regime de internato (a escola possui alojamento onde os alunos permanecem e dormem diariamente, durante todo o período escolar)?')
    questao10 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='10. Qual o grau de escolaridade mais elevado que você pretende concluir?')
    questao11 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='11. Quando terminar o ciclo/curso que você está frequentando atualmente, você pretende?')
    questao12 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='12. Você mora com sua mãe?')
    questao13 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='13. Você mora com seu pai?')
    questao14 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='14. Contando com você, quantas pessoas moram na sua casa ou apartamento?')
    questao15 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='15. Na sua casa tem telefone fixo (convencional)?')
    questao16 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='16. Você tem celular?')
    questao17 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='17. Na sua casa tem computador (de mesa, netbook, laptop etc.)?')
    questao18 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='18. Você tem acesso à internet em sua casa?')
    questao19 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='19. Alguém que mora na sua casa tem carro?')
    questao20 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='20. Alguém que mora na sua casa tem moto?')
    questao21 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='21. Quantos banheiros com chuveiro têm dentro da sua casa?')
    questao22 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='22. Tem empregado(a) doméstico(a) recebendo dinheiro para fazer o trabalho em sua casa, três ou mais dias por semana?')
    questao23 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='23. Qual nível de ensino (grau) sua mãe estudou ou estuda?')
    questao24 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='24. Você tem algum trabalho, emprego ou negócio atualmente?')
    questao25 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='25. Você recebe dinheiro por este trabalho, emprego ou negócio?')
    questao26 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='26. Sua família recebe benefícios do Programa Bolsa Família?')
    
    # Alimentação
    questao27 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='27. Você costuma tomar o café da manhã?')
    questao28 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='28. Você costuma almoçar ou jantar com sua mãe, pai ou responsável?')
    questao29 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='29. Você costuma comer quando está assistindo à TV ou estudando?')
    questao30 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='30. Sua escola oferece comida (merenda escolar/almoço) aos alunos da sua turma? (Não considerar lanches/comida comprados na cantina)')
    questao31 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='31. Você costuma comer a comida (merenda/almoço) oferecida pela escola? (Não considerar lanches/comida comprados na cantina)')
    questao32 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='32. NOS ÚLTIMOS 7 DIAS, em quantos dias você comeu feijão?')
    questao33 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='33. NOS ÚLTIMOS 7 DIAS, em quantos dias você comeu salgados fritos? Exemplo: batata frita (sem contar a batata de pacote) ou salgados fritos como coxinha de galinha, quibe frito, pastel frito, comidas típicas, etc.')
    questao34 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='34. NOS ÚLTIMOS 7 DIAS, em quantos dias você comeu pelo menos um tipo de legume ou verdura? Exemplos: alface, abóbora, brócolis, cebola, cenoura, chuchu, couve, espinafre, pepino, tomate etc. Não inclua batata e aipim (mandioca/macaxeira).')
    questao35 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='35. NOS ÚLTIMOS 7 DIAS, em quantos dias você comeu guloseimas (doces, balas, chocolates, chicletes, bombons ou pirulitos)?')
    questao36 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='36. NOS ÚLTIMOS 7 DIAS, em quantos dias você comeu frutas frescas ou salada de frutas?')
    questao37 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='37. NOS ÚLTIMOS SETE DIAS, em quantos dias você tomou refrigerante?')
    questao38 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='38. NOS ÚLTIMOS SETE DIAS, em quantos dias você comeu alimentos industrializados/ultraprocessados salgados, como hambúrguer, presunto, mortadela, salame, linguiça, salsicha, macarrão instantâneo, salgadinho de pacote, biscoitos salgados?')
    questao39 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='39. NOS ÚLTIMOS SETE DIAS, em quantos dias você comeu em restaurantes fast food, tais como lanchonetes, barracas de cachorro quentes, pizzaria etc.?')
    questao40 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='40. NOS ÚLTIMOS 30 DIAS, com que frequência você ficou com fome por não ter comida suficiente em sua casa?')
    questao41 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='41. NOS ÚLTIMOS 30 DIAS, quantas vezes por dia você normalmente comeu frutas frescas ou salada de frutas?')
    questao42 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='42. NOS ÚLTIMOS 30 DIAS, quantas vezes por dia você normalmente comeu legumes ou verduras, tais como alface, abóbora, brócolis, cebola, cenoura, chuchu, couve, espinafre, pepino, tomate etc.? Não inclua batata e aipim (mandioca/macaxeira)')
    questao43 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='43. NOS ÚLTIMOS 30 DIAS, quantas vezes por dia você tomou refrigerante?')
    
    # Atividade física
    questao44 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='44. NOS ÚLTIMOS 7 DIAS, em quantos dias você FOI a pé ou de bicicleta para a escola?')
    questao45 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='45. Quando você VAI para a escola a pé ou de bicicleta, quanto tempo você gasta?')
    questao46 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='46. NOS ÚLTIMOS 7 DIAS, em quantos dias você VOLTOU a pé ou de bicicleta da escola?')
    questao47 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='47. Quando você VOLTA da escola a pé ou de bicicleta, quanto tempo você gasta?')
    questao48 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='48. NOS ÚLTIMOS 7 DIAS, quantos dias você teve aulas de educação física na escola?')
    questao49 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='49. NOS ÚLTIMOS 7 DIAS, quanto tempo por dia você fez atividade física ou esporte durante as aulas de educação física na escola?')
    questao50 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='50. NOS ÚLTIMOS 7 DIAS, sem contar as aulas de educação física da escola, em quantos dias você praticou alguma atividade física, como esportes, dança, ginástica, musculação, lutas ou outra atividade?')
    questao51 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='51. NORMALMENTE, quanto tempo por dia duram essas atividades (como esportes, dança, ginástica, musculação, lutas ou outra atividade) que você faz? (Sem contar as aulasde educação física)')
    questao52 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='52. NOS ÚLTIMOS 7 DIAS, em quantos dias você fez atividade física por pelo menos 60 minutos (1 hora) por dia? (Some todo o tempo que você gastou em qualquer tipo de atividade física, EM CADA DIA)')
    questao53 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='53. Se você tivesse oportunidade de fazer atividade física na maioria dos dias da semana, qual seria a sua atitude?')
    questao54 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='54. Em um dia de semana comum, quantas horas por dia você assiste a TV? (não contar sábado, domingo e feriado)')
    questao55 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='55. Em um dia de semana comum, quanto tempo você fica sentado(a), assistindo televisão, usando computador, jogando videogame, conversando com amigos(as) ou fazendo outras atividades sentado(a)? (não contar sábado, domingo, feriados e o tempo sentado na escola)')
    
    # Uso de cigarro
    questao56 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='56. Alguma vez na vida, você já fumou cigarro, mesmo uma ou duas tragadas?')
    questao57 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='57. Que idade você tinha quando experimentou fumar cigarro pela primeira vez?')
    questao58 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='58. NOS ÚLTIMOS 30 DIAS, em quantos dias você fumou cigarros?')
    questao59 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='59. NOS ÚLTIMOS 30 DIAS, em geral, como você conseguiu seus próprios cigarros?')
    questao60 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='60. NOS ÚLTIMOS 30 DIAS, alguém se recusou a lhe vender cigarros por causa de sua idade?')
    questao61 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='61. NOS ÚLTIMOS 30 DIAS, em quantos dias você usou outros produtos de tabaco: cigarros de palha ou enrolados a mão, charuto, cachimbo, cigarrilha, cigarro indiano ou bali, narguilé, rapé, fumo de mascar etc.? (não incluir cigarro comum)')
    questao62 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='62. Qual outro produto do tabaco você usou com mais frequência NOS ÚLTIMOS 30 DIAS?')
    questao63 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='63. NOS ÚLTIMOS 7 DIAS, em quantos dias pessoas fumaram na sua presença?')
    questao64 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='64. Algum de seus pais ou responsáveis fuma?')
    questao65 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='65. Primeira dose de bebida alcoólica (uma dose equivale a uma lata de cerveja ou uma taça de vinho ou uma dose de cachaça ou uísque etc.)?')
    
    # Bebidas alcoólicas
    questao66 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='66. Alguma vez na vida você tomou uma dose de bebida alcoólica (uma dose equivale a uma lata de cerveja ou uma taça de vinho ou uma dose de cachaça ou uísque etc.)?')
    questao67 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='67. Que idade você tinha quando tomou a primeira dose de bebida alcoólica (uma dose equivale a uma lata de cerveja ou uma taça de vinho ou uma dose de cachaça ou uísque etc.)?')
    questao68 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='68. NOS ÚLTIMOS 30 DIAS, em quantos dias você tomou pelo menos um copo ou uma dose de bebida alcoólica (uma dose equivale a uma lata de cerveja ou uma taça de vinho ou uma dose de cachaça ou uísque etc.)?')
    questao69 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='69. NOS ÚLTIMOS 30 DIAS, nos dias em que você tomou alguma bebida alcoólica, quantos copos ou doses você tomou por dia?')
    questao70 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='70. NOS ÚLTIMOS 30 DIAS, na maioria das vezes, como você conseguiu a bebida que tomou?')
    questao71 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='71. Na sua vida, quantas vezes você bebeu tanto que ficou realmente bêbado(a)?')
    questao72 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='72. Na sua vida, quantas vezes você teve problemas com sua família ou amigos, perdeu aulas ou brigou por que tinha bebido?')
    questao73 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='73. Quantos amigos seus consomem bebida alcoólica?')
    
    # Drogas ilícitas
    questao74 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='74. Alguma vez na vida, você já usou alguma droga como: maconha, cocaína, crack, cola, loló, lança-perfume, ecstasy, oxy etc.?')
    questao75 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='75. Que idade você tinha quando usou alguma droga como: maconha, cocaína, crack, cola, loló, lança-perfume, ecstasy, oxy ou outra pela primeira vez?')
    questao76 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='76. NOS ÚLTIMOS 30 DIAS, quantos dias você usou droga como maconha, cocaína, crack, cola, loló, lança-perfume, ecstasy, oxy etc.?')
    questao77 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='77. NOS ÚLTIMOS 30 DIAS, quantos dias você usou maconha?')
    questao78 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='78. NOS ÚLTIMOS 30 DIAS, quantos dias você usou crack?')
    questao79 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='79. Quantos amigos seus usam drogas?')
    
    # Situações em casa e na escola
    questao80 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='80. NOS ÚLTIMOS 30 DIAS, em quantos dias você faltou às aulas ou à escola sem permissão dos seus pais ou responsáveis?')
    questao81 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='81. NOS ÚLTIMOS 30 DIAS, com que frequência seus pais ou responsáveis sabiam realmente o que você estava fazendo em seu tempo livre?')
    questao82 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='82. NOS ÚLTIMOS 30 DIAS, com que frequência seus pais ou responsáveis verificaram se os seus deveres de casa (lição de casa) foram feitos?')
    questao83 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='83. NOS ÚLTIMOS 30 DIAS, com que frequência seus pais ou responsáveis entenderam seus problemas e preocupações?')
    questao84 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='84. NOS ÚLTIMOS 30 DIAS, com que frequência seus pais ou responsáveis mexeram em suas coisas sem a sua concordância?')
    questao85 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='85. NOS ÚLTIMOS 30 DIAS, com que frequência os colegas de sua escola trataram você bem e/ou foram prestativos contigo?')
    questao86 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='86. NOS ÚLTIMOS 30 DIAS, com que frequência algum dos seus colegas de escola te esculacharam, zoaram, mangaram, intimidaram ou caçoaram tanto que você ficou magoado, incomodado, aborrecido, ofendido ou humilhado?')
    questao87 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='87. NOS ÚLTIMOS 30 DIAS, qual o motivo/causa de seus colegas terem te esculachado, zombado, zoado, caçoado, mangado, intimidado ou humilhado?')
    questao88 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='88. NOS ÚLTIMOS 30 DIAS, você esculachou, zombou, mangou, intimidou ou caçoou algum de seus colegas da escola tanto que ele ficou magoado, aborrecido, ofendido ou humilhado?')
    questao89 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='89. Você já sofreu bullying?')
    questao90 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='90. NOS ÚLTIMOS 12 MESES, com que frequência você não conseguiu dormir à noite porque algo o(a) preocupava muito?')
    questao91 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='91. Quantos amigos(as) próximos você tem?')
    
    # Higiene e saúde bucal
    questao92 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='92. NOS ÚLTIMOS 30 DIAS, com que frequência você lavou as mãos antes de comer?')
    questao93 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='93. NOS ÚLTIMOS 30 DIAS, com que frequência você lavou as mãos após usar o banheiro ou o vaso sanitário?')
    questao94 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='94. NOS ÚLTIMOS 30 DIAS, com que frequência você usou sabão ou sabonete quando lavou suas mãos?')
    questao95 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='95. NOS ÚLTIMOS 30 DIAS, quantas vezes por dia você usualmente escovou os dentes?')
    questao96 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='96. NOS ÚLTIMOS 06 MESES, você teve dor de dente? (excluir dor de dente causada por uso de aparelho)')
    questao97 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='97. NOS ÚLTIMOS 12 MESES, quantas vezes você foi ao dentista?')
    
    # Segurança
    questao98 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='98. NOS ÚLTIMOS 30 DIAS, em quantos dias você deixou de ir à escola porque não se sentia seguro no caminho de casa para a escola ou da escola para casa?')
    questao99 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='99. NOS ÚLTIMOS 30 DIAS, em quantos dias você não foi à escola porque não se sentia seguro na escola?')
    questao100 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='100. NOS ÚLTIMOS 30 DIAS, com que frequência você usou cinto de segurança enquanto andava como passageiro(a) NO BANCO DA FRENTE de carro/automóvel, van ou táxi?')
    questao101 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='101. NOS ÚLTIMOS 30 DIAS, com que frequência você usou capacete ao andar de motocicleta?')
    questao102 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='102. NOS ÚLTIMOS 30 DIAS, quantas vezes você dirigiu um veículo motorizado de transporte (carro, motocicleta, voadeira, barco)?')
    questao103 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='103. NOS ÚLTIMOS 30 DIAS, quantas vezes você andou em carro ou outro veículo motorizado dirigido por alguém que tinha consumido alguma bebida alcoólica?')
    questao104 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='104. NOS ÚLTIMOS 30 DIAS, quantas vezes você foi agredido(a) fisicamente por um adulto da sua família?')
    questao105 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='105. NOS ÚLTIMOS 30 DIAS, você esteve envolvido(a) em alguma briga em que alguma pessoa usou arma de fogo, como revólver ou espingarda?')
    questao106 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='106. NOS ÚLTIMOS 30 DIAS, você esteve envolvido(a) em alguma briga em que alguma pessoa usou alguma outra arma como faca, canivete, peixeira, pedra, pedaço de pau ou garrafa?')
    questao107 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='107. NOS ÚLTIMOS 12 MESES, quantas vezes você foi agredido(a) fisicamente?')
    questao108 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='108. NOS ÚLTIMOS 12 MESES, quantas vezes você se envolveu em briga (uma luta física)?')
    questao109 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='109. NOS ÚLTIMOS 12 MESES, quantas vezes você foi seriamente ferido(a)?')
    questao110 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='110. NOS ÚLTIMOS 12 MESES, qual foi o ferimento ou a lesão MAIS SÉRIA que aconteceu com você?')
    questao111 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='111. NOS ÚLTIMOS 12 MESES, qual foi a PRINCIPAL CAUSA do ferimento ou da lesão mais séria que aconteceu com você?')
    questao112 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='112. NOS ÚLTIMOS 12 MESES, você sofreu algum acidente de bicicleta (caiu e se machucou)?')
    questao113 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='113. Alguma vez na vida você foi forçado(a) a ter relação sexual?')
    questao114 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='114. Quem forçou você a ter relação sexual?')
    
    # Uso de serviço de saúde
    questao115 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='115. Como você classificaria seu estado de saúde?')
    questao116 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='116. NOS ÚLTIMOS 12 MESES, quantos dias você faltou a escola por motivo(s) relacionado(s) à sua saúde?')
    questao117 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='117. NOS ÚLTIMOS 12 MESES você procurou algum serviço ou profissional de saúde para atendimento relacionado à própria saúde?')
    questao118 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='118. NOS ÚLTIMOS 12 MESES, qual foi o serviço de saúde que você procurou com MAIS FREQUÊNCIA?')
    questao119 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='119. Você foi atendido(a) NA ÚLTIMA VEZ que procurou alguma Unidade Básica de Saúde (Centro ou Posto de saúde ou Unidade de Saúde da Família/PSF), NESTES ÚLTIMOS 12 MESES?')
    questao120 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='120. Qual foi o PRINCIPAL MOTIVO da sua procura na Unidade Básica de Saúde (Centro ou Posto de saúde ou Unidade de Saúde da Família/PSF) NESTA ÚLTIMA VEZ?')
    questao121 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='121. Você conhece/ouviu falar sobre a campanha de vacinação contra o vírus HPV?')
    questao122 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='122. Você foi vacinada contra o vírus HPV?')
    
    # Imagem corporal
    questao123 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='123. Você considera sua imagem corporal como sendo algo:')
    questao124 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='124. Como você se sente em relação ao seu corpo?')
    questao125 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='125. Quanto ao seu corpo, você se considera:')
    questao126 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='126. O que você está fazendo em relação a seu peso?')
    questao127 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='127. NOS ÚLTIMOS 30 DIAS, você vomitou ou tomou laxantes para perder peso ou evitar ganhar peso?')
    questao128 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='128. NOS ÚLTIMOS 30 DIAS, você tomou algum remédio, fórmula ou outro produto para perder peso, sem acompanhamento médico?')
    questao129 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='129. NOS ÚLTIMOS 30 DIAS, você tomou algum remédio, fórmula ou outro produto para ganhar peso ou massa muscular sem acompanhamento médico?')
    
    # A sua opinião
    questao130 = models.ArrayField(models.IntegerField(choices=QUESTOES), null=True, verbose_name='130. O que você achou deste questionário?')

    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.nome


class Exame(models.Model):
    """Modelo que representa um exame completo"""
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE)
    data = models.DateField(blank=True, null=True, verbose_name='Data')
    examinador = models.CharField(max_length=TAMANHO_NOMES, blank=True, null=True, verbose_name='Examinador')
    anotador = models.CharField(max_length=TAMANHO_NOMES, blank=True, null=True, verbose_name='Anotador')
    
    def __str__(self):
        """Devolve a representação do modelo em string"""
        return str(self.id)


class Odontograma(models.Model):
    """Modelo que representa um odontograma"""
    odontograma = models.ForeignKey('Odontograma', on_delete=models.CASCADE)
    
    def __str__(self):
        """Devolve a representação do modelo em string"""
        return str(self.id)


class Dente(models.Model):
    """Modelo que representa um dente"""
    odontograma = models.ForeignKey('Odontograma', on_delete=models.CASCADE)
    nome = models.CharField(max_length=2, blank=True, null=True, verbose_name='Nome')
    carie = models.SmallIntegerField(blank=True, null=True, verbose_name='Código para cárie')
    fluorose = models.SmallIntegerField(blank=True, null=True, verbose_name='Código para fluorose')
    traumatismo = models.SmallIntegerField(blank=True, null=True, verbose_name='Código para traumatismo')

    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.nome


class Periodontal(models.Model):
    """Modelo que representa um odontograma"""
    
    def __str__(self):
        """Devolve a representação do modelo em string"""
        return str(self.id)
