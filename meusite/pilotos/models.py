from django.db.models import Model, BooleanField, CharField, TextField, DateTimeField, DateField
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Pilotos(Model):
    """Docstring"""
    data_de_criacao = DateTimeField(auto_now_add=True,verbose_name='data de criação')
    nome = CharField(max_length=200, verbose_name='nome do piloto')
    nacionalidade = CharField(max_length=200, verbose_name='nacionalidade', null=True,  blank=True)
    data_de_nascimento = DateField(verbose_name='data de nascimento', null=True,  blank=True)
    detalhes = TextField(verbose_name='detalhes', null=True,  blank=True)
    ativo = BooleanField(default=True, verbose_name='ativo')
    carro = ForeignKey('carros.Carros', on_delete=CASCADE, verbose_name='carro', null=True, blank=True)

    class Meta:
        """Docstring"""
        verbose_name_plural = 'Pilotos'
        verbose_name = 'Piloto'
        ordering = ['nome']