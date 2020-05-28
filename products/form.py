from django import forms
from .models import Produto

class ProdutForm(forms.ModelForm):
	class Meta:
		model = Produto
		fields = ['nome','categoria','cor','tamanho_em_cm','preco','imagem']

		