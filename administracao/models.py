from django.db import models
from django.contrib.postgres.fields import ArrayField

from .const import *


class Campanha(models.Model):
    """Modelo que representa uma campanha de pesquisa"""
    nome = models.CharField(max_length=TAMANHO_NOMES, verbose_name='Nome')

    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.nome


class Acao(models.Model):
    """Modelo que representa uma acao de uma campanha"""
    campanha = models.ForeignKey('Campanha', related_name='acoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=TAMANHO_NOMES, verbose_name='Nome')

    class Meta:
        verbose_name = 'Ação'
        verbose_name_plural = 'Ações'

    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.nome


class Escola(models.Model):
    """Modelo que representa uma escola de uma acao"""
    acao = models.ForeignKey('Acao', related_name='escolas', on_delete=models.CASCADE)
    nome = models.CharField(choices=ESCOLA, max_length=TAMANHO_NOMES, verbose_name='Nome')
    latitude = models.DecimalField(max_digits=22, decimal_places=18, default=0, verbose_name='Latitude')
    longitude = models.DecimalField(max_digits=22, decimal_places=18, default=0, verbose_name='Longitude')

    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.nome


class Aluno(models.Model):
    """Modelo que representa um aluno"""
    escola = models.ForeignKey('Escola', related_name='alunos', on_delete=models.CASCADE)

    nome = models.CharField(max_length=TAMANHO_NOMES, verbose_name='Nome')
    sexo = models.CharField(choices=SEXO, max_length=TAMANHO_OPCOES, verbose_name='Sexo')
    nascimento = models.DateField(verbose_name="Data de nascimento")
    periodo = models.CharField(choices=PERIODO, max_length=TAMANHO_OPCOES, verbose_name='Período')
    turma = models.CharField(choices=TURMA, max_length=TAMANHO_OPCOES, verbose_name='Turma')
    municipio = models.CharField(choices=MUNICIPIO, max_length=TAMANHO_OPCOES, verbose_name='Município')

    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.nome


class Questionario(models.Model):
    """Modelo que representa um questionário"""
    aluno = models.OneToOneField('Aluno', on_delete=models.CASCADE)
    
    # Informações pessoais
    questao1 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='1. Qual é a sua cor ou raça?')
    questao2 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='2. Qual é a sua idade?')
    questao3 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='3. Qual é o mês do seu aniversário?')
    questao4 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='4. Em que ano você nasceu?')
    
    # Informações gerais
    questao5 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='5. Qual é o seu gênero?')
    questao6 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='6. Em que ano/série você está?')
    questao7 = ArrayField(models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES), null=True, verbose_name='7. Em que turno você estuda? (pode ser múltipla escola).')
    questao8 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='8. Você estuda em regime integral (tem atividades escolares por 7 horas ou mais diárias, durante todo o período escolar)?')
    questao9 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='9. Você estuda em regime de internato (a escola possui alojamento onde os alunos permanecem e dormem diariamente, durante todo o período escolar)?')
    questao10 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='10. Qual o grau de escolaridade mais elevado que você pretende concluir?')
    questao11 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='11. Quando terminar o ciclo/curso que você está frequentando atualmente, você pretende?')
    questao12 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='12. Você mora com sua mãe?')
    questao13 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='13. Você mora com seu pai?')
    questao14 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='14. Contando com você, quantas pessoas moram na sua casa ou apartamento?')
    questao15 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='15. Na sua casa tem telefone fixo (convencional)?')
    questao16 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='16. Você tem celular?')
    questao17 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='17. Na sua casa tem computador (de mesa, netbook, laptop etc.)?')
    questao18 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='18. Você tem acesso à internet em sua casa?')
    questao19 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='19. Alguém que mora na sua casa tem carro?')
    questao20 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='20. Alguém que mora na sua casa tem moto?')
    questao21 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='21. Quantos banheiros com chuveiro têm dentro da sua casa?')
    questao22 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='22. Tem empregado(a) doméstico(a) recebendo dinheiro para fazer o trabalho em sua casa, três ou mais dias por semana?')
    questao23 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='23. Qual nível de ensino (grau) sua mãe estudou ou estuda?')
    questao24 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='24. Você tem algum trabalho, emprego ou negócio atualmente?')
    questao25 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='25. Você recebe dinheiro por este trabalho, emprego ou negócio?')
    questao26 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='26. Sua família recebe benefícios do Programa Bolsa Família?')
    
    # Alimentação
    questao27 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='27. Você costuma tomar o café da manhã?')
    questao28 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='28. Você costuma almoçar ou jantar com sua mãe, pai ou responsável?')
    questao29 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='29. Você costuma comer quando está assistindo à TV ou estudando?')
    questao30 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='30. Sua escola oferece comida (merenda escolar/almoço) aos alunos da sua turma? (Não considerar lanches/comida comprados na cantina)')
    questao31 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='31. Você costuma comer a comida (merenda/almoço) oferecida pela escola? (Não considerar lanches/comida comprados na cantina)')
    questao32 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='32. NOS ÚLTIMOS 7 DIAS, em quantos dias você comeu feijão?')
    questao33 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='33. NOS ÚLTIMOS 7 DIAS, em quantos dias você comeu salgados fritos? Exemplo: batata frita (sem contar a batata de pacote) ou salgados fritos como coxinha de galinha, quibe frito, pastel frito, comidas típicas, etc.')
    questao34 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='34. NOS ÚLTIMOS 7 DIAS, em quantos dias você comeu pelo menos um tipo de legume ou verdura? Exemplos: alface, abóbora, brócolis, cebola, cenoura, chuchu, couve, espinafre, pepino, tomate etc. Não inclua batata e aipim (mandioca/macaxeira).')
    questao35 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='35. NOS ÚLTIMOS 7 DIAS, em quantos dias você comeu guloseimas (doces, balas, chocolates, chicletes, bombons ou pirulitos)?')
    questao36 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='36. NOS ÚLTIMOS 7 DIAS, em quantos dias você comeu frutas frescas ou salada de frutas?')
    questao37 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='37. NOS ÚLTIMOS SETE DIAS, em quantos dias você tomou refrigerante?')
    questao38 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='38. NOS ÚLTIMOS SETE DIAS, em quantos dias você comeu alimentos industrializados/ultraprocessados salgados, como hambúrguer, presunto, mortadela, salame, linguiça, salsicha, macarrão instantâneo, salgadinho de pacote, biscoitos salgados?')
    questao39 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='39. NOS ÚLTIMOS SETE DIAS, em quantos dias você comeu em restaurantes fast food, tais como lanchonetes, barracas de cachorro quentes, pizzaria etc.?')
    questao40 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='40. NOS ÚLTIMOS 30 DIAS, com que frequência você ficou com fome por não ter comida suficiente em sua casa?')
    questao41 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='41. NOS ÚLTIMOS 30 DIAS, quantas vezes por dia você normalmente comeu frutas frescas ou salada de frutas?')
    questao42 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='42. NOS ÚLTIMOS 30 DIAS, quantas vezes por dia você normalmente comeu legumes ou verduras, tais como alface, abóbora, brócolis, cebola, cenoura, chuchu, couve, espinafre, pepino, tomate etc.? Não inclua batata e aipim (mandioca/macaxeira)')
    questao43 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='43. NOS ÚLTIMOS 30 DIAS, quantas vezes por dia você tomou refrigerante?')
    
    # Atividade física
    questao44 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='44. NOS ÚLTIMOS 7 DIAS, em quantos dias você FOI a pé ou de bicicleta para a escola?')
    questao45 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='45. Quando você VAI para a escola a pé ou de bicicleta, quanto tempo você gasta?')
    questao46 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='46. NOS ÚLTIMOS 7 DIAS, em quantos dias você VOLTOU a pé ou de bicicleta da escola?')
    questao47 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='47. Quando você VOLTA da escola a pé ou de bicicleta, quanto tempo você gasta?')
    questao48 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='48. NOS ÚLTIMOS 7 DIAS, quantos dias você teve aulas de educação física na escola?')
    questao49 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='49. NOS ÚLTIMOS 7 DIAS, quanto tempo por dia você fez atividade física ou esporte durante as aulas de educação física na escola?')
    questao50 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='50. NOS ÚLTIMOS 7 DIAS, sem contar as aulas de educação física da escola, em quantos dias você praticou alguma atividade física, como esportes, dança, ginástica, musculação, lutas ou outra atividade?')
    questao51 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='51. NORMALMENTE, quanto tempo por dia duram essas atividades (como esportes, dança, ginástica, musculação, lutas ou outra atividade) que você faz? (Sem contar as aulasde educação física)')
    questao52 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='52. NOS ÚLTIMOS 7 DIAS, em quantos dias você fez atividade física por pelo menos 60 minutos (1 hora) por dia? (Some todo o tempo que você gastou em qualquer tipo de atividade física, EM CADA DIA)')
    questao53 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='53. Se você tivesse oportunidade de fazer atividade física na maioria dos dias da semana, qual seria a sua atitude?')
    questao54 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='54. Em um dia de semana comum, quantas horas por dia você assiste a TV? (não contar sábado, domingo e feriado)')
    questao55 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='55. Em um dia de semana comum, quanto tempo você fica sentado(a), assistindo televisão, usando computador, jogando videogame, conversando com amigos(as) ou fazendo outras atividades sentado(a)? (não contar sábado, domingo, feriados e o tempo sentado na escola)')
    
    # Uso de cigarro
    questao56 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='56. Alguma vez na vida, você já fumou cigarro, mesmo uma ou duas tragadas?')
    questao57 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='57. Que idade você tinha quando experimentou fumar cigarro pela primeira vez?')
    questao58 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='58. NOS ÚLTIMOS 30 DIAS, em quantos dias você fumou cigarros?')
    questao59 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='59. NOS ÚLTIMOS 30 DIAS, em geral, como você conseguiu seus próprios cigarros?')
    questao60 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='60. NOS ÚLTIMOS 30 DIAS, alguém se recusou a lhe vender cigarros por causa de sua idade?')
    questao61 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='61. NOS ÚLTIMOS 30 DIAS, em quantos dias você usou outros produtos de tabaco: cigarros de palha ou enrolados a mão, charuto, cachimbo, cigarrilha, cigarro indiano ou bali, narguilé, rapé, fumo de mascar etc.? (não incluir cigarro comum)')
    questao62 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='62. Qual outro produto do tabaco você usou com mais frequência NOS ÚLTIMOS 30 DIAS?')
    questao63 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='63. NOS ÚLTIMOS 7 DIAS, em quantos dias pessoas fumaram na sua presença?')
    questao64 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='64. Algum de seus pais ou responsáveis fuma?')
    questao65 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='65. Primeira dose de bebida alcoólica (uma dose equivale a uma lata de cerveja ou uma taça de vinho ou uma dose de cachaça ou uísque etc.)?')
    
    # Bebidas alcoólicas
    questao66 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='66. Alguma vez na vida você tomou uma dose de bebida alcoólica (uma dose equivale a uma lata de cerveja ou uma taça de vinho ou uma dose de cachaça ou uísque etc.)?')
    questao67 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='67. Que idade você tinha quando tomou a primeira dose de bebida alcoólica (uma dose equivale a uma lata de cerveja ou uma taça de vinho ou uma dose de cachaça ou uísque etc.)?')
    questao68 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='68. NOS ÚLTIMOS 30 DIAS, em quantos dias você tomou pelo menos um copo ou uma dose de bebida alcoólica (uma dose equivale a uma lata de cerveja ou uma taça de vinho ou uma dose de cachaça ou uísque etc.)?')
    questao69 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='69. NOS ÚLTIMOS 30 DIAS, nos dias em que você tomou alguma bebida alcoólica, quantos copos ou doses você tomou por dia?')
    questao70 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='70. NOS ÚLTIMOS 30 DIAS, na maioria das vezes, como você conseguiu a bebida que tomou?')
    questao71 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='71. Na sua vida, quantas vezes você bebeu tanto que ficou realmente bêbado(a)?')
    questao72 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='72. Na sua vida, quantas vezes você teve problemas com sua família ou amigos, perdeu aulas ou brigou por que tinha bebido?')
    questao73 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='73. Quantos amigos seus consomem bebida alcoólica?')
    
    # Drogas ilícitas
    questao74 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='74. Alguma vez na vida, você já usou alguma droga como: maconha, cocaína, crack, cola, loló, lança-perfume, ecstasy, oxy etc.?')
    questao75 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='75. Que idade você tinha quando usou alguma droga como: maconha, cocaína, crack, cola, loló, lança-perfume, ecstasy, oxy ou outra pela primeira vez?')
    questao76 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='76. NOS ÚLTIMOS 30 DIAS, quantos dias você usou droga como maconha, cocaína, crack, cola, loló, lança-perfume, ecstasy, oxy etc.?')
    questao77 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='77. NOS ÚLTIMOS 30 DIAS, quantos dias você usou maconha?')
    questao78 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='78. NOS ÚLTIMOS 30 DIAS, quantos dias você usou crack?')
    questao79 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='79. Quantos amigos seus usam drogas?')
    
    # Situações em casa e na escola
    questao80 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='80. NOS ÚLTIMOS 30 DIAS, em quantos dias você faltou às aulas ou à escola sem permissão dos seus pais ou responsáveis?')
    questao81 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='81. NOS ÚLTIMOS 30 DIAS, com que frequência seus pais ou responsáveis sabiam realmente o que você estava fazendo em seu tempo livre?')
    questao82 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='82. NOS ÚLTIMOS 30 DIAS, com que frequência seus pais ou responsáveis verificaram se os seus deveres de casa (lição de casa) foram feitos?')
    questao83 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='83. NOS ÚLTIMOS 30 DIAS, com que frequência seus pais ou responsáveis entenderam seus problemas e preocupações?')
    questao84 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='84. NOS ÚLTIMOS 30 DIAS, com que frequência seus pais ou responsáveis mexeram em suas coisas sem a sua concordância?')
    questao85 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='85. NOS ÚLTIMOS 30 DIAS, com que frequência os colegas de sua escola trataram você bem e/ou foram prestativos contigo?')
    questao86 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='86. NOS ÚLTIMOS 30 DIAS, com que frequência algum dos seus colegas de escola te esculacharam, zoaram, mangaram, intimidaram ou caçoaram tanto que você ficou magoado, incomodado, aborrecido, ofendido ou humilhado?')
    questao87 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='87. NOS ÚLTIMOS 30 DIAS, qual o motivo/causa de seus colegas terem te esculachado, zombado, zoado, caçoado, mangado, intimidado ou humilhado?')
    questao88 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='88. NOS ÚLTIMOS 30 DIAS, você esculachou, zombou, mangou, intimidou ou caçoou algum de seus colegas da escola tanto que ele ficou magoado, aborrecido, ofendido ou humilhado?')
    questao89 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='89. Você já sofreu bullying?')
    questao90 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='90. NOS ÚLTIMOS 12 MESES, com que frequência você não conseguiu dormir à noite porque algo o(a) preocupava muito?')
    questao91 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='91. Quantos amigos(as) próximos você tem?')
    
    # Higiene e saúde bucal
    questao92 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='92. NOS ÚLTIMOS 30 DIAS, com que frequência você lavou as mãos antes de comer?')
    questao93 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='93. NOS ÚLTIMOS 30 DIAS, com que frequência você lavou as mãos após usar o banheiro ou o vaso sanitário?')
    questao94 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='94. NOS ÚLTIMOS 30 DIAS, com que frequência você usou sabão ou sabonete quando lavou suas mãos?')
    questao95 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='95. NOS ÚLTIMOS 30 DIAS, quantas vezes por dia você usualmente escovou os dentes?')
    questao96 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='96. NOS ÚLTIMOS 06 MESES, você teve dor de dente? (excluir dor de dente causada por uso de aparelho)')
    questao97 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='97. NOS ÚLTIMOS 12 MESES, quantas vezes você foi ao dentista?')
    
    # Segurança
    questao98 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='98. NOS ÚLTIMOS 30 DIAS, em quantos dias você deixou de ir à escola porque não se sentia seguro no caminho de casa para a escola ou da escola para casa?')
    questao99 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='99. NOS ÚLTIMOS 30 DIAS, em quantos dias você não foi à escola porque não se sentia seguro na escola?')
    questao100 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='100. NOS ÚLTIMOS 30 DIAS, com que frequência você usou cinto de segurança enquanto andava como passageiro(a) NO BANCO DA FRENTE de carro/automóvel, van ou táxi?')
    questao101 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='101. NOS ÚLTIMOS 30 DIAS, com que frequência você usou capacete ao andar de motocicleta?')
    questao102 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='102. NOS ÚLTIMOS 30 DIAS, quantas vezes você dirigiu um veículo motorizado de transporte (carro, motocicleta, voadeira, barco)?')
    questao103 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='103. NOS ÚLTIMOS 30 DIAS, quantas vezes você andou em carro ou outro veículo motorizado dirigido por alguém que tinha consumido alguma bebida alcoólica?')
    questao104 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='104. NOS ÚLTIMOS 30 DIAS, quantas vezes você foi agredido(a) fisicamente por um adulto da sua família?')
    questao105 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='105. NOS ÚLTIMOS 30 DIAS, você esteve envolvido(a) em alguma briga em que alguma pessoa usou arma de fogo, como revólver ou espingarda?')
    questao106 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='106. NOS ÚLTIMOS 30 DIAS, você esteve envolvido(a) em alguma briga em que alguma pessoa usou alguma outra arma como faca, canivete, peixeira, pedra, pedaço de pau ou garrafa?')
    questao107 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='107. NOS ÚLTIMOS 12 MESES, quantas vezes você foi agredido(a) fisicamente?')
    questao108 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='108. NOS ÚLTIMOS 12 MESES, quantas vezes você se envolveu em briga (uma luta física)?')
    questao109 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='109. NOS ÚLTIMOS 12 MESES, quantas vezes você foi seriamente ferido(a)?')
    questao110 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='110. NOS ÚLTIMOS 12 MESES, qual foi o ferimento ou a lesão MAIS SÉRIA que aconteceu com você?')
    questao111 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='111. NOS ÚLTIMOS 12 MESES, qual foi a PRINCIPAL CAUSA do ferimento ou da lesão mais séria que aconteceu com você?')
    questao112 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='112. NOS ÚLTIMOS 12 MESES, você sofreu algum acidente de bicicleta (caiu e se machucou)?')
    questao113 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='113. Alguma vez na vida você foi forçado(a) a ter relação sexual?')
    questao114 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='114. Quem forçou você a ter relação sexual?')
    
    # Uso de serviço de saúde
    questao115 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='115. Como você classificaria seu estado de saúde?')
    questao116 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='116. NOS ÚLTIMOS 12 MESES, quantos dias você faltou a escola por motivo(s) relacionado(s) à sua saúde?')
    questao117 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='117. NOS ÚLTIMOS 12 MESES você procurou algum serviço ou profissional de saúde para atendimento relacionado à própria saúde?')
    questao118 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='118. NOS ÚLTIMOS 12 MESES, qual foi o serviço de saúde que você procurou com MAIS FREQUÊNCIA?')
    questao119 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='119. Você foi atendido(a) NA ÚLTIMA VEZ que procurou alguma Unidade Básica de Saúde (Centro ou Posto de saúde ou Unidade de Saúde da Família/PSF), NESTES ÚLTIMOS 12 MESES?')
    questao120 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='120. Qual foi o PRINCIPAL MOTIVO da sua procura na Unidade Básica de Saúde (Centro ou Posto de saúde ou Unidade de Saúde da Família/PSF) NESTA ÚLTIMA VEZ?')
    questao121 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='121. Você conhece/ouviu falar sobre a campanha de vacinação contra o vírus HPV?')
    questao122 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='122. Você foi vacinada contra o vírus HPV?')
    
    # Imagem corporal
    questao123 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='123. Você considera sua imagem corporal como sendo algo:')
    questao124 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='124. Como você se sente em relação ao seu corpo?')
    questao125 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='125. Quanto ao seu corpo, você se considera:')
    questao126 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='126. O que você está fazendo em relação a seu peso?')
    questao127 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='127. NOS ÚLTIMOS 30 DIAS, você vomitou ou tomou laxantes para perder peso ou evitar ganhar peso?')
    questao128 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='128. NOS ÚLTIMOS 30 DIAS, você tomou algum remédio, fórmula ou outro produto para perder peso, sem acompanhamento médico?')
    questao129 = models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES, null=True, verbose_name='129. NOS ÚLTIMOS 30 DIAS, você tomou algum remédio, fórmula ou outro produto para ganhar peso ou massa muscular sem acompanhamento médico?')
    
    # A sua opinião
    questao130 = ArrayField(models.CharField(choices=QUESTAO1, max_length=TAMANHO_OPCOES), null=True, verbose_name='130. O que você achou deste questionário?')

    class Meta:
        verbose_name = 'Questionário'
        verbose_name_plural = 'Questionários'

    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.nome


