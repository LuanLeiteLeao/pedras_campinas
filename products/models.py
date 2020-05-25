from django.db import models
from .constantes import CATEGORIAS,COR
# Create your models here.
class Produto(models.Model):
	nome = models.CharField('Nome Do Produto',max_length=200)
	preco = models.DecimalField('Preço em R$', max_digits=100, decimal_places=2)
	categoria = models.CharField(max_length=1, null=True, verbose_name='Categoria',
                              choices=(
                                 	CATEGORIAS

                              )
                              )
	cor = models.CharField(max_length=1, null=True, verbose_name='Cor',
                          choices=(
                             	COR

                          )
                          )
	tamanho_em_cm =	models.DecimalField('Tamanho em cm', max_digits=100, decimal_places=2)
	imagem = models.ImageField('Imagem do Produto', upload_to='mangueiras/imagens/')