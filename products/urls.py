from django.urls import path, include
from . import views

urlpatterns = [

    path('cadastrar/', views.cadastra_produtos, name='cadastrar_produtos'),
    path('gerenciar_produtos/', views.gerenciar, name='gerenciar_produtos'),
    path('excluir_produto/<pk>', views.excluir, name='excluir_produto'),
    path('editar_produto/<pk>', views.editar, name='editar_produto'),
    path('comprar_produto/<pk>', views.comprar, name='comprar_produto'),
    path('confirmar_comprar/<pk>', views.confirmar_comprar, name='confirmar_comprar'),
]
