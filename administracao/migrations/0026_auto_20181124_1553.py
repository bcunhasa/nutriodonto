# Generated by Django 2.1.3 on 2018-11-24 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0025_auto_20181121_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diretor',
            name='questao_1',
            field=models.CharField(blank=True, choices=[('0', 'Manhã'), ('1', 'Intermediário'), ('2', 'Tarde'), ('3', 'Noite')], max_length=2, null=True, verbose_name='1. A escola funciona em quais turnos? (múltipla resposta)'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_10',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não está em condições de uso'), ('2', 'Não tem sala de recursos de mídia/comunicação')], max_length=2, null=True, verbose_name='10. A escola tem sala de recursos de mídia/comunicação EM CONDIÇÕES DE USO? (Exemplos: televisão, videocassete, dvd, projetor etc)'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_11',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='11. A escola tem conselho escolar?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_12',
            field=models.CharField(blank=True, choices=[('0', 'Não se reúne com frequência'), ('1', '1 a 3 vezes por ano'), ('2', '4 a 6 vezes por ano'), ('3', '7 a 9 vezes por ano'), ('4', '10 a 12 vezes por ano'), ('5', 'Mais de 12 vezes por ano')], max_length=2, null=True, verbose_name='12. Com que frequência o conselho escolar se reúne?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_13',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='13. A escola fica aberta nos finais de semana para uso da comunidade?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_14',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='14. As ações desenvolvidas na escola, no final de semana, são pactuadas com a comunidade?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_15',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não está em condições de uso'), ('2', 'Não tem quadra de esportes')], max_length=2, null=True, verbose_name='15. A escola tem quadra de esportes EM CONDIÇÕES DE USO?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_16',
            field=models.CharField(blank=True, choices=[('0', '1'), ('1', '2'), ('2', '3 ou mais')], max_length=2, null=True, verbose_name='16. Quantas quadras de esporte EM CONDIÇÕES DE USO a escola tem?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_17',
            field=models.CharField(blank=True, choices=[('0', 'Nenhuma'), ('1', '1'), ('2', '2'), ('3', '3 ou mais'), ('4', 'Todas')], max_length=2, null=True, verbose_name='17. Quantas das quadras de esporte EM CONDIÇÕES DE USO da escola são cobertas?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_18',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não está em condições de uso'), ('2', 'Não tem pista de atletismo')], max_length=2, null=True, verbose_name='18. A escola tem pista para corrida/atletismo EM CONDIÇÕES DE USO?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_19',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não está em condições de uso'), ('2', 'Não tem piscina')], max_length=2, null=True, verbose_name='19. A escola tem piscina EM CONDIÇÕES DE USO?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_2',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='2. A escola funciona em regime integral?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_20',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não é utilizado para prática regular de atividade física com instrutor'), ('2', 'Não tem pátio')], max_length=2, null=True, verbose_name='20. O pátio da escola é utilizado para prática regular de atividade física com instrutor?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_21',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não está em condições de uso'), ('2', 'Não tem material esportivo para jogos e brincadeiras')], max_length=2, null=True, verbose_name='21. A escola tem material esportivo ou para jogos e brincadeiras EM CONDIÇÕES DE USO?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_22',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não está em condições de uso'), ('2', 'Não tem vestiário')], max_length=2, null=True, verbose_name='22. A escola tem vestiário EM CONDIÇÕES DE USO para os alunos?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_23',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não estão em condições de uso'), ('2', 'Não tem vestiários separados')], max_length=2, null=True, verbose_name='23. A escola tem vestiários separados para alunos e alunas EM CONDIÇÕES DE USO?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_24',
            field=models.CharField(blank=True, choices=[('0', 'Sim, gratuito'), ('1', 'Sim, pago'), ('2', 'Sim, pago e gratuito'), ('3', 'Não')], max_length=2, null=True, verbose_name='24. A escola oferece atividades esportivas para os alunos fora do horário regular de aula?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_25',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='25. A escola participa de jogos entre escolas?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_26',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='26. A escola realiza jogos entre as classes, turmas ou turnos?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_27',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='27. A escola possui alunos com deficiência ou com transtorno global do desenvolvimento?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_28',
            field=models.CharField(blank=True, choices=[('0', 'Deficiência intelectual'), ('1', 'Transtornos do espectro do autismo'), ('2', 'Transtornos mentais e de comportamento'), ('3', 'Deficiência física'), ('4', 'Deficiência auditiva'), ('5', 'Deficiência visual'), ('6', 'Deficiência múltipla (2 ou mais deficiências simultâneas)'), ('7', 'Outros')], max_length=2, null=True, verbose_name='28. Qual(is) tipo(s) de deficiência? (múltipla resposta)'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_29',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='29. A escola oferece atividade física adaptada para alunos com deficiência?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_3',
            field=models.CharField(blank=True, choices=[('0', 'Educação Infantil (creche, pré-escola)'), ('1', 'Ensino Fundamental (8 anos, 9 anos)'), ('2', 'Ensino Médio (médio, integrado, normal/magistério, educação profissional)'), ('3', 'Educação de Jovens e Adultos (fundamental, projovem urbano, médio)')], max_length=2, null=True, verbose_name='3. A escola atende a quais etapas de ensino? (múltipla resposta)'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_30',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='30. A escola possui estrutura para assegurar a acessibilidade dos alunos com necessidades especiais?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_31',
            field=models.CharField(blank=True, choices=[('0', 'Rampas de acesso'), ('1', 'Interior adequado para locomoção'), ('2', 'Móveis adequados para alunos com necessidades especiais'), ('3', 'Sanitário adequado para alunos com necessidades especiais')], max_length=2, null=True, verbose_name='31. Quais estruturas existem na escola para assegurar a acessibilidade dos alunos com necessidades especiais? (múltipla resposta)'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_32',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='32. A escola oferece comida (merenda escolar / almoço) para os estudantes?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_33',
            field=models.CharField(blank=True, choices=[('0', 'Manhã'), ('1', 'Intermediário'), ('2', 'Tarde'), ('3', 'Noite'), ('4', 'Integral'), ('5', 'Internato'), ('6', 'Educação Infantil'), ('7', '1o a 5o ano do Ensino Fundamental'), ('8', '6o a 9o ano do Ensino Fundamental'), ('9', 'Ensino Médio'), ('10', 'Educação de Jovens e Adultos')], max_length=2, null=True, verbose_name='33. A escola oferece comida (merenda escolar / almoço) para alunos de quais turnos e níveis de ensino? (múltipla resposta)'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_34',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não está em condições de uso'), ('2', 'Não tem cozinha')], max_length=2, null=True, verbose_name='34. A escola tem cozinha EM CONDIÇÕES DE USO?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_35',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não está em condições de uso'), ('2', 'Não tem refeitório')], max_length=2, null=True, verbose_name='35. A escola tem refeitório EM CONDIÇÕES DE USO? (espaço exclusivo para servir alimentação)'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_36',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='36. A escola tem cantina?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_37',
            field=models.CharField(blank=True, choices=[('0', 'Refrigerante'), ('1', 'Suco ou refresco natural de frutas'), ('2', 'Bebidas açucaradas (suco artificial, chá gelado, isotônicos, águas com sabor, energéticos, leite de soja etc. Não contar bebida láctea)'), ('3', 'Leite ou bebida a base de leite (excluir leite de soja)'), ('4', 'Salgados fritos (coxinha, pastel, quibe, batata frita etc)'), ('5', 'Salgados assados (pastel, empada, esfirra etc)'), ('6', 'Salgadinhos industrializados vendidos em pacotes, tipo “chips” e outros (incluindo batata frita de pacote)'), ('7', 'Biscoitos ou bolachas salgadas ou doces, balas, confeitos, doces, chocolates, sorvetes, dim-dim, sacolé, chupe-chupe e outros'), ('8', 'Sanduíches (cachorro quente, misto quente, hambúrguer etc)'), ('9', 'Frutas frescas ou salada de frutas')], max_length=2, null=True, verbose_name='37. Que tipos de bebidas e produtos alimentícios são vendidos na cantina? (múltipla resposta)láctea)'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_38',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='38. Existe algum ponto alternativo de venda de produtos alimentícios dentro ou na entrada da escola? (ex: ambulante/carrocinha)'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_39',
            field=models.CharField(blank=True, choices=[('0', 'Refrigerante'), ('1', 'Suco ou refresco natural de frutas'), ('2', 'Bebidas açucaradas (suco artificial, chá gelado, isotônicos, águas com sabor, energéticos, leite de soja etc. Não contar bebida láctea)'), ('3', 'Leite ou bebida a base de leite (excluir leite de soja)'), ('4', 'Salgados fritos (coxinha, pastel, quibe, batata frita etc)'), ('5', 'Salgados assados (pastel, empada, esfirra etc)'), ('6', 'Salgadinhos industrializados vendidos em pacotes, tipo “chips” e outros (incluindo batata frita de pacote)'), ('7', 'Biscoitos ou bolachas salgadas ou doces'), ('8', 'Balas, confeitos, doces, chocolates, sorvetes, dim-dim, sacolé, chupe-chupe e outros'), ('9', 'Sanduíches (cachorro quente, misto quente, hambúrguer etc)'), ('10', 'Frutas frescas ou salada de frutas')], max_length=2, null=True, verbose_name='39. Que tipos de bebidas e produtos alimentícios são vendidos no ponto alternativo de vendas? (múltipla resposta)láctea)'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_4',
            field=models.CharField(blank=True, choices=[('0', 'Até 50 alunos'), ('1', 'De 51 a 100 alunos'), ('2', 'De 101 a 200 alunos'), ('3', 'De 201 a 500 alunos'), ('4', 'De 501 a 1.000 alunos'), ('5', 'Mais de 1.000 alunos')], max_length=2, null=True, verbose_name='4. Qual é o TOTAL de alunos matriculados?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_40',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='40. A escola tem horta?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_41',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não'), ('2', 'Não tem água')], max_length=2, null=True, verbose_name='41. A escola tem água potável (adequada para beber) para uso dos alunos?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_42',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não'), ('2', 'Não sabe')], max_length=2, null=True, verbose_name='42. NOS ÚLTIMOS 12 MESES, alguma vez a água da escola foi testada quanto a sua potabilidade (se é adequada para beber)?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_43',
            field=models.CharField(blank=True, choices=[('0', 'Rede de abastecimento de água'), ('1', 'Poço ou nascente'), ('2', 'Água de chuva (cisterna)'), ('3', 'Açude, lago ou rio'), ('4', 'Outra fonte')], max_length=2, null=True, verbose_name='43. Qual é a principal fonte de água potável (adequada para beber) da escola?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_44',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não está em condições de uso'), ('2', 'Não tem banheiro')], max_length=2, null=True, verbose_name='44. A escola tem banheiros EM CONDIÇÕES DE USO?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_45',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não estão em condições de uso'), ('2', 'Não tem banheiros separados')], max_length=2, null=True, verbose_name='45. A escola tem banheiros separados para alunos e alunas EM CONDIÇÕES DE USO?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_46',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='46. A escola oferece papel higiênico para uso nos banheiros da escola?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_47',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não está em condições de uso'), ('2', 'Não tem pia ou lavatório')], max_length=2, null=True, verbose_name='47. A escola tem pia ou lavatório EM CONDIÇÕES DE USO onde os estudantes possam lavar as mãos depois de ir ao banheiro e/ou antes das refeições?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_48',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='48. A escola oferece sabão para que os alunos lavem as mãos após usar o banheiro e/ou antes das refeições?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_49',
            field=models.CharField(blank=True, choices=[('0', 'Nenhum dia por semana'), ('1', '1 a 2 dias por semana'), ('2', '3 a 4 dias por semana'), ('3', '5 a 6 dias por semana'), ('4', 'Todos os dias da semana')], max_length=2, null=True, verbose_name='49. Normalmente, com que frequência a remoção do lixo é feita pela escola?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_5',
            field=models.CharField(blank=True, choices=[('0', 'Até 10 salas'), ('1', 'De 11 a 20 salas'), ('2', 'De 21 a 30 salas'), ('3', 'De 31 a 40 salas'), ('4', 'De 41 a 50 salas'), ('5', 'Mais de 50 salas')], max_length=2, null=True, verbose_name='5. Qual é a quantidade TOTAL de salas de aula da escola?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_50',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='50. A escola tem escovódromo?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_51',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não (pular para a questão X)')], max_length=2, null=True, verbose_name='51. A escola realiza alguma Ação de Saúde Bucal?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_52',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='52. Escovação dental supervisionada'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_53',
            field=models.CharField(blank=True, choices=[('0', 'Todos os dias letivos'), ('1', 'Uma vez por semana'), ('2', 'Duas vezes por semana'), ('3', 'Três ou mais vezes por semana'), ('4', 'Uma vez por mês'), ('5', 'Duas vezes por mês'), ('6', 'Uma vez a cada dois meses'), ('7', 'Uma vez a cada três meses'), ('8', 'Uma vez por semestre'), ('9', 'Uma vez por ano')], max_length=2, null=True, verbose_name='53. Caso positivo, com qual frequência?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_54',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='54. Aplicação Tópica de Flúor'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_55',
            field=models.CharField(blank=True, choices=[('0', 'Todos os dias letivos'), ('1', 'Uma vez por semana'), ('2', 'Duas vezes por semana'), ('3', 'Três ou mais vezes por semana'), ('4', 'Uma vez por mês'), ('5', 'Duas vezes por mês'), ('6', 'Uma vez a cada dois meses'), ('7', 'Uma vez a cada três meses'), ('8', 'Uma vez por semestre'), ('9', 'Uma vez por ano')], max_length=2, null=True, verbose_name='55. Caso positivo, com qual frequência?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_56',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='56. Bochechos fluorados'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_57',
            field=models.CharField(blank=True, choices=[('0', 'Todos os dias letivos'), ('1', 'Uma vez por semana'), ('2', 'Duas vezes por semana'), ('3', 'Três ou mais vezes por semana'), ('4', 'Uma vez por mês'), ('5', 'Duas vezes por mês'), ('6', 'Uma vez a cada dois meses'), ('7', 'Uma vez a cada três meses'), ('8', 'Uma vez por semestre'), ('9', 'Uma vez por ano')], max_length=2, null=True, verbose_name='57. Caso positivo, com qual frequência?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_58',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='58. A escola realiza ação de Educação em Saúde Bucal?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_59',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='59. Estas ações estão incluídas no currículo escolar?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_6',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não está em condições de uso'), ('2', 'Não tem biblioteca')], max_length=2, null=True, verbose_name='6. A escola tem biblioteca EM CONDIÇÕES DE USO?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_60',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='60. Sua escola já realizou Levantamento Epidemiológico sobre cárie dentária?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_61',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='61. Caso positivo você conhece (eu) os resultados?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_62',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='62. Sua escola disponibiliza escovas dentais para os estudantes?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_63',
            field=models.CharField(blank=True, choices=[('0', 'Mensalmente'), ('1', 'Bimestralmente'), ('2', 'Trimestralmente'), ('3', 'Uma vez por ano')], max_length=2, null=True, verbose_name='63. Caso positivo, com qual frequência?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_64',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='64. Sua escola disponibiliza creme dental para os estudantes?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_65',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='65. Sua escola disponibiliza fio dental para os estudantes?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_66',
            field=models.CharField(blank=True, choices=[('0', 'Nenhuma vez'), ('1', 'Raramente'), ('2', 'Às vezes'), ('3', 'Na maior parte do tempo'), ('4', 'Em todo período')], max_length=2, null=True, verbose_name='66. NOS ÚLTIMOS 12 MESES, com que frequência, a localidade onde a escola está situada foi considerada área de risco em termos de violência (roubos, furtos, assaltos, troca de tiros, consumo de drogas, homicídios etc)?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_67',
            field=models.CharField(blank=True, choices=[('0', 'Nenhuma vez'), ('1', '1 vez'), ('2', '2 a 4 vezes'), ('3', '5 ou mais vezes')], max_length=2, null=True, verbose_name='67. NOS ÚLTIMOS 12 MESES, a escola teve que suspender ou interromper suas aulas por motivo de segurança em termos de violência?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_68',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='68. A escola tem algum grupo ou comitê responsável por orientar ou coordenar ações e/ou atividades relacionadas à saúde?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_69',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='69. A escola aderiu ao Programa Saúde da Escola (PSE)?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_7',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não está em condições de uso'), ('2', 'Não tem sala ou laboratório de informática')], max_length=2, null=True, verbose_name='7. A escola tem sala ou laboratório de informática EM CONDIÇÕES DE USO para os alunos?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_70',
            field=models.CharField(blank=True, choices=[('0', '2013'), ('1', '2014'), ('2', '2015'), ('3', '2016'), ('4', '2017'), ('5', '2018'), ('6', 'Não sei.')], max_length=2, null=True, verbose_name='70. Caso positivo, qual o ano da adesão da escola ao Programa Saúde na Escola (PSE)?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_71',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='71. A escola implementa ações do Programa Saúde da Escola (PSE)?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_72',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='72. A escola implementa ações do Programa Mais Educação?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_73',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='73. A escola realiza ações conjuntas com Unidade Básica de Saúde ou Equipe de Saúde da Família ou Equipe de Atenção Básica?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_74',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='74. A escola mantém registros sobre a caderneta de vacinação dos escolares?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_75',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='75. A escola mantém outros registros sobre a saúde dos escolares? (histórico clínico,ocorrência de alergias, acidentes, tipo sanguíneo, doenças etc)'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_76',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='76. A escola tem material e/ou medicamentos de Primeiros Socorros mantidos em local adequado?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_77',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='77. A escola tem conhecimento de consumo de cigarro por professores nas suas dependências?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_78',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='78. A escola tem conhecimento de consumo de cigarro por alunos nas suas dependências?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_79',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='79. A escola tem alguma política, norma ou regra escrita que proíba o uso do tabaco nas suas dependências?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_8',
            field=models.CharField(blank=True, choices=[('0', 'Não existem computadores em condições de uso para os alunos'), ('1', 'Até 10 computadores'), ('2', 'De 11 a 20 computadores'), ('3', 'De 21 a 30 computadores'), ('4', 'De 31 a 40 computadores'), ('5', 'De 41 a 50 computadores'), ('6', 'Mais de 50 computadores')], max_length=2, null=True, verbose_name='8. Quantos computadores (desktops, laptops, notebooks, netbooks, tablets) da escola EM CONDIÇÕES DE USO estão disponíveis para os alunos em sala de aula e/ou salas específicas de informática?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_80',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='80. A escola tem alguma política, norma ou regra escrita que proíba o uso de drogas ilícitas nas suas dependências?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_81',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='81. A escola tem alguma política, norma ou regra escrita que proíba bullying nas suas dependências?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_82',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='82. A escola tem alguma política, norma ou regra escrita que proíba brigas nas suas dependências?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_83',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='83. A escola tem alguma política, norma ou regra escrita que proíba punição física dos estudantes pelos professores ou funcionários nas suas dependências?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_84',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='84. A escola está situada em área de vulnerabilidade social?'),
        ),
        migrations.AlterField(
            model_name='diretor',
            name='questao_9',
            field=models.CharField(blank=True, choices=[('0', 'Sim'), ('1', 'Não')], max_length=2, null=True, verbose_name='9. Os alunos têm acesso à internet através de equipamentos da escola?'),
        ),
    ]