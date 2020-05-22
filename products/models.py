from django.db import models

# Create your models here.
class Produto(models.Model):
	nome = models.CharField('Nome',max_length=200)
	preco = models.DecimalField('Preço', max_digits=100, decimal_places=2)
	imagem = models.ImageField('Imagem do Produto', upload_to='mangueiras/imagens/')