from django.db import models
from .constantes import CATEGORIAS, COR
from users.models import User


# Create your models here.
class Produto(models.Model):
    nome = models.CharField('Nome Do Produto', max_length=200)
    preco = models.DecimalField('Preço em R$', max_digits=100, decimal_places=2)
    categoria = models.PositiveIntegerField('Categoria', choices=(CATEGORIAS))
    cor = models.PositiveIntegerField('Cor', choices=(COR))
    tamanho_em_cm = models.DecimalField('Tamanho em cm', null=True, max_digits=100, decimal_places=2)
    imagem = models.ImageField('Imagem do Produto', upload_to='produtos/imagens/')

    def __str__(self):
        return self.nome

# Create your models here.
class Compra(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='Produto')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User')
    def __str__(self):
        return self.produto.nome+'/'+self.usuario.nome
