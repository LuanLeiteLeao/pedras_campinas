from django.shortcuts import render,redirect
from .form import ProdutForm
from .models import Produto,Compra
from rest_framework.generics import get_object_or_404
from users import utils
from datetime import datetime


# Create your views here.

def cadastra_produtos(request):
    context = {}

    if request.method == 'POST':
        produt = ProdutForm(request.POST, request.FILES)
        print(produt.errors)
        if produt.is_valid():
            produt.save()
        sucess = ['Produto Cadastrado Com Sucesso']
        context.update({'sucess': sucess})

    context.update({'form': ProdutForm()})
    return render(request, 'products/cadastrar.html', context)


def gerenciar(request):

    produtos = Produto.objects.all()
    context = {'produtos':produtos}

    return render(request, 'products/gerenciar_produto.html',context)

def excluir(request,pk):
    user = utils.obter_usuario_logado(request)
    if user.is_gerente:
        prod_excuir = Produto.objects.get(id = pk)
        prod_excuir.delete()

    return redirect('gerenciar_produtos')

def editar(request,pk):
    user = utils.obter_usuario_logado(request)
    prod_edit = Produto.objects.get(id = pk)
    if user.is_gerente:
        if request.method == 'POST':
            form = ProdutForm(request.POST, instance=prod_edit)
            if form.is_valid:
                prod_edit = form.save()
                return redirect('gerenciar_produtos')




    form = ProdutForm(instance=prod_edit)

    return render(request,'products/cadastrar.html',{'form':form})

def comprar(request,pk):
    user = utils.obter_usuario_logado(request)
    produto =  Produto.objects.get(id = pk)
    data = datetime.now().strftime("%m/%d/%Y")

    context = {'produto':produto,'nome_user':user.nome, 'data':data}

    return render(request,'products/comprar.html',context)

def confirmar_comprar(request,pk):
    user = utils.obter_usuario_logado(request)
    produto =  Produto.objects.get(id = pk)
    comp=Compra( produto = produto,usuario= user)
    comp.save()
    return redirect('home')