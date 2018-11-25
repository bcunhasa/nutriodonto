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
    numero_identificacao = models.CharField(max_length=TAMANHO_NOMES, verbose_name='Número de identificação')
    escola = models.ForeignKey('Escola', related_name='alunos', on_delete=models.CASCADE)

    periodo = models.CharField(choices=PERIODO, blank=True, null=True, max_length=TAMANHO_OPCOES, verbose_name='Período')
    turma = models.CharField(max_length=TAMANHO_NOMES, blank=True, null=True, verbose_name='Turma')
    nascimento = models.DateField(null=True,verbose_name="Data de nascimento")
    sexo = models.CharField(choices=SEXO, blank=True, null=True, max_length=TAMANHO_OPCOES, verbose_name='Sexo')
    raca = models.CharField(choices=RACA, blank=True, null=True, max_length=TAMANHO_OPCOES, verbose_name='Raça')   

    def __str__(self):
        """Devolve a representação do modelo em string"""
        return str(self.numero_identificacao)


class Questionario(models.Model):
    """Modelo que representa um questionário"""
    aluno = models.OneToOneField('Aluno', on_delete=models.CASCADE)
    data = models.DateField(null=True, verbose_name='Data')
    
    # Informações pessoais
    questao_1 = models.CharField(choices=ALUNO_1, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='01. Qual o grau de escolaridade mais elevado que você pretende concluir?')
    questao_2 = models.CharField(choices=ALUNO_2, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='02. Quando terminar o ciclo/curso que você está frequentando atualmente, você pretende?')
    questao_3 = models.CharField(choices=ALUNO_3, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='03. Você mora com sua mãe?')
    questao_4 = models.CharField(choices=ALUNO_4, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='04. Você mora com seu pai?')
    questao_5 = models.CharField(choices=ALUNO_5, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='05. Contando com você, quantas pessoas moram na sua casa ou apartamento?')
    questao_6 = models.CharField(choices=ALUNO_6, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='06. Na sua casa tem telefone fixo (convencional)?')
    questao_7 = models.CharField(choices=ALUNO_7, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='07. Você tem celular?')
    questao_8 = models.CharField(choices=ALUNO_8, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='08. Na sua casa tem computador (de mesa, notbook, laptop etc.)?')
    questao_9 = models.CharField(choices=ALUNO_9, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='09. Você tem acesso à internet em sua casa?')
    questao_10 = models.CharField(choices=ALUNO_10, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='10. Alguém que mora na sua casa tem carro?')
    questao_11 = models.CharField(choices=ALUNO_11, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='11. Alguém que mora na sua casa tem moto?')
    questao_12 = models.CharField(choices=ALUNO_12, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='12. Quantos banheiros com chuveiro têm dentro da sua casa?')
    questao_13 = models.CharField(choices=ALUNO_13, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='13. Na sua casa tem empregado (a) doméstico (a)?')
    questao_14 = models.CharField(choices=ALUNO_14, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='14. Caso responda SIM, quantos dias esta pessoa trabalha?')
    questao_15 = models.CharField(choices=ALUNO_15, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='15. Qual nível de ensino (grau) sua mãe estudou ou estuda?')
    questao_16 = models.CharField(choices=ALUNO_16, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='16. Você tem algum trabalho, emprego ou negócio atualmente?')
    questao_17 = models.CharField(choices=ALUNO_17, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='17. Você recebe dinheiro por este trabalho, emprego ou negócio?')
    questao_18 = models.CharField(choices=ALUNO_18, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='18. Sua família recebe benefícios do Programa Bolsa Família? Comportamento Alimentar')
    questao_19 = models.CharField(choices=ALUNO_19, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='19. Você costuma tomar o café da manhã?')
    questao_20 = models.CharField(choices=ALUNO_20, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='20. Você costuma almoçar ou jantar com sua mãe, pai ou responsável?')
    questao_21 = models.CharField(choices=ALUNO_21, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='21. Você costuma comer quando está assistindo à TV ou estudando?')
    questao_22 = models.CharField(choices=ALUNO_22, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='22. Sua escola oferece comida (merenda escolar/almoço) aos alunos da sua turma? (Não considerar lanches/comida comprados na cantina)')
    questao_23 = models.CharField(choices=ALUNO_23, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='23. Você costuma comer a comida (merenda/almoço) oferecida pela escola? (Não considerar lanches/comida comprados na cantina)')
    questao_24 = models.CharField(choices=ALUNO_24, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='24. Nos últimos 30 dias, com que frequência você ficou com fome por não ter comida suficiente em sua casa?')
    questao_25 = models.CharField(choices=ALUNO_25, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='25. Leite de vaca:')
    questao_26 = models.CharField(choices=ALUNO_26, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='26. Leite de vaca com adição de achocolatados em pó (nescau, toddy, ovomaltine), mel ou açúcar:')
    questao_27 = models.CharField(choices=ALUNO_27, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='27. Achocolatados líquidos comprados em supermercados como, por exemplo: Todyynho, Chokinho; Nescau; Italac etc.')
    questao_28 = models.CharField(choices=ALUNO_28, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='28. Iogurte como, por exemplo: Danone, Danoninho, Nestlé, Ninho, etc.')
    questao_29 = models.CharField(choices=ALUNO_29, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='29. Queijo.')
    questao_30 = models.CharField(choices=ALUNO_30, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='30. Sobremesas feitas com leite (pudim, flam, pudim de chocolate, creme de leite).')
    questao_31 = models.CharField(choices=ALUNO_31, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='31. Gelados (Picolé, sorvete, geladinho).')
    questao_32 = models.CharField(choices=ALUNO_32, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='32. Pão ou torrada (torrada é o mesmo que pão, sendo que em torrado).')
    questao_33 = models.CharField(choices=ALUNO_33, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='33. Flocos de cereais açucarados (por exemplo, flocos conhecidos como sucrilhos ou equivalentes, nescau cereal), etc.')
    questao_34 = models.CharField(choices=ALUNO_34, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='34. Flocos de cereais (aveia, milho, centeio, como os da marca Nesfit e Nutry)')
    questao_35 = models.CharField(choices=ALUNO_35, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='35. Arroz, massas, batatas.')
    questao_36 = models.CharField(choices=ALUNO_36, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='36. Batatas fritas pacote Ruffles, Pringles, Lay’s')
    questao_37 = models.CharField(choices=ALUNO_37, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='37. Batatas fritas caseiras.')
    questao_38 = models.CharField(choices=ALUNO_38, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='38. Bolachas Maria, bolachas Mabel, biscoitos ou bolachas cream cracker, (ou água e sal) etc.')
    questao_39 = models.CharField(choices=ALUNO_39, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='39. Outras bolachas (biscoitos recheados como Bono, Trakinas e Oreo).')
    questao_40 = models.CharField(choices=ALUNO_40, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='40. Produtos de pastelaria (coxinhas, pastéis, salgadinhos de queijo, kibes).')
    questao_41 = models.CharField(choices=ALUNO_41, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='41. Snacks (chocolates vendidos em barrinhas, como Twix, Kitkat, Bis e Chokito)')
    questao_42 = models.CharField(choices=ALUNO_42, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='42. Marmelada, doce em potinho, geleia, mel. (Como Paçoquita, Melzinho e Pé de moleque)')
    questao_43 = models.CharField(choices=ALUNO_43, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='43. Açúcares em geral.')
    questao_44 = models.CharField(choices=ALUNO_44, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='44. Sopas comuns caseiras (de carne, frango ou legumes)')
    questao_45 = models.CharField(choices=ALUNO_45, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='45. Vegetais crus em salada ou cozinhados (Cenoura, couve flor, brócolis, alface, beterraba, agrião)')
    questao_46 = models.CharField(choices=ALUNO_46, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='46. Leguminosas (feijão, grão de bico, ervilhas, favas).')
    questao_47 = models.CharField(choices=ALUNO_47, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='47. Fruta fresca. (Manga, caju, banana, goiaba, acerola, murici, maça, laranja)')
    questao_48 = models.CharField(choices=ALUNO_48, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='48. Frutos enlatados em calda: (pêssego, banana, caju, goiaba).')
    questao_49 = models.CharField(choices=ALUNO_49, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='49. Sucos naturais (de laranja, acerola, tangerina, uva)')
    questao_50 = models.CharField(choices=ALUNO_50, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='50. Refrigerantes (Coca cola, graraná ou fanta) ou ainda sucos de caixinha com néctar (como Kapo, del Valle)')
    questao_51 = models.CharField(choices=ALUNO_51, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='51. Pizzas. (Mini Pizza por exemplo)')
    questao_52 = models.CharField(choices=ALUNO_52, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='52. Hamburguer e cachorro quente.')
    questao_53 = models.CharField(choices=ALUNO_53, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='53. Rebuçados, gomas, pastilhas elásticas. (Chicletes, balinhas, jujubas)')
    questao_54 = models.CharField(choices=ALUNO_54, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='54. Rosquinhas (como Donuts, Sonhos, Rosquinhas de Polvilho, Pão de Mel) Hábitos Alimentares quando o (a) estudante tinha menos de dois anos de idade')
    questao_55 = models.CharField(choices=ALUNO_55, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='55. Seu filho (a) foi alimentado (a) com leite materno?')
    questao_56 = models.CharField(choices=ALUNO_56, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='56. Ele (a) mamou (apenas no peito) até quantos meses de idade?')
    questao_57 = models.CharField(choices=ALUNO_57, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='57. Se seu filho ou sua filha mamou até seis meses ou mais, até quantos meses ele (a) mamou no peito (mesmo que tenha se alimentado com outras comidas ou bebidas) Meu (minha) Filho (filha) mamou no peito até:')
    questao_58 = models.CharField(choices=ALUNO_58, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='58. Antes de completar dois anos de idade, seu filho (a) foi alimentado (a) com leite industrial? (aquele leite comprado nas farmácias ou supermercados)')
    questao_59 = models.CharField(choices=ALUNO_59, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='59. Caso sua resposta tenha sido SIM, até quantos meses ele se alimentou de leite industrial, isto é, aquele leite que é comprado nas farmácias e supermercados?')
    questao_60 = ArrayField(models.CharField(choices=ALUNO_60, max_length=TAMANHO_OPCOES), blank=True, null=True, verbose_name='60. Até dois anos de idade, seu filho ou sua filha recebeu alimentação mista, isto é:')
    questao_61 = models.CharField(choices=ALUNO_61, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='61. Até dois anos de idade, seu filho ou sua filha tomou leite de vaca?')
    questao_62 = models.CharField(choices=ALUNO_62, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='62. Caso sua resposta tenha sido sim, com que idade (em meses) ele começou a tomar leite de vaca?')
    questao_63 = models.CharField(choices=ALUNO_63, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='63. Nos últimos dias, em quantos deles você foi a pé ou de bicicleta para a escola?')
    questao_64 = models.CharField(choices=ALUNO_64, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='64. Quando você vai para a escola a pé ou de bicicleta, quanto tempo você gasta?')
    questao_65 = models.CharField(choices=ALUNO_65, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='65. Nos últimos 7 dias, quantos dias você teve aulas de educação física na escola?')
    questao_66 = models.CharField(choices=ALUNO_66, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='66. Nos últimos sete dias, quanto tempo por dia você fez atividade física ou esporte durante as aulas de educação física na escola?')
    questao_67 = models.CharField(choices=ALUNO_67, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='67. Nos últimos 7 dias, sem contar as aulas de educação física da escola, em quantos dias você praticou alguma atividade física, como esportes, dança, ginástica, musculação, lutas ou outra atividade?')
    questao_68 = models.CharField(choices=ALUNO_68, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='68. Normalmente, quanto tempo por dia duram essas atividades (como esportes, dança, ginástica, musculação, lutas ou outra atividade) que você faz? (Sem contar as aulas de educação física)')
    questao_69 = models.CharField(choices=ALUNO_69, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='69. Nos últimos 7 dias, em quantos dias você fez atividade física por pelo menos 60 minutos (1 hora) por dia? (Some todo o tempo que você gastou em qualquer tipo de atividade física, em cada dia)')
    questao_70 = models.CharField(choices=ALUNO_70, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='70. Se você tivesse oportunidade de fazer atividade física na maioria dos dias da semana, qual seria a sua atitude?')
    questao_71 = models.CharField(choices=ALUNO_71, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='71. Em um dia de semana comum, quantas horas por dia você assiste a TV? (não contar sábado, domingo e feriado)')
    questao_72 = models.CharField(choices=ALUNO_72, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='72. Em um dia de semana comum, quanto tempo você fica sentado(a), assistindo televisão, usando computador, jogando videogame, conversando com amigos(as) ou fazendo outras atividades sentado(a)? (não contar sábado, domingo, feriados e o tempo sentado na escola)')
    questao_73 = models.CharField(choices=ALUNO_73, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='73. Alguma vez na vida, você já fumou cigarro, mesmo uma ou duas tragadas?')
    questao_74 = models.CharField(choices=ALUNO_74, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='74. Que idade você tinha quando experimentou fumar cigarro pela primeira vez?')
    questao_75 = models.CharField(choices=ALUNO_75, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='75. Nos últimos 30 dias, em quantos dias você fumou cigarros?')
    questao_76 = models.CharField(choices=ALUNO_76, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='76. Nos últimos 30 dias, em geral, como você conseguiu seus próprios cigarros?')
    questao_77 = models.CharField(choices=ALUNO_77, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='77. Nos ultimos 30 dias, alguém se recusou a lhe vender cigarros por causa de sua idade?')
    questao_78 = models.CharField(choices=ALUNO_78, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='78. Nos últimos 30 dias, em quantos dias você usou outros produtos de tabaco: cigarros de palha ou enrolados a mão, charuto, cachimbo, cigarrilha, cigarro indiano ou bali, narguilé, rapé, fumo de mascar etc.? (não incluir cigarro comum)')
    questao_79 = models.CharField(choices=ALUNO_79, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='79. Qual outro produto do tabaco você usou com mais frequência nos últimos 30 dias?')
    questao_80 = models.CharField(choices=ALUNO_80, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='80. Nos últimos 7 dias, em quantos dias pessoas fumaram na sua presença?')
    questao_81 = models.CharField(choices=ALUNO_81, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='81. Algum de seus pais ou responsáveis fuma?')
    questao_82 = models.CharField(choices=ALUNO_82, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='82. Alguma vez na vida você tomou uma dose de bebida alcoólica (uma dose equivale a uma lata de cerveja ou uma taça de vinho ou uma dose de cachaça ou uísque etc.)?')
    questao_83 = models.CharField(choices=ALUNO_83, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='83. Que idade você tinha quando tomou a primeira dose de bebida alcoólica (uma dose equivale a uma lata de cerveja ou uma taça de vinho ou uma dose de cachaça ou uísque etc.)?')
    questao_84 = models.CharField(choices=ALUNO_84, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='84. Nos últimos 30 dias, em quantos dias você tomou pelo menos um copo ou uma dose de bebida alcoólica (uma dose equivale a uma lata de cerveja ou uma taça de vinho ou uma dose de cachaça ou uísque etc.)?')
    questao_85 = models.CharField(choices=ALUNO_85, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='85. Nos últimos 30 dias, nos dias em que você tomou alguma bebida alcoólica, quantos copos ou doses você tomou por dia?')
    questao_86 = models.CharField(choices=ALUNO_86, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='86. Nos últimos 30 dias, na maioria das vezes, como você conseguiu a bebida que tomou?')
    questao_87 = models.CharField(choices=ALUNO_87, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='87. Na sua vida, quantas vezes você bebeu tanto que ficou realmente bêbado(a)?')
    questao_88 = models.CharField(choices=ALUNO_88, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='88. Na sua vida, quantas vezes você teve problemas com sua família ou amigos, perdeu aulas ou brigou por que tinha bebido?')
    questao_89 = models.CharField(choices=ALUNO_89, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='89. Quantos amigos seus consomem bebida alcoólica?')
    questao_90 = models.CharField(choices=ALUNO_90, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='90. Alguma vez na vida, você já usou alguma droga como: maconha, cocaína, crack, cola, loló, lança-perfume, ecstasy, oxy etc.?')
    questao_91 = models.CharField(choices=ALUNO_91, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='91. Que idade você tinha quando usou alguma droga como: maconha, cocaína, crack, cola, loló, lança-perfume, ecstasy, oxy ou outra pela primeira vez?')
    questao_92 = models.CharField(choices=ALUNO_92, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='92. Nos ultimos 30 dias, quantos dias você usou droga como maconha, cocaína, crack, cola, loló, lança-perfume, ecstasy, oxy etc.?')
    questao_93 = models.CharField(choices=ALUNO_93, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='93. Nos últimos 30 dias, quantos dias você usou maconha?')
    questao_94 = models.CharField(choices=ALUNO_94, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='94. Nos últimos 30 dias, quantos dias você usou crack?')
    questao_95 = models.CharField(choices=ALUNO_95, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='95. Quantos amigos seus usam drogas?')
    questao_96 = models.CharField(choices=ALUNO_96, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='96. Nos últimos 30 dias, em quantos dias você faltou às aulas ou à escola sem permissão dos seus pais ou responsáveis?')
    questao_97 = models.CharField(choices=ALUNO_97, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='97. Nos últimos 30 dias, com que frequência seus pais ou responsáveis sabiam realmente o que você estava fazendo em seu tempo livre?')
    questao_98 = models.CharField(choices=ALUNO_98, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='98. Nos últimos 30 dias, com que frequência seus pais ou responsáveis verificaram se os seus deveres de casa (lição de casa) foram feitos?')
    questao_99 = models.CharField(choices=ALUNO_99, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='99. Nos últimos 30 dias, com que frequência seus pais ou responsáveis entenderam seus problemas e preocupações?')
    questao_100 = models.CharField(choices=ALUNO_100, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='100. Nos últimos 30 dias, com que frequência seus pais ou responsáveis mexeram em suas coisas sem a sua concordância?')
    questao_101 = models.CharField(choices=ALUNO_101, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='101. Nos últimos 30 dias, com que frequência os colegas de sua escola trataram você bem e/ou foram prestativos com você?')
    questao_102 = models.CharField(choices=ALUNO_102, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='102. Nos últimos 30 dias, com que frequência algum dos seus colegas de escola lhe esculacharam, zoaram, mangaram, intimidaram ou caçoaram tanto que você ficou magoado, incomodado, aborrecido, ofendido ou humilhado?')
    questao_103 = models.CharField(choices=ALUNO_103, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='103. Nos últimos 30 dias, qual o motivo ou causa de seus colegas terem lhe esculachado, zombado, zoado, caçoado, mangado, intimidado ou humilhado?')
    questao_104 = models.CharField(choices=ALUNO_104, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='104. Nos últimos 30 dias, você esculachou, zombou, mangou, intimidou ou caçoou algum de seus colegas da escola tanto que ele ficou magoado, aborrecido, ofendido ou humilhado?')
    questao_105 = models.CharField(choices=ALUNO_105, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='105. Você já sofreu bullying?')
    questao_106 = models.CharField(choices=ALUNO_106, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='106. Nos ultimos 12 meses, com que frequência você não conseguiu dormir à noite porque algo o(a) preocupava muito?')
    questao_107 = models.CharField(choices=ALUNO_107, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='107. Quantos amigos(as) próximos você tem?')
    questao_108 = models.CharField(choices=ALUNO_108, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='108. Nos últimos 30 dias, com que frequência você lavou as mãos antes de comer?')
    questao_109 = models.CharField(choices=ALUNO_109, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='109. Nos últimos 30 dias, com que frequência você lavou as mãos após usar o banheiro ou o vaso sanitário?')
    questao_110 = models.CharField(choices=ALUNO_110, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='110. Nos últimos 30 dias, com que frequência você usou sabão ou sabonete quando lavou suas mãos?')
    questao_111 = models.CharField(choices=ALUNO_111, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='111. Nos últimos 30 dias, quantas vezes por dia você usualmente escovou os dentes?')
    questao_112 = models.CharField(choices=ALUNO_112, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='112. Nos últimos 06 meses, você teve dor de dente? (Não vale aquela dor de dente causada por uso de aparelho para correção dos dentes, isto é, aparelhos ortodônticos).)')
    questao_113 = models.CharField(choices=ALUNO_113, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='113. Nos últimos 12 meses, quantas vezes você foi ao dentista?')
    questao_114 = models.CharField(choices=ALUNO_114, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='114. Nos últimos 30 dias, em quantos dias você deixou de ir à escola porque não se sentia seguro no caminho de casa para a escola ou da escola para casa?')
    questao_115 = models.CharField(choices=ALUNO_115, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='115. Nos últimos 30 dias, em quantos dias você não foi à escola porque não se sentia seguro na escola?')
    questao_116 = models.CharField(choices=ALUNO_116, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='116. Nos últimos 30 dias, com que frequência você usou cinto de segurança enquanto andava como passageiro(a) no banco da frente de carro/automóvel, van ou táxi?')
    questao_117 = models.CharField(choices=ALUNO_117, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='117. Nos últimos 30 dias, com que frequência você usou capacete ao andar de motocicleta?')
    questao_118 = models.CharField(choices=ALUNO_118, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='118. Nos últimos 30 dias, quantas vezes você dirigiu um veículo motorizado de transporte? (carro, motocicleta, voadeira, barco, etc.)')
    questao_119 = models.CharField(choices=ALUNO_119, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='119. Nos últimos 30 dias, quantas vezes você andou em carro ou outro veículo motorizado dirigido por alguém que tinha consumido alguma bebida alcoólica?')
    questao_120 = models.CharField(choices=ALUNO_120, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='120. Nos últimos 30 dias, quantas vezes você foi agredido(a) fisicamente por um adulto da sua família?')
    questao_121 = models.CharField(choices=ALUNO_121, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='121. Nos últimos 30 dias, você esteve envolvido(a) em alguma briga em que alguma pessoa usou arma de fogo, como revólver ou espingarda?')
    questao_122 = models.CharField(choices=ALUNO_122, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='122. Nos últimos 30 dias, você esteve envolvido(a) em alguma briga em que alguma pessoa usou alguma outra arma como faca, canivete, peixeira, pedra, pedaço de pau ou garrafa?')
    questao_123 = models.CharField(choices=ALUNO_123, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='123. Nos últimos 12 meses, quantas vezes você foi agredido(a) fisicamente?')
    questao_124 = models.CharField(choices=ALUNO_124, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='124. Nos últimos 12 meses, quantas vezes você se envolveu em briga (uma luta física)?')
    questao_125 = models.CharField(choices=ALUNO_125, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='125. Nos últimos 12 meses, quantas vezes você foi seriamente ferido(a) em uma briga?')
    questao_126 = models.CharField(choices=ALUNO_126, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='126. Nos últimos 12 meses, qual foi o ferimento ou a lesão mais séria que aconteceu com você?')
    questao_127 = models.CharField(choices=ALUNO_127, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='127. Nos últimos 12 meses, qual foi a principal causa do ferimento ou da lesão mais séria que aconteceu com você?')
    questao_128 = models.CharField(choices=ALUNO_128, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='128. Nos últimos 12 meses, você sofreu algum acidente de bicicleta (caiu e se machucou)?')
    questao_129 = models.CharField(choices=ALUNO_129, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='129. Alguma vez na vida você foi forçado(a) a ter relação sexual?')
    questao_130 = models.CharField(choices=ALUNO_130, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='130. Quem forçou você a ter relação sexual?')
    questao_131 = models.CharField(choices=ALUNO_131, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='131. Como você classificaria seu estado de saúde?')
    questao_132 = models.CharField(choices=ALUNO_132, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='132. Nos últimos 12 meses, quantos dias você faltou a escola por motivo(s) relacionado(s) à sua saúde?')
    questao_133 = models.CharField(choices=ALUNO_133, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='133. Nos últimos 12 meses você procurou algum serviço ou profissional de saúde para atendimento relacionado à própria saúde?')
    questao_134 = models.CharField(choices=ALUNO_134, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='134. Nos últimos 12 meses, qual foi o serviço de saúde que você procurou com mais frequência?')
    questao_135 = models.CharField(choices=ALUNO_135, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='135. Você foi atendido(a) na última vez que procurou alguma Unidade Básica de Saúde (Centro ou Posto de saúde ou Unidade de Saúde da Família/PSF), nestes últimos 12 meses?')
    questao_136 = models.CharField(choices=ALUNO_136, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='136. Qual foi o principal motivo da sua procura na Unidade Básica de Saúde (Centro ou Posto de saúde ou Unidade de Saúde da Família/PSF) nesta última vez?')
    questao_137 = models.CharField(choices=ALUNO_137, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='137. Você conhece/ouviu falar sobre a campanha de vacinação contra o vírus HPV?')
    questao_138 = models.CharField(choices=ALUNO_138, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='138. Você foi vacinada contra o vírus HPV?')
    questao_139 = models.CharField(choices=ALUNO_139, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='139. Você considera sua imagem corporal como sendo algo:')
    questao_140 = models.CharField(choices=ALUNO_140, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='140. Como você se sente em relação ao seu corpo?')
    questao_141 = models.CharField(choices=ALUNO_141, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='141. Quanto ao seu corpo, você se considera:')
    questao_142 = models.CharField(choices=ALUNO_142, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='142. O que você está fazendo em relação a seu peso?')
    questao_143 = models.CharField(choices=ALUNO_143, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='143. Nos últimos 30 dias, você vomitou ou tomou laxantes para perder peso ou evitar ganhar peso?')
    questao_144 = models.CharField(choices=ALUNO_144, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='144. Nos últimos 30 dias, você tomou algum remédio, fórmula ou outro produto para perder peso, sem acompanhamento médico?')
    questao_145 = models.CharField(choices=ALUNO_145, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='145. Nos últimos 30 dias, você tomou algum remédio, fórmula ou outro produto para ganhar peso ou massa muscular sem acompanhamento médico?')
    questao_146 = ArrayField(models.CharField(choices=ALUNO_146, max_length=TAMANHO_OPCOES), blank=True, null=True, verbose_name='146. O que você achou deste questionário?')

    class Meta:
        verbose_name = 'Questionário'
        verbose_name_plural = 'Questionários'

    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.nome


class Exame(models.Model):
    """Modelo que representa um exame completo"""
    aluno = models.OneToOneField('Aluno', on_delete=models.CASCADE)
    data = models.DateField(blank=True, null=True, verbose_name='Data')
    examinador = models.CharField(max_length=TAMANHO_NOMES, blank=True, null=True, verbose_name='Examinador')
    anotador = models.CharField(max_length=TAMANHO_NOMES, blank=True, null=True, verbose_name='Anotador')
    
    # Cárie
    carie_coroa_18 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 18')
    carie_tratamento_18 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 18')
    
    carie_coroa_17 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 17')
    carie_tratamento_17 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 17')

    carie_coroa_16 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 16')
    carie_tratamento_16 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 16')

    carie_coroa_15 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 15')
    carie_tratamento_15 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 15')

    carie_coroa_14 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 14')
    carie_tratamento_14 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 14')

    carie_coroa_13 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 13')
    carie_tratamento_13 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 13')

    carie_coroa_12 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 12')
    carie_tratamento_12 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 12')

    carie_coroa_11 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 11')
    carie_tratamento_11 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 11')
    
    carie_coroa_21 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 21')
    carie_tratamento_21 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 21')

    carie_coroa_22 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 22')
    carie_tratamento_22 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 22')

    carie_coroa_23 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 23')
    carie_tratamento_23 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 23')

    carie_coroa_24 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 24')
    carie_tratamento_24 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 24')

    carie_coroa_25 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 25')
    carie_tratamento_25 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 25')

    carie_coroa_26 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 26')
    carie_tratamento_26 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 26')

    carie_coroa_27 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 27')
    carie_tratamento_27 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 27')

    carie_coroa_28 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 28')
    carie_tratamento_28 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 28')

    carie_coroa_38 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 38')
    carie_tratamento_38 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 38')

    carie_coroa_37 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 37')
    carie_tratamento_37 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 37')

    carie_coroa_36 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 36')
    carie_tratamento_36 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 36')

    carie_coroa_35 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 35')
    carie_tratamento_35 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 35')

    carie_coroa_34 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 34')
    carie_tratamento_34 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 34')

    carie_coroa_33 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 33')
    carie_tratamento_33 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 33')

    carie_coroa_32 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 32')
    carie_tratamento_32 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 32')

    carie_coroa_31 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 31')
    carie_tratamento_31 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 31')

    carie_coroa_41 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 41')
    carie_tratamento_41 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 41')

    carie_coroa_42 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 42')
    carie_tratamento_42 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 42')

    carie_coroa_43 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 43')
    carie_tratamento_43 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 43')

    carie_coroa_44 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 44')
    carie_tratamento_44 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 44')

    carie_coroa_45 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 45')
    carie_tratamento_45 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 45')

    carie_coroa_46 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 46')
    carie_tratamento_46 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 46')

    carie_coroa_47 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 47')
    carie_tratamento_47 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 47')

    carie_coroa_48 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Coroa 48')
    carie_tratamento_48 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Tratamento 48')
    
    # Periodontal
    periodontal_sangramento_1716 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Sangramento 17/16')
    periodontal_calculo_1716 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Cálculo dentário 17/16')
    periodontal_bolsa_1716 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Bolsa periodontal 17/16')
    
    periodontal_sangramento_11 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Sangramento 11')
    periodontal_calculo_11 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Cálculo dentário 11')
    periodontal_bolsa_11 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Bolsa periodontal 11')

    periodontal_sangramento_2627 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Sangramento 26/27')
    periodontal_calculo_2627 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Cálculo dentário 26/27')
    periodontal_bolsa_2627 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Bolsa periodontal 26/27')

    periodontal_sangramento_3736 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Sangramento 37/36')
    periodontal_calculo_3736 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Cálculo dentário 37/36')
    periodontal_bolsa_3736 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Bolsa periodontal 37/36')

    periodontal_sangramento_31 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Sangramento 31')
    periodontal_calculo_31 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Cálculo dentário 31')
    periodontal_bolsa_31 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Bolsa periodontal 31')

    periodontal_sangramento_4647 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Sangramento 46/47')
    periodontal_calculo_4647 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Cálculo dentário 46/47')
    periodontal_bolsa_4647 = models.CharField(max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='Bolsa periodontal 46/47')
    
    def __str__(self):
        """Devolve a representação do modelo em string"""
        return str(self.aluno.numero_identificacao)


