from django.db.models import *


# Create your models here.
class Carros(Model):
    """Docstring"""
    data_de_criacao = DateTimeField(auto_now_add=True,verbose_name='data de criação')
    nome = CharField(max_length=200, verbose_name='nome do carro')
    modelo = CharField(max_length=200, verbose_name='modelo do carro', null=True,  blank=True)
    detalhes = TextField(verbose_name='detalhes', null=True,  blank=True)
    ativo = BooleanField(default=True, verbose_name='ativo')
    equipe = ForeignKey('equipes.Equipes', on_delete=CASCADE, verbose_name='equipe', null=True,  blank=True)

    def __str__(self):
        nome = self.nome if self.nome is not None else ''
        modelo = self.modelo if self.modelo is not None else ''
        return nome + ' ' + modelo


    class Meta:
        """Docstring"""
        verbose_name_plural = 'Carros'
        verbose_name = 'Carro'
        ordering = ['nome']

        permissions = [
            ("can_delete_carro", "Can delete Carro"),
        ]
