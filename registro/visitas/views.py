from django.shortcuts import render, redirect
from django.utils.timezone import now
from .models import Visita
from .forms import VisitaForm

def registrar_visita(request):
    if request.method == 'POST':
        form = VisitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_visitas')
    else:
        form = VisitaForm()
    return render(request, 'visitas/registrar.html', {'form': form})

def listar_visitas(request):
    visitas = Visita.objects.filter(hora_entrada__date=now().date())
    return render(request, 'visitas/listar.html', {'visitas': visitas})
