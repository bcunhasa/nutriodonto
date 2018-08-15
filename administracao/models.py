from django.db import models


class Aluno(models.Model):
    """Modelo que representa um aluno"""
    nome = models.CharField(max_length=TAMANHO_NOMES, blank=True, null=True, verbose_name='Nome')

    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.nome


class Questionario(models.Model):
    """Modelo que representa um questionário"""
    questao1 = models.CharField(max_length=TAMANHO_NOMES, blank=True, null=True, verbose_name='Nome')

    def __str__(self):
        """Devolve a representação do modelo em string"""
        return self.nome


class Exame(models.Model):
    """Modelo que representa um exame completo"""
    
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