class Exame(models.Model):
    """Modelo que representa um exame completo"""
    aluno = models.OneToOneField('Aluno', on_delete=models.CASCADE)
    data = models.DateField(null=True, verbose_name='Data')
    examinador = models.CharField(max_length=TAMANHO_NOMES, null=True, verbose_name='Examinador')
    anotador = models.CharField(max_length=TAMANHO_NOMES, null=True, verbose_name='Anotador')
    
    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.aluno.nome


class Edentulismo(models.Model):
    """Modelo que representa a seção de edentulismo do exame"""
    exame = models.OneToOneField('Exame', on_delete=models.CASCADE)
    
    uso_superior = models.CharField(choices=USO_PROTESE, max_length=TAMANHO_OPCOES, null=True, verbose_name='Uso de prótese - superior')
    uso_inferior = models.CharField(choices=USO_PROTESE, max_length=TAMANHO_OPCOES, null=True, verbose_name='Uso de prótese - inferior')
    necessidade_superior = models.CharField(choices=NECESSIDADE_PROTESE, max_length=TAMANHO_OPCOES, null=True, verbose_name='Necessidade de prótese - superior')
    necessidade_inferior = models.CharField(choices=NECESSIDADE_PROTESE, max_length=TAMANHO_OPCOES, null=True, verbose_name='Necessidade de prótese - inferior')
    
    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.exame.aluno.nome


