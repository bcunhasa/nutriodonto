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
            'questao_73': '73. Have you ever smoked a cigarette, even one or two puffs?',
            'questao_74': '74. How old were you when you first tried cigarette smoking?',
            'questao_75': '75. In the last 30 days, how many days have you smoked cigarettes?',
            'questao_76': '76. In the last 30 days, in general, how did you get your own cigarettes?',
            'questao_77': '77. In the last 30 days, has anyone refused to sell you cigarettes because of your age?',
            'questao_78': '78. In the past 30 days, how many days have you used other tobacco products: straw or hand-rolled cigarettes, cigar, pipe, cigarillo, Indian or bali cigarette, hookah, snuff, chewing tobacco, etc.? (not include regular cigarette)',
            'questao_79': '79. Which other tobacco product have you used most often in the last 30 days?',
            'questao_80': '80. In the last 7 days, how many days did people smoke in your presence?',
            'questao_81': '81. Do any of your parents or guardians smoke?',
            'questao_82': '82. Have you ever had a shot of alcohol (a shot is like a can of beer or a glass of wine or a shot of rum or whiskey, etc.)?',
            'questao_83': '83. How old were you when you had your first shot of alcohol (one shot is like a can of beer or a glass of wine or a shot of rum or whiskey, etc.)?',
            'questao_84': '84. Over the past 30 days, how many days have you had at least one glass or one shot of alcohol (one shot equals one can of beer or one glass of wine or one shot of rum or whiskey, etc.)?',
            'questao_85': '85. In the last 30 days, on the days you had a drink, how many glasses or drinks did you have a day?',
            'questao_86': '86. Over the past 30 days, most of the time, how did you get the drink you had?',
            'questao_87': '87. How many times in your life did you drink so much that you were really drunk?',
            'questao_88': '88. How many times in your life have you had problems with family or friends, missed classes, or fought over drinking?',
            'questao_89': '89. How many of your friends drink alcohol?',
            'questao_90': '90. Have you ever used drugs like marijuana, cocaine, crack, glue, loló, perfume thrower, ecstasy, oxy etc.?',
            'questao_91': '91. How old were you when you used a drug like marijuana, cocaine, crack, cola, loló, scent launcher, ecstasy, oxy or another for the first time?',
            'questao_92': '92. In the last 30 days, how many days have you used drugs like marijuana, cocaine, crack, glue, loló, perfume thrower, ecstasy, oxy etc.?',
            'questao_93': '93. In the last 30 days, how many days have you used cannabis?',
            'questao_94': '94. In the last 30 days, how many days have you used crack?',
            'questao_95': '95. How many of your friends use drugs?',
            'questao_96': '96. Over the past 30 days, how many days have you missed classes or school without permission from your parents or guardians?',
            'questao_97': '97. In the last 30 days, how often did your parents or guardians really know what you were doing in your free time?',
            'questao_98': '98. In the last 30 days, how often have your parents or guardians checked that your homework (homework) has been done?',
            'questao_99': '99. In the last 30 days, how often have your parents or guardians understood your issues and concerns?',
            'questao_100': '100. Over the past 30 days, how often have your parents or guardians moved your things without your agreement?',
            'questao_101': '101. Over the past 30 days, how often have your classmates treated you well and / or been helpful to you?',
            'questao_102': '102. Over the past 30 days, how often have any of your schoolmates scolded, mocked, mocked, intimidated, or mocked you so much that you were hurt, bothered, upset, offended, or humiliated?',
            'questao_103': '103. In the last 30 days, why or why have your colleagues been cheating, mocking, mocking, mocking, intimidating or humiliating you?',
            'questao_104': '104. Over the past 30 days, have you sculpted, mocked, made a mockery, intimidated or mocked any of your schoolmates so much that he was hurt, upset, offended or humiliated?',
            'questao_105': '105. Have you ever been bullied?',
            'questao_106': '106. In the last 12 months, how often have you been unable to sleep at night because something worried you so much?',
            'questao_107': '107. How many close friends do you have?',
            'questao_108': '108. In the last 30 days, how often have you washed your hands before eating?',
            'questao_109': '109. In the last 30 days, how often have you washed your hands after using the bathroom or toilet?',
            'questao_110': '110. In the last 30 days, how often did you use soap or soap when you washed your hands?',
            'questao_111': '111. In the last 30 days, how many times a day have you usually brushed your teeth?',
            'questao_112': '112. In the last 06 months, have you had a toothache? (Not worth that toothache caused by braces, ie orthodontic braces.)',
            'questao_113': '113. In the last 12 months, how many times have you been to the dentist?',
            'questao_114': '114. In the past 30 days, how many days have you dropped out of school because you didn\'t feel safe on the way home from school or from school to home?',
            'questao_115': '115. In the last 30 days, how many days did you not go to school because you did not feel safe at school?',
            'questao_116': '116. Over the past 30 days, how often have you been wearing a seat belt while riding a passenger in the front seat of a car / car, van or taxi?',
            'questao_117': '117. In the last 30 days, how often have you worn a helmet when riding a motorcycle?',
            'questao_118': '118. In the last 30 days, how many times have you driven a motorized transport vehicle? (car, motorcycle, boat, boat, etc.)',
            'questao_119': '119. In the last 30 days, how many times have you ridden in a car or other motor vehicle driven by someone who had consumed an alcoholic beverage?',
            'questao_120': '120. In the last 30 days, how many times have you been physically assaulted by an adult in your family?',
            'questao_121': '121. In the last 30 days, have you been involved in a fight where someone used a gun, such as a revolver or shotgun?',
            'questao_122': '122. Have you been involved in a fight in the last 30 days in which someone used any other weapon such as a knife, pocketknife, fishmonger, stone, stick or bottle?',
            'questao_123': '123. In the last 12 months, how many times have you been physically assaulted?',
            'questao_124': '124. In the last 12 months, how many times have you been involved in fights?',
            'questao_125': '125. In the last 12 months, how many times have you been seriously injuried in a fight?',
            'questao_126': '126. In the last 12 months, what was the most serious injury or injury to you?',
            'questao_127': '127. In the last 12 months, what was the main cause of the injury or the most serious injury to you?',
            'questao_128': '128. In the last 12 months, have you had a bicycle accident (crashed and injured)?',
            'questao_129': '129. Have you ever been forced to have sex in your life?',
            'questao_130': '130. Who forced you to have sex?',
            'questao_131': '131. How would you rate your state of health?',
            'questao_132': '132. In the last 12 months, how many days did you miss school for a reason (s) related to your health?',
            'questao_133': '133. In the last 12 months have you sought any health services or professionals for health-related care?',
            'questao_134': '134. In the last 12 months, which health service have you sought most often?',
            'questao_135': '135. Have you been seen the last time you went to any Basic Health Unit (Health Center or Post or Family Health Unit / PSF) in the last 12 months?',
            'questao_136': '136. What was the main reason for your search at the Basic Health Unit (Health Center or Post or Family Health Unit / PSF) this last time?',
            'questao_137': '137. 137. Do you know / hear about the HPV vaccination campaign?',
            'questao_138': '138. 138. Have you been vaccinated against the HPV virus?',
            'questao_139': '139. 139. You consider your body image to be something:',
            'questao_140': '140. 140. How do you feel about your body?',
            'questao_141': '141. As for your body, you consider yourself:',
            'questao_142': '142. What are you doing about your weight?',
            'questao_143': '143. In the last 30 days, have you vomited or taken laxatives to lose weight or avoid gaining weight?',
            'questao_144': '144. In the last 30 days, have you taken any medicine, formula or other weight loss product without medical supervision?',
            'questao_145': '145. In the last 30 days, have you taken any medicine, formula or other product to gain weight or muscle mass without medical supervision?',
            'questao_146': '146. What did you think of this questionnaire?',
        }


class ExameForm(forms.ModelForm):
    
    class Meta:
        model = Exame
        fields = '__all__'


class DiretorForm(forms.ModelForm):
    
    class Meta:
        model = Diretor
        fields = '__all__'
