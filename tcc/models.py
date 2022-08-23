from django.contrib.postgres.fields import ArrayField
from django.db import models

class Autor(models.Model):

    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=150)
    foto = models.ImageField(upload_to='fotos/')

    def __str__(self):
        return self.nome

class Orientador(models.Model):
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=150)
    linkcurriculo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Curso(models.Model):

    MODALIDADE = [
        ('B', 'Bacharelado'),
        ('L', 'Licenciatura'),
        ('T', 'Tecnológico'),
    ]

    nome = models.CharField(max_length=50)
    modalidade = models.CharField(max_length=1, choices=MODALIDADE, null=True)


    def __str__(self):
        return self.nome

class  TCC(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    orientador = models.CharField(max_length=50)
    curso = models.CharField(max_length=50)
    anodoc = models.DateField(verbose_name="Ano do documento")
    resumo = models.TextField()
    arquivo= models.FileField(upload_to= 'uploads/')
    palavraschave = ArrayField(models.CharField(max_length=50), blank=True)

    def __str__(self):
        return self.titulo