class Fluorose(models.Model):
    """Modelo que representa a seção de fluorose do exame"""
    exame = models.OneToOneField('Exame', on_delete=models.CASCADE)
    
    valor = models.CharField(choices=FLUOROSE, max_length=TAMANHO_OPCOES, null=True, verbose_name='Fluorose')
    
    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.exame.aluno.nome


class Traumatismo(models.Model):
    """Modelo que representa a seção de traumatismo do exame"""
    exame = models.OneToOneField('Exame', on_delete=models.CASCADE)
    
    dente12 = models.CharField(choices=TRAUMATISMO, max_length=TAMANHO_OPCOES, null=True, verbose_name='Dente 12')
    dente11 = models.CharField(choices=TRAUMATISMO, max_length=TAMANHO_OPCOES, null=True, verbose_name='Dente 11')
    dente21 = models.CharField(choices=TRAUMATISMO, max_length=TAMANHO_OPCOES, null=True, verbose_name='Dente 21')
    dente22 = models.CharField(choices=TRAUMATISMO, max_length=TAMANHO_OPCOES, null=True, verbose_name='Dente 22')
    dente42 = models.CharField(choices=TRAUMATISMO, max_length=TAMANHO_OPCOES, null=True, verbose_name='Dente 42')
    dente41 = models.CharField(choices=TRAUMATISMO, max_length=TAMANHO_OPCOES, null=True, verbose_name='Dente 41')
    dente31 = models.CharField(choices=TRAUMATISMO, max_length=TAMANHO_OPCOES, null=True, verbose_name='Dente 31')
    dente32 = models.CharField(choices=TRAUMATISMO, max_length=TAMANHO_OPCOES, null=True, verbose_name='Dente 32')
    
    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.exame.aluno.nome


