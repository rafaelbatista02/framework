from django.shortcuts import render

# Create your views here.
from dono.forms import DonoForm


def cadastro(request):
    form = DonoForm(request.POST or None)
    args = {
        'form':form
    }
    if form.is_valid():
        form.save()
        args['msg'] = 'Cadastro Realizado com sucesso'
    return render(request, 'cadastro.html', args)

def detalhe(request, id):
    dono = Dono.objects.get(id=id)
    donos = dono.gatinho.all()
    args = {
        'donos':donos,
        'dono':dono
    }
    return render(request, 'detail.html', args) 
    
def deleta(request, id):
    dono = Dono.objects.get(id=id)

    args = {
        'dodno': dono
    }

    dono.delete()
    return render(request, 'delete.html', args)       

def updat(request, id):
    dono = Dono.objects.get(id=id)
    form = DonoForm(request.POST or None, instance=dono)

    if form.is_valid():
        form.save()
        return redirect(f'../detail/{dono.id}')

    args = {
        'dono':dono,
        'form':form
    }
    return render(request, 'update.html', args)    