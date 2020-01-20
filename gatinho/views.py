from django.shortcuts import render, redirect

# Create your views here.
from gatinho.forms import GatinhoForm
from gatinho.models import Gatinho, Anuncio
from rest_framework import viewsets
from gatinho.serializers import GatinhoSerializer, AnuncioSerializer



class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Gatinho.objects.all() # ele ta trazer todas as informaçoes do banco de dados
    serializer_class = GatinhoSerializer  # 

class PropagandaViewSet(viewsets.ModelViewSet):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer    





def home(request):
    form = GatinhoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/', kwargs={'msg':'Cadastrado com sucesso'})

    gatinhos = reversed(Gatinho.objects.filter().all())

    args = {
        'gatinhos': gatinhos,
        'form':form
    }

    return render(request, 'index.html', args)

def detail(request, id):
    gatinho = Gatinho.objects.get(id=id)
    donos = gatinho.dono.all()
    args = {
        'donos':donos,
        'gatinho':gatinho
    }
    return render(request, 'detail.html', args)

def delete(request, id):
    gatinho = Gatinho.objects.get(id=id)

    args = {
        'gatinho': gatinho
    }

    gatinho.delete()
    return render(request, 'delete.html', args)

def update(request, id):
    gatinho = Gatinho.objects.get(id=id)
    form = GatinhoForm(request.POST or None, instance=gatinho)

    if form.is_valid():
        form.save()
        return redirect(f'../detail/{gatinho.id}')

    args = {
        'gatinho':gatinho,
        'form':form
    }
    return render(request, 'update.html', args)