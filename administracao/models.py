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
    questao1 = models.IntegerField(choices=QUESTAO, verbose_name='1. Qual é a sua cor ou raça?')
    questao2 = models.IntegerField(choices=QUESTAO, verbose_name='2. Qual é a sua idade?')
    questao3 = models.IntegerField(choices=QUESTAO, verbose_name='3. Qual é o mês do seu aniversário?')
    questao4 = models.IntegerField(choices=QUESTAO, verbose_name='4. Em que ano você nasceu?')
    
    # Informações gerais
    questao5 = models.IntegerField(choices=QUESTAO, verbose_name='5. Qual é o seu gênero?')
    questao6 = models.IntegerField(choices=QUESTAO, verbose_name='6. Em que ano/série você está?')
    questao7 = models.ArrayField(models.IntegerField(choices=QUESTAO), default=[], verbose_name='7. Em que turno você estuda? (pode ser múltipla escola).')
    questao8 = models.IntegerField(choices=QUESTAO, verbose_name='8. Você estuda em regime integral (tem atividades escolares por 7 horas ou mais diárias, durante todo o período escolar)?')
    questao9 = models.IntegerField(choices=QUESTAO, verbose_name='9. Você estuda em regime de internato (a escola possui alojamento onde os alunos permanecem e dormem diariamente, durante todo o período escolar)?')
    questao10 = models.IntegerField(choices=QUESTAO, verbose_name='10. Qual o grau de escolaridade mais elevado que você pretende concluir?')
    questao11 = models.IntegerField(choices=QUESTAO, verbose_name='11. Quando terminar o ciclo/curso que você está frequentando atualmente, você pretende?')
    questao12 = models.IntegerField(choices=QUESTAO, verbose_name='12. Você mora com sua mãe?')
    questao13 = models.IntegerField(choices=QUESTAO, verbose_name='13. Você mora com seu pai?')
    questao14 = models.IntegerField(choices=QUESTAO, verbose_name='14. Contando com você, quantas pessoas moram na sua casa ou apartamento?')
    questao15 = models.IntegerField(choices=QUESTAO, verbose_name='15. Na sua casa tem telefone fixo (convencional)?')
    questao16 = models.IntegerField(choices=QUESTAO, verbose_name='16. Você tem celular?')
    questao17 = models.IntegerField(choices=QUESTAO, verbose_name='17. Na sua casa tem computador (de mesa, netbook, laptop etc.)?')
    questao18 = models.IntegerField(choices=QUESTAO, verbose_name='18. Você tem acesso à internet em sua casa?')
    questao19 = models.IntegerField(choices=QUESTAO, verbose_name='19. Alguém que mora na sua casa tem carro?')
    questao20 = models.IntegerField(choices=QUESTAO, verbose_name='20. Alguém que mora na sua casa tem moto?')
    questao21 = models.IntegerField(choices=QUESTAO, verbose_name='21. Quantos banheiros com chuveiro têm dentro da sua casa?')
    questao22 = models.IntegerField(choices=QUESTAO, verbose_name='22. Tem empregado(a) doméstico(a) recebendo dinheiro para fazer o trabalho em sua casa, três ou mais dias por semana?')
    questao23 = models.IntegerField(choices=QUESTAO, verbose_name='23. Qual nível de ensino (grau) sua mãe estudou ou estuda?')
    questao24 = models.IntegerField(choices=QUESTAO, verbose_name='24. Você tem algum trabalho, emprego ou negócio atualmente?')
    questao25 = models.IntegerField(choices=QUESTAO, verbose_name='25. Você recebe dinheiro por este trabalho, emprego ou negócio?')
    questao26 = models.IntegerField(choices=QUESTAO, verbose_name='26. Sua família recebe benefícios do Programa Bolsa Família?')
    
    # Alimentação
    questao27 = models.IntegerField(choices=QUESTAO, verbose_name='27. ')
    
    # Atividade física
    
    # Uso de cigarro
    
    # Bebidas alcoólicas
    
    # Drogas ilícitas
    
    # Situações em casa e na escola
    
    # Higiene e saúde bucal
    
    # Segurança
    
    # Uso de serviço de saúde
    
    # Imagem corporal
    
    # A sua opinião

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
