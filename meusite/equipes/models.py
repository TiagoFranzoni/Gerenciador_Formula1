"""Docstring"""
from django.db.models import Model, BooleanField, CharField, TextField, URLField, IntegerField, DateTimeField

# Create your models here.
class Equipes(Model):
    """Docstring"""
    data_de_criacao = DateTimeField(auto_now_add=True,verbose_name='data de criação')
    nome = CharField(max_length=200, verbose_name='nome da equipe')
    detalhes = TextField(verbose_name='detalhes', null=True,  blank=True)
    fundador = CharField(max_length=200, verbose_name='nome do fundador', null=True,  blank=True)
    administrador = CharField(max_length=200, verbose_name='nome do administrador', null=True,  blank=True)
    ativa = BooleanField(default=False, verbose_name='ativa', null=True,  blank=True)

    def __str__(self):
        return self.nome + ' - ' + self.data_de_criacao.strftime('%d/%m/%Y')
    
    class Meta:
        """Docstring"""
        verbose_name_plural = 'Equipes'
        verbose_name = 'Equipe'
        ordering = ['nome']