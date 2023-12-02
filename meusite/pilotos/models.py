from django.db.models import Model, BooleanField, CharField, TextField, URLField, IntegerField, DateTimeField, DateField

# Create your models here.
class Pilotos(Model):
    """Docstring"""
    data_de_criacao = DateTimeField(auto_now_add=True,verbose_name='data de criação')
    nome = CharField(max_length=200, verbose_name='nome da equipe')
    nacionalidade = CharField(max_length=200, verbose_name='nacionalidade')
    data_de_nascimento = DateField(verbose_name='data de nascimento')
    detalhes = TextField(verbose_name='detalhes', null=True,  blank=True)
    ativo = BooleanField(default=False, verbose_name='ativo', null=True,  blank=True)
    
    class Meta:
        """Docstring"""
        verbose_name_plural = 'Pilotos'
        verbose_name = 'Piloto'
        ordering = ['nome']