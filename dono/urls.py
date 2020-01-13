from django.urls import path
from dono.views import cadastro,deleta,detalhe,updat

urlpatterns = [
    path('cadastro/', cadastro),
]

