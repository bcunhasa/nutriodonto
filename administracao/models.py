from django.db import models


class Aluno(models.Model):
    """Modelo que representa um aluno"""
    nome = models.CharField(max_length=TAMANHO_NOMES, verbose_name='Nome')
    sexo = models.IntegerField(choices=SEXO, verbose_name='Sexo')
    nascimento = models.DateField(verbose_name="Data de nascimento")
    escola = models.IntegerField(choices=ESCOLA, verbose_name='Escola')
    periodo = models.IntegerField(choices=PERIODO, verbose_name='Período')
    turma = models.IntegerField(choices=TURMA, verbose_name='Turma')
    municipio = models.IntegerField(choices=MUNICIPIO, verbose_name='Município')

    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.nome


class Questionario(models.Model):
    """Modelo que representa um questionário"""
    
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
    questao57 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='57. Qual é a sua cor ou raça?')
    questao58 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='58. Qual é a sua cor ou raça?')
    questao59 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='59. Qual é a sua cor ou raça?')
    questao60 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='60. Qual é a sua cor ou raça?')
    questao61 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='61. Qual é a sua cor ou raça?')
    questao62 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='62. Qual é a sua cor ou raça?')
    questao63 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='63. Qual é a sua cor ou raça?')
    questao64 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='64. Qual é a sua cor ou raça?')
    questao65 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='65. Qual é a sua cor ou raça?')
    
    # Bebidas alcoólicas
    questao66 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='66. Qual é a sua cor ou raça?')
    questao67 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='67. Qual é a sua cor ou raça?')
    questao68 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='68. Qual é a sua cor ou raça?')
    questao69 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='69. Qual é a sua cor ou raça?')
    questao70 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='70. Qual é a sua cor ou raça?')
    questao71 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='71. Qual é a sua cor ou raça?')
    questao72 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='72. Qual é a sua cor ou raça?')
    questao73 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='73. Qual é a sua cor ou raça?')
    
    # Drogas ilícitas
    questao74 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='74. Qual é a sua cor ou raça?')
    questao75 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='75. Qual é a sua cor ou raça?')
    questao76 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='76. Qual é a sua cor ou raça?')
    questao77 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='77. Qual é a sua cor ou raça?')
    questao78 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='78. Qual é a sua cor ou raça?')
    questao79 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='79. Qual é a sua cor ou raça?')
    
    # Situações em casa e na escola
    questao80 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='80. Qual é a sua cor ou raça?')
    questao81 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='81. Qual é a sua cor ou raça?')
    questao82 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='82. Qual é a sua cor ou raça?')
    questao83 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='83. Qual é a sua cor ou raça?')
    questao84 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='84. Qual é a sua cor ou raça?')
    questao85 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='85. Qual é a sua cor ou raça?')
    questao86 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='86. Qual é a sua cor ou raça?')
    questao87 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='87. Qual é a sua cor ou raça?')
    questao88 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='88. Qual é a sua cor ou raça?')
    questao89 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='89. Qual é a sua cor ou raça?')
    questao90 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='90. Qual é a sua cor ou raça?')
    questao91 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='91. Qual é a sua cor ou raça?')
    
    # Higiene e saúde bucal
    questao92 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='92. Qual é a sua cor ou raça?')
    questao93 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='93. Qual é a sua cor ou raça?')
    questao94 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='94. Qual é a sua cor ou raça?')
    questao95 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='95. Qual é a sua cor ou raça?')
    questao96 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='96. Qual é a sua cor ou raça?')
    questao97 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='97. Qual é a sua cor ou raça?')
    
    # Segurança
    questao98 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='98. Qual é a sua cor ou raça?')
    questao99 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='99. Qual é a sua cor ou raça?')
    questao100 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='100. Qual é a sua cor ou raça?')
    questao101 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='101. Qual é a sua cor ou raça?')
    questao102 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='102. Qual é a sua cor ou raça?')
    questao103 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='103. Qual é a sua cor ou raça?')
    questao104 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='104. Qual é a sua cor ou raça?')
    questao105 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='105. Qual é a sua cor ou raça?')
    questao106 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='106. Qual é a sua cor ou raça?')
    questao107 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='107. Qual é a sua cor ou raça?')
    questao108 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='108. Qual é a sua cor ou raça?')
    questao109 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='109. Qual é a sua cor ou raça?')
    questao110 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='110. Qual é a sua cor ou raça?')
    questao111 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='111. Qual é a sua cor ou raça?')
    questao112 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='112. Qual é a sua cor ou raça?')
    questao113 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='113. Qual é a sua cor ou raça?')
    questao114 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='114. Qual é a sua cor ou raça?')
    questao115 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='115. Qual é a sua cor ou raça?')
    
    # Uso de serviço de saúde
    questao116 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='116. Qual é a sua cor ou raça?')
    questao117 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='117. Qual é a sua cor ou raça?')
    questao118 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='118. Qual é a sua cor ou raça?')
    questao119 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='119. Qual é a sua cor ou raça?')
    questao120 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='120. Qual é a sua cor ou raça?')
    questao121 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='121. Qual é a sua cor ou raça?')
    questao122 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='122. Qual é a sua cor ou raça?')
    questao123 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='123. Qual é a sua cor ou raça?')
    
    # Imagem corporal
    questao124 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='124. Qual é a sua cor ou raça?')
    questao125 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='125. Qual é a sua cor ou raça?')
    questao126 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='126. Qual é a sua cor ou raça?')
    questao127 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='127. Qual é a sua cor ou raça?')
    questao128 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='128. Qual é a sua cor ou raça?')
    questao129 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='129. Qual é a sua cor ou raça?')
    questao130 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='130. Qual é a sua cor ou raça?')
    questao131 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='131. Qual é a sua cor ou raça?')
    
    # A sua opinião
    questao132 = models.IntegerField(choices=QUESTOES, null=True, verbose_name='132. Qual é a sua cor ou raça?')

    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.nome


class Exame(models.Model):
    """Modelo que representa um exame completo"""
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
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """Devolve a representação do modelo em string"""
        return str(self.id)
