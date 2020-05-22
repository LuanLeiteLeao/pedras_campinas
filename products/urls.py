from django.urls import path,include
from . import views

urlpatterns = [
	
    path('cadastrar/', views.cadastra_produtos),
]
