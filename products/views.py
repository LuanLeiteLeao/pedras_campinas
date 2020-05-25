from django.shortcuts import render
from .form import ProdutForm
# Create your views here.

def cadastra_produtos(request):
	 if request.method == 'POST':
          form_produt = ProdutForm(request.POST)
          if form_user.is_valid():
             post.save()
            

	 context={'form': ProdutForm()}
	 return render(request,'products/cadastrar.html',context)