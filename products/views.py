from django.shortcuts import render
from .form import ProdutForm
# Create your views here.

def cadastra_produtos(request):
	 if request.method == 'POST':
          produt = ProdutForm(request.POST, request.FILES)
          print(produt.errors)
          if produt.is_valid():
             produt.save()
            

	 context={'form': ProdutForm()}
	 return render(request,'products/cadastrar.html',context)