class Diretor(models.Model):
    """Modelo que representa um questionário para ser respondido pelo diretor de escola"""
    escola = models.ForeignKey('Escola', related_name='diretores', on_delete=models.CASCADE)
    data = models.DateField(blank=True, null=True, verbose_name="Data de preenchimento")
    
    questao_1 = models.CharField(choices=DIRETOR_1, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='1. A escola funciona em quais turnos? (múltipla resposta)')
    questao_2 = models.CharField(choices=DIRETOR_2, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='2. A escola funciona em regime integral?')
    questao_3 = models.CharField(choices=DIRETOR_3, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='3. A escola atende a quais etapas de ensino? (múltipla resposta)')
    questao_4 = models.CharField(choices=DIRETOR_4, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='4. Qual é o TOTAL de alunos matriculados?')
    questao_5 = models.CharField(choices=DIRETOR_5, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='5. Qual é a quantidade TOTAL de salas de aula da escola?')
    questao_6 = models.CharField(choices=DIRETOR_6, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='6. A escola tem biblioteca EM CONDIÇÕES DE USO?')
    questao_7 = models.CharField(choices=DIRETOR_7, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='7. A escola tem sala ou laboratório de informática EM CONDIÇÕES DE USO para os alunos?')
    questao_8 = models.CharField(choices=DIRETOR_8, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='8. Quantos computadores (desktops, laptops, notebooks, netbooks, tablets) da escola EM CONDIÇÕES DE USO estão disponíveis para os alunos em sala de aula e/ou salas específicas de informática?')
    questao_9 = models.CharField(choices=DIRETOR_9, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='9. Os alunos têm acesso à internet através de equipamentos da escola?')
    questao_10 = models.CharField(choices=DIRETOR_10, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='10. A escola tem sala de recursos de mídia/comunicação EM CONDIÇÕES DE USO? (Exemplos: televisão, videocassete, dvd, projetor etc)')
    questao_11 = models.CharField(choices=DIRETOR_11, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='11. A escola tem conselho escolar?')
    questao_12 = models.CharField(choices=DIRETOR_12, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='12. Com que frequência o conselho escolar se reúne?')
    questao_13 = models.CharField(choices=DIRETOR_13, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='13. A escola fica aberta nos finais de semana para uso da comunidade?')
    questao_14 = models.CharField(choices=DIRETOR_14, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='14. As ações desenvolvidas na escola, no final de semana, são pactuadas com a comunidade?')
    questao_15 = models.CharField(choices=DIRETOR_15, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='15. A escola tem quadra de esportes EM CONDIÇÕES DE USO?')
    questao_16 = models.CharField(choices=DIRETOR_16, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='16. Quantas quadras de esporte EM CONDIÇÕES DE USO a escola tem?')
    questao_17 = models.CharField(choices=DIRETOR_17, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='17. Quantas das quadras de esporte EM CONDIÇÕES DE USO da escola são cobertas?')
    questao_18 = models.CharField(choices=DIRETOR_18, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='18. A escola tem pista para corrida/atletismo EM CONDIÇÕES DE USO?')
    questao_19 = models.CharField(choices=DIRETOR_19, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='19. A escola tem piscina EM CONDIÇÕES DE USO?')
    questao_20 = models.CharField(choices=DIRETOR_20, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='20. O pátio da escola é utilizado para prática regular de atividade física com instrutor?')
    questao_21 = models.CharField(choices=DIRETOR_21, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='21. A escola tem material esportivo ou para jogos e brincadeiras EM CONDIÇÕES DE USO?')
    questao_22 = models.CharField(choices=DIRETOR_22, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='22. A escola tem vestiário EM CONDIÇÕES DE USO para os alunos?')
    questao_23 = models.CharField(choices=DIRETOR_23, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='23. A escola tem vestiários separados para alunos e alunas EM CONDIÇÕES DE USO?')
    questao_24 = models.CharField(choices=DIRETOR_24, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='24. A escola oferece atividades esportivas para os alunos fora do horário regular de aula?')
    questao_25 = models.CharField(choices=DIRETOR_25, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='25. A escola participa de jogos entre escolas?')
    questao_26 = models.CharField(choices=DIRETOR_26, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='26. A escola realiza jogos entre as classes, turmas ou turnos?')
    questao_27 = models.CharField(choices=DIRETOR_27, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='27. A escola possui alunos com deficiência ou com transtorno global do desenvolvimento?')
    questao_28 = models.CharField(choices=DIRETOR_28, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='28. Qual(is) tipo(s) de deficiência? (múltipla resposta)')
    questao_29 = models.CharField(choices=DIRETOR_29, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='29. A escola oferece atividade física adaptada para alunos com deficiência?')
    questao_30 = models.CharField(choices=DIRETOR_30, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='30. A escola possui estrutura para assegurar a acessibilidade dos alunos com necessidades especiais?')
    questao_31 = models.CharField(choices=DIRETOR_31, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='31. Quais estruturas existem na escola para assegurar a acessibilidade dos alunos com necessidades especiais? (múltipla resposta)')
    questao_32 = models.CharField(choices=DIRETOR_32, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='32. A escola oferece comida (merenda escolar / almoço) para os estudantes?')
    questao_33 = models.CharField(choices=DIRETOR_33, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='33. A escola oferece comida (merenda escolar / almoço) para alunos de quais turnos e níveis de ensino? (múltipla resposta)')
    questao_34 = models.CharField(choices=DIRETOR_34, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='34. A escola tem cozinha EM CONDIÇÕES DE USO?')
    questao_35 = models.CharField(choices=DIRETOR_35, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='35. A escola tem refeitório EM CONDIÇÕES DE USO? (espaço exclusivo para servir alimentação)')
    questao_36 = models.CharField(choices=DIRETOR_36, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='36. A escola tem cantina?')
    questao_37 = models.CharField(choices=DIRETOR_37, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='37. Que tipos de bebidas e produtos alimentícios são vendidos na cantina? (múltipla resposta)láctea)')
    questao_38 = models.CharField(choices=DIRETOR_38, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='38. Existe algum ponto alternativo de venda de produtos alimentícios dentro ou na entrada da escola? (ex: ambulante/carrocinha)')
    questao_39 = models.CharField(choices=DIRETOR_39, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='39. Que tipos de bebidas e produtos alimentícios são vendidos no ponto alternativo de vendas? (múltipla resposta)láctea)')
    questao_40 = models.CharField(choices=DIRETOR_40, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='40. A escola tem horta?')
    questao_41 = models.CharField(choices=DIRETOR_41, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='41. A escola tem água potável (adequada para beber) para uso dos alunos?')
    questao_42 = models.CharField(choices=DIRETOR_42, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='42. NOS ÚLTIMOS 12 MESES, alguma vez a água da escola foi testada quanto a sua potabilidade (se é adequada para beber)?')
    questao_43 = models.CharField(choices=DIRETOR_43, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='43. Qual é a principal fonte de água potável (adequada para beber) da escola?')
    questao_44 = models.CharField(choices=DIRETOR_44, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='44. A escola tem banheiros EM CONDIÇÕES DE USO?')
    questao_45 = models.CharField(choices=DIRETOR_45, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='45. A escola tem banheiros separados para alunos e alunas EM CONDIÇÕES DE USO?')
    questao_46 = models.CharField(choices=DIRETOR_46, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='46. A escola oferece papel higiênico para uso nos banheiros da escola?')
    questao_47 = models.CharField(choices=DIRETOR_47, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='47. A escola tem pia ou lavatório EM CONDIÇÕES DE USO onde os estudantes possam lavar as mãos depois de ir ao banheiro e/ou antes das refeições?')
    questao_48 = models.CharField(choices=DIRETOR_48, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='48. A escola oferece sabão para que os alunos lavem as mãos após usar o banheiro e/ou antes das refeições?')
    questao_49 = models.CharField(choices=DIRETOR_49, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='49. Normalmente, com que frequência a remoção do lixo é feita pela escola?')
    questao_50 = models.CharField(choices=DIRETOR_50, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='50. A escola tem escovódromo?')
    questao_51 = models.CharField(choices=DIRETOR_51, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='51. A escola realiza alguma Ação de Saúde Bucal?')
    questao_52 = models.CharField(choices=DIRETOR_52, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='52. Escovação dental supervisionada')
    questao_53 = models.CharField(choices=DIRETOR_53, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='53. Caso positivo, com qual frequência?')
    questao_54 = models.CharField(choices=DIRETOR_54, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='54. Aplicação Tópica de Flúor')
    questao_55 = models.CharField(choices=DIRETOR_55, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='55. Caso positivo, com qual frequência?')
    questao_56 = models.CharField(choices=DIRETOR_56, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='56. Bochechos fluorados')
    questao_57 = models.CharField(choices=DIRETOR_57, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='57. Caso positivo, com qual frequência?')
    questao_58 = models.CharField(choices=DIRETOR_58, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='58. A escola realiza ação de Educação em Saúde Bucal?')
    questao_59 = models.CharField(choices=DIRETOR_59, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='59. Estas ações estão incluídas no currículo escolar?')
    questao_60 = models.CharField(choices=DIRETOR_60, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='60. Sua escola já realizou Levantamento Epidemiológico sobre cárie dentária?')
    questao_61 = models.CharField(choices=DIRETOR_61, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='61. Caso positivo você conhece (eu) os resultados?')
    questao_62 = models.CharField(choices=DIRETOR_62, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='62. Sua escola disponibiliza escovas dentais para os estudantes?')
    questao_63 = models.CharField(choices=DIRETOR_63, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='63. Caso positivo, com qual frequência?')
    questao_64 = models.CharField(choices=DIRETOR_64, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='64. Sua escola disponibiliza creme dental para os estudantes?')
    questao_65 = models.CharField(choices=DIRETOR_65, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='65. Sua escola disponibiliza fio dental para os estudantes?')
    questao_66 = models.CharField(choices=DIRETOR_66, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='66. NOS ÚLTIMOS 12 MESES, com que frequência, a localidade onde a escola está situada foi considerada área de risco em termos de violência (roubos, furtos, assaltos, troca de tiros, consumo de drogas, homicídios etc)?')
    questao_67 = models.CharField(choices=DIRETOR_67, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='67. NOS ÚLTIMOS 12 MESES, a escola teve que suspender ou interromper suas aulas por motivo de segurança em termos de violência?')
    questao_68 = models.CharField(choices=DIRETOR_68, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='68. A escola tem algum grupo ou comitê responsável por orientar ou coordenar ações e/ou atividades relacionadas à saúde?')
    questao_69 = models.CharField(choices=DIRETOR_69, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='69. A escola aderiu ao Programa Saúde da Escola (PSE)?')
    questao_70 = models.CharField(choices=DIRETOR_70, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='70. Caso positivo, qual o ano da adesão da escola ao Programa Saúde na Escola (PSE)?')
    questao_71 = models.CharField(choices=DIRETOR_71, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='71. A escola implementa ações do Programa Saúde da Escola (PSE)?')
    questao_72 = models.CharField(choices=DIRETOR_72, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='72. A escola implementa ações do Programa Mais Educação?')
    questao_73 = models.CharField(choices=DIRETOR_73, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='73. A escola realiza ações conjuntas com Unidade Básica de Saúde ou Equipe de Saúde da Família ou Equipe de Atenção Básica?')
    questao_74 = models.CharField(choices=DIRETOR_74, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='74. A escola mantém registros sobre a caderneta de vacinação dos escolares?')
    questao_75 = models.CharField(choices=DIRETOR_75, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='75. A escola mantém outros registros sobre a saúde dos escolares? (histórico clínico,ocorrência de alergias, acidentes, tipo sanguíneo, doenças etc)')
    questao_76 = models.CharField(choices=DIRETOR_76, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='76. A escola tem material e/ou medicamentos de Primeiros Socorros mantidos em local adequado?')
    questao_77 = models.CharField(choices=DIRETOR_77, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='77. A escola tem conhecimento de consumo de cigarro por professores nas suas dependências?')
    questao_78 = models.CharField(choices=DIRETOR_78, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='78. A escola tem conhecimento de consumo de cigarro por alunos nas suas dependências?')
    questao_79 = models.CharField(choices=DIRETOR_79, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='79. A escola tem alguma política, norma ou regra escrita que proíba o uso do tabaco nas suas dependências?')
    questao_80 = models.CharField(choices=DIRETOR_80, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='80. A escola tem alguma política, norma ou regra escrita que proíba o uso de drogas ilícitas nas suas dependências?')
    questao_81 = models.CharField(choices=DIRETOR_81, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='81. A escola tem alguma política, norma ou regra escrita que proíba bullying nas suas dependências?')
    questao_82 = models.CharField(choices=DIRETOR_82, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='82. A escola tem alguma política, norma ou regra escrita que proíba brigas nas suas dependências?')
    questao_83 = models.CharField(choices=DIRETOR_83, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='83. A escola tem alguma política, norma ou regra escrita que proíba punição física dos estudantes pelos professores ou funcionários nas suas dependências?')
    questao_84 = models.CharField(choices=DIRETOR_84, max_length=TAMANHO_OPCOES, blank=True, null=True, verbose_name='84. A escola está situada em área de vulnerabilidade social?')
    
    class Meta:
        verbose_name = 'Questionário para diretores'
        verbose_name_plural = 'Questionários para diretores'
    
    def __str__(self):
        """Devolve a representação do modelo em string"""
        return str(self.escola.numero_identificacao)
