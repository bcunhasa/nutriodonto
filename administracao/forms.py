from django import forms
from django.contrib.auth.models import User

from .models import *


class LoginForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'password']


class CampanhaForm(forms.ModelForm):
    
    class Meta:
        model = Campanha
        fields = '__all__'


class AcaoForm(forms.ModelForm):
    
    class Meta:
        model = Acao
        fields = '__all__'


class EscolaForm(forms.ModelForm):
    
    class Meta:
        model = Escola
        fields = '__all__'


class AlunoForm(forms.ModelForm):
    
    class Meta:
        model = Aluno
        fields = '__all__'


class QuestionarioForm(forms.ModelForm):
    
    class Meta:
        model = Questionario
        fields = '__all__'


class QuestionarioInglesForm(forms.ModelForm):
    
    class Meta:
        model = Questionario
        fields = '__all__'
        labels = {
            'questao_1': '01. What is the highest level of education you intend to complete?',
            'questao_2': '02. When you finish the cycle / course you are currently attending, do you intend to?',
            'questao_3': '03. Do you live with your mother?',
            'questao_4': '04. Do you live with your father?',
            
            'questao_5': '05. Counting on you, how many people live in your house or apartment?',
            'questao_6': '06. Does your home have a landline (conventional)?',
            'questao_7': '07. Do you have a cell phone?',
            'questao_8': '08. Does your home have a computer (desktop, laptop, etc.)?',
            'questao_9': '09. Do you have internet access in your home?',
            'questao_10': '10. Does anyone who lives in your house have a car?',
            'questao_11': '11. Does anyone who lives in your house have a motorcycle?',
            'questao_12': '12. How many bathrooms with showers do you have inside your home?',
            'questao_13': '13. Do you have a domestic worker at home?',
            'questao_14': '14. If YES, how many days does this person work?',
            'questao_15': '15. What level of education (degree) did your mother study or study at?',
            'questao_16': '16. Do you currently have a job, job or business?',
            'questao_17': '17. Do you get money for this job, job or business?',
            'questao_18': '18. Does your family receive Bolsa Familia benefits?',
            'questao_19': '19. Do you usually have breakfast?',
            'questao_20': '20. Do you usually have lunch or dinner with your mother, father or guardian?',
            'questao_21': '21. Do you usually eat when watching TV or studying?',
            'questao_22': '22. Does your school offer food (school lunch / lunch) to students in your class? (Do not consider canteen-bought snacks / food)',
            'questao_23': '23. Do you usually eat the food (meals / lunch) offered by the school?',
            'questao_24': '24. In the last 30 days, how often have you been hungry for not having enough food in your home?',
            
            'questao_25': '25. Cow milk: ',
            'questao_26': '26. Cow\'s milk with added chocolate powder (nescau, toddy, ovomaltine), honey or sugar:',
            'questao_27': '27. Liquid chocolate bought in supermarkets, such as Todyynho, Chokinho; Nescau; Italac etc.',
            'questao_28': '28. Yogurt such as Danone, Danoninho, Nestlé, Ninho, etc.',
            'questao_29': '29. Cheese.',
            'questao_30': '30. Desserts made with milk (pudding, flam, chocolate pudding, sour cream).',
            'questao_31': '31. Ice Cream (Popsicle, Ice Cream, Ice Cream).',
            'questao_32': '32. Bread or toast (Toast is the same as bread, but toasted).',
            'questao_33': '33. Sugary cereal flakes (for example, flakes known as cornflakes or the like, nescau cereal), etc.',
            'questao_34': '34. Cereal flakes (oats, maize, rye, such as Nesfit and Nutry)',
            'questao_35': '35. Rice, pasta, potatoes.',
            'questao_36': '36. Chips Pack Ruffles, Pringles, Lay\'s',
            'questao_37': '37. Homemade French Fries.',
            'questao_38': '38. Maria biscuits, Mabel biscuits, cream crackers (or water and salt) etc.',
            'questao_39': '39. Other cookies (stuffed cookies like Bono, Trakinas and Oreo).',
            'questao_40': '40. Pastry products (drumsticks, pastries, cheese chips, kibes).',
            'questao_41': '41. Snacks (chocolate sold in bars, such as Twix, Kitkat, Bis and Chokito)',
            'questao_42': '42. Marmalade, sweet in jars, jam, honey. (Like Paçoquita, Melzinho and Kid\'s foot)',
            
            'questao_43': '43. Sugars in general.',
            'questao_44': '44. Homemade common soups (meat, chicken or vegetables)',
            'questao_45': '45. Raw salad or cooked vegetables (Carrot, Cauliflower, Broccoli, Lettuce, Beetroot, Watercress)',
            'questao_46': '46. Legumes (beans, chickpeas, peas, broad beans).',
            'questao_47': '47. Fresh fruit. (Mango, cashew, banana, guava, acerola, murici, apple, orange)',
            
            'questao_48': '48. Canned fruit in syrup: (peach, banana, cashew, guava).',
            'questao_49': '49. Natural juices (Orange, Acerola, Tangerine, Grape)',
            'questao_50': '50. Soft drinks (Coca cola, Grana or Fanta) or boxed juices with nectar (such as Kapo, del Valle)',
            'questao_51': '51. Pizzas. (Mini Pizza for example)',
            'questao_52': '52. Burger and hot dog.',
            'questao_53': '53. Candies, gums, chewing gum. (Chewing Gum, Candies, Jelly Beans)',
            'questao_54': '54. Donuts (like Donuts, Dreams, Sprinkles Donuts, Gingerbread)',
            'questao_55': '55. Has your child been fed breast milk?',
            'questao_56': '56. Did you breastfeed (chest only) until how many months old?',
            
            'questao_57': '57. If your child has breastfed for up to six months or more, how many months he or she has breastfed (even if he or she has eaten other foods or drinks)',
            'questao_58': '58. Before you were two years old, was your child fed industrial milk? (that milk bought at pharmacies or supermarkets)',
            'questao_59': '59. If your answer was YES, how many months did he feed on industrial milk, that is, milk that is bought at pharmacies and supermarkets?',
            'questao_60': '60. Up to two years of age, your son or daughter has received mixed feeding, ie:',
            'questao_61': '61. Up to two years old, did your son or daughter drink cow\'s milk?',
            'questao_62': '62. If so, at what age (in months) did he start drinking cow\'s milk?',
            'questao_63': '63. In the last few days, how many of them have you been walking or cycling to school?',
            
            'questao_64': '64. When you go to school on foot or by bike, how much time do you spend?',
            'questao_65': '65. In the last 7 days, how many days did you take PE classes at school?',
            'questao_66': '66. In the last seven days, how long per day did you do physical activity or sport during physical education classes at school?',
            'questao_67': '67. In the last 7 days, not counting school physical education classes, how many days have you been engaged in any physical activity such as sports, dancing, gymnastics, bodybuilding, wrestling or any other activity?',
            'questao_68': '68. How often do these activities (such as sports, dance, gymnastics, bodybuilding, wrestling, or other activity) last a day? (Not counting physical education classes)',
            'questao_69': '69. In the last 7 days, how many days have you been doing physical activity for at least 60 minutes (1 hour) a day? (Add up all the time you spent on any kind of physical activity each day)',
            'questao_70': '70. If you had the opportunity to do physical activity most days of the week, what would you do?',
            'questao_71': '71. On a typical weekday, how many hours a day do you watch TV? (do not count Saturday, Sunday and holiday)',
            'questao_72': '72. On a typical weekday, how long do you sit around watching television, using a computer, playing video games, talking to friends, or doing other sitting activities? (do not count Saturday, Sunday, holidays and time sitting at school)',
            
            'questao_73': '73. Alguma vez na vida, você já fumou cigarro, mesmo uma ou duas tragadas?',
            'questao_74': '74. Que idade você tinha quando experimentou fumar cigarro pela primeira vez?',
            'questao_75': '75. Nos últimos 30 dias, em quantos dias você fumou cigarros?',
            'questao_76': '76. Nos últimos 30 dias, em geral, como você conseguiu seus próprios cigarros?',
            'questao_77': '77. Nos ultimos 30 dias, alguém se recusou a lhe vender cigarros por causa de sua idade?',
            'questao_78': '78. Nos últimos 30 dias, em quantos dias você usou outros produtos de tabaco: cigarros de palha ou enrolados a mão, charuto, cachimbo, cigarrilha, cigarro indiano ou bali, narguilé, rapé, fumo de mascar etc.? (não incluir cigarro comum)',
            'questao_79': '79. Qual outro produto do tabaco você usou com mais frequência nos últimos 30 dias?',
            'questao_80': '80. Nos últimos 7 dias, em quantos dias pessoas fumaram na sua presença?',
            'questao_81': '81. Algum de seus pais ou responsáveis fuma?',
            'questao_82': '82. Alguma vez na vida você tomou uma dose de bebida alcoólica (uma dose equivale a uma lata de cerveja ou uma taça de vinho ou uma dose de cachaça ou uísque etc.)?',
            'questao_83': '83. Que idade você tinha quando tomou a primeira dose de bebida alcoólica (uma dose equivale a uma lata de cerveja ou uma taça de vinho ou uma dose de cachaça ou uísque etc.)?',
            'questao_84': '84. Nos últimos 30 dias, em quantos dias você tomou pelo menos um copo ou uma dose de bebida alcoólica (uma dose equivale a uma lata de cerveja ou uma taça de vinho ou uma dose de cachaça ou uísque etc.)?',
            'questao_85': '85. Nos últimos 30 dias, nos dias em que você tomou alguma bebida alcoólica, quantos copos ou doses você tomou por dia?',
            'questao_86': '86. Nos últimos 30 dias, na maioria das vezes, como você conseguiu a bebida que tomou?',
            'questao_87': '87. Na sua vida, quantas vezes você bebeu tanto que ficou realmente bêbado(a)?',
            'questao_88': '88. Na sua vida, quantas vezes você teve problemas com sua família ou amigos, perdeu aulas ou brigou por que tinha bebido?',
            'questao_89': '89. Quantos amigos seus consomem bebida alcoólica?',
            'questao_90': '90. Alguma vez na vida, você já usou alguma droga como: maconha, cocaína, crack, cola, loló, lança-perfume, ecstasy, oxy etc.?',
            'questao_91': '91. Que idade você tinha quando usou alguma droga como: maconha, cocaína, crack, cola, loló, lança-perfume, ecstasy, oxy ou outra pela primeira vez?',
            'questao_92': '92. Nos ultimos 30 dias, quantos dias você usou droga como maconha, cocaína, crack, cola, loló, lança-perfume, ecstasy, oxy etc.?',
            'questao_93': '93. Nos últimos 30 dias, quantos dias você usou maconha?',
            'questao_94': '94. Nos últimos 30 dias, quantos dias você usou crack?',
            'questao_95': '95. Quantos amigos seus usam drogas?',
            'questao_96': '96. Nos últimos 30 dias, em quantos dias você faltou às aulas ou à escola sem permissão dos seus pais ou responsáveis?',
            'questao_97': '97. Nos últimos 30 dias, com que frequência seus pais ou responsáveis sabiam realmente o que você estava fazendo em seu tempo livre?',
            'questao_98': '98. Nos últimos 30 dias, com que frequência seus pais ou responsáveis verificaram se os seus deveres de casa (lição de casa) foram feitos?',
            'questao_99': '99. Nos últimos 30 dias, com que frequência seus pais ou responsáveis entenderam seus problemas e preocupações?',
            'questao_100': '100. Nos últimos 30 dias, com que frequência seus pais ou responsáveis mexeram em suas coisas sem a sua concordância?',
            'questao_101': '101. Nos últimos 30 dias, com que frequência os colegas de sua escola trataram você bem e/ou foram prestativos com você?',
            'questao_102': '102. Nos últimos 30 dias, com que frequência algum dos seus colegas de escola lhe esculacharam, zoaram, mangaram, intimidaram ou caçoaram tanto que você ficou magoado, incomodado, aborrecido, ofendido ou humilhado?',
            'questao_103': '103. Nos últimos 30 dias, qual o motivo ou causa de seus colegas terem lhe esculachado, zombado, zoado, caçoado, mangado, intimidado ou humilhado?',
            'questao_104': '104. Nos últimos 30 dias, você esculachou, zombou, mangou, intimidou ou caçoou algum de seus colegas da escola tanto que ele ficou magoado, aborrecido, ofendido ou humilhado?',
            'questao_105': '105. Você já sofreu bullying?',
            'questao_106': '106. Nos ultimos 12 meses, com que frequência você não conseguiu dormir à noite porque algo o(a) preocupava muito?',
            'questao_107': '107. Quantos amigos(as) próximos você tem?',
            'questao_108': '108. Nos últimos 30 dias, com que frequência você lavou as mãos antes de comer?',
            'questao_109': '109. Nos últimos 30 dias, com que frequência você lavou as mãos após usar o banheiro ou o vaso sanitário?',
            'questao_110': '110. Nos últimos 30 dias, com que frequência você usou sabão ou sabonete quando lavou suas mãos?',
            'questao_111': '111. Nos últimos 30 dias, quantas vezes por dia você usualmente escovou os dentes?',
            'questao_112': '112. Nos últimos 06 meses, você teve dor de dente? (Não vale aquela dor de dente causada por uso de aparelho para correção dos dentes, isto é, aparelhos ortodônticos).)',
            'questao_113': '113. Nos últimos 12 meses, quantas vezes você foi ao dentista?',
            'questao_114': '114. Nos últimos 30 dias, em quantos dias você deixou de ir à escola porque não se sentia seguro no caminho de casa para a escola ou da escola para casa?',
            'questao_115': '115. Nos últimos 30 dias, em quantos dias você não foi à escola porque não se sentia seguro na escola?',
            'questao_116': '116. Nos últimos 30 dias, com que frequência você usou cinto de segurança enquanto andava como passageiro(a) no banco da frente de carro/automóvel, van ou táxi?',
            'questao_117': '117. Nos últimos 30 dias, com que frequência você usou capacete ao andar de motocicleta?',
            'questao_118': '118. Nos últimos 30 dias, quantas vezes você dirigiu um veículo motorizado de transporte? (carro, motocicleta, voadeira, barco, etc.)',
            'questao_119': '119. Nos últimos 30 dias, quantas vezes você andou em carro ou outro veículo motorizado dirigido por alguém que tinha consumido alguma bebida alcoólica?',
            'questao_120': '120. Nos últimos 30 dias, quantas vezes você foi agredido(a) fisicamente por um adulto da sua família?',
            'questao_121': '121. Nos últimos 30 dias, você esteve envolvido(a) em alguma briga em que alguma pessoa usou arma de fogo, como revólver ou espingarda?',
            'questao_122': '122. Nos últimos 30 dias, você esteve envolvido(a) em alguma briga em que alguma pessoa usou alguma outra arma como faca, canivete, peixeira, pedra, pedaço de pau ou garrafa?',
            'questao_123': '123. Nos últimos 12 meses, quantas vezes você foi agredido(a) fisicamente?',
            'questao_124': '124. Nos últimos 12 meses, quantas vezes você se envolveu em briga (uma luta física)?',
            'questao_125': '125. Nos últimos 12 meses, quantas vezes você foi seriamente ferido(a) em uma briga?',
            'questao_126': '126. Nos últimos 12 meses, qual foi o ferimento ou a lesão mais séria que aconteceu com você?',
            'questao_127': '127. Nos últimos 12 meses, qual foi a principal causa do ferimento ou da lesão mais séria que aconteceu com você?',
            'questao_128': '128. Nos últimos 12 meses, você sofreu algum acidente de bicicleta (caiu e se machucou)?',
            'questao_129': '129. Alguma vez na vida você foi forçado(a) a ter relação sexual?',
            'questao_130': '130. Quem forçou você a ter relação sexual?',
            'questao_131': '131. Como você classificaria seu estado de saúde?',
            'questao_132': '132. Nos últimos 12 meses, quantos dias você faltou a escola por motivo(s) relacionado(s) à sua saúde?',
            'questao_133': '133. Nos últimos 12 meses você procurou algum serviço ou profissional de saúde para atendimento relacionado à própria saúde?',
            'questao_134': '134. Nos últimos 12 meses, qual foi o serviço de saúde que você procurou com mais frequência?',
            'questao_135': '135. Você foi atendido(a) na última vez que procurou alguma Unidade Básica de Saúde (Centro ou Posto de saúde ou Unidade de Saúde da Família/PSF), nestes últimos 12 meses?',
            'questao_136': '136. Qual foi o principal motivo da sua procura na Unidade Básica de Saúde (Centro ou Posto de saúde ou Unidade de Saúde da Família/PSF) nesta última vez?',
            'questao_137': '137. Você conhece/ouviu falar sobre a campanha de vacinação contra o vírus HPV?',
            'questao_138': '138. Você foi vacinada contra o vírus HPV?',
            'questao_139': '139. Você considera sua imagem corporal como sendo algo:',
            'questao_140': '140. Como você se sente em relação ao seu corpo?',
            'questao_141': '141. Quanto ao seu corpo, você se considera:',
            'questao_142': '142. O que você está fazendo em relação a seu peso?',
            'questao_143': '143. Nos últimos 30 dias, você vomitou ou tomou laxantes para perder peso ou evitar ganhar peso?',
            'questao_144': '144. Nos últimos 30 dias, você tomou algum remédio, fórmula ou outro produto para perder peso, sem acompanhamento médico?',
            'questao_145': '145. Nos últimos 30 dias, você tomou algum remédio, fórmula ou outro produto para ganhar peso ou massa muscular sem acompanhamento médico?',
            'questao_146': '146. O que você achou deste questionário?',
        }


class ExameForm(forms.ModelForm):
    
    class Meta:
        model = Exame
        fields = '__all__'


class DiretorForm(forms.ModelForm):
    
    class Meta:
        model = Diretor
        fields = '__all__'
