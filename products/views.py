from django.shortcuts import render
from .form import ProdutForm
# Create your views here.

def cadastra_produtos(request):
	context={'form': ProdutForm()}
	return render(request,'products/cadastrar.html',context)