class Carie(models.Model):
    """Modelo que representa a seção de cárie do exame"""
    exame = models.OneToOneField('Exame', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Cárie'
        verbose_name_plural = 'Cáries'
    
    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.exame.aluno.nome


class Dente(models.Model):
    """Modelo que representa um dente do da seção de cárie do exame"""
    carie = models.ForeignKey('Carie', related_name='dentes', on_delete=models.CASCADE)
    
    codigo = models.CharField(null=True, max_length=TAMANHO_CODIGOS, verbose_name='Código')
    coroa = models.CharField(choices=CARIE_COROA, max_length=TAMANHO_OPCOES, null=True, verbose_name='Coroa')
    raiz = models.CharField(choices=CARIE_RAIZ, max_length=TAMANHO_OPCOES, null=True, verbose_name='Raiz')
    tratamento = models.CharField(choices=CARIE_TRATAMENTO, max_length=TAMANHO_OPCOES, null=True, verbose_name='Tratamento')
    
    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.codigo


class Periodontal(models.Model):
    """Modelo que representa a seção de periodontia do exame"""
    exame = models.OneToOneField('Exame', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Periodontais'
    
    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.exame.aluno.nome


class Gengiva(models.Model):
    """Modelo que representa um dente do índice periodontal comunitário"""
    periodontal = models.ForeignKey('Periodontal', related_name='gengivas', on_delete=models.CASCADE)
    
    codigo = models.CharField(null=True, max_length=TAMANHO_CODIGOS, verbose_name='Código')
    
    sangramento = models.CharField(choices=CPI_SANGRAMENTO, max_length=TAMANHO_OPCOES, null=True, verbose_name='Sangramento')
    calculo = models.CharField(choices=CPI_CALCULO, max_length=TAMANHO_OPCOES, null=True, verbose_name='Cálculo dentário')
    bolsa = models.CharField(choices=CPI_BOLSA, max_length=TAMANHO_OPCOES, null=True, verbose_name='Bolsa periodontal')
    
    pip = models.CharField(choices=PIP, max_length=TAMANHO_OPCOES, null=True, verbose_name='Índice de Perda de Inserção Periodontal')
    
    class Meta:
        verbose_name = 'CPI'
        verbose_name_plural = 'CPI'
    
    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.codigo
