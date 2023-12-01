from django.db.models import Model, BooleanField, CharField, TextField, URLField, IntegerField, DateTimeField

# Create your models here.
class Carros(Model):
    """Docstring"""
    data_de_criacao = DateTimeField(auto_now_add=True,verbose_name='data de criação')
    nome = CharField(max_length=200, verbose_name='nome do carro')
    modelo = CharField(max_length=200, verbose_name='modelo do carro', null=True,  blank=True)
    detalhes = TextField(verbose_name='detalhes', null=True,  blank=True)
    em_uso = BooleanField(default=False, verbose_name='em uso', null=True,  blank=True)
    
    class Meta:
        """Docstring"""
        verbose_name_plural = 'Carros'
        verbose_name = 'Carro'
        ordering = ['nome']