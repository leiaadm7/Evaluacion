from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now
from django.contrib import messages
from .models import Visita
from .forms import VisitaForm

def inicio(request):
    return render(request, 'visitas/inicio.html')

def registrar_visita(request):
    if request.method == 'POST':
        form = VisitaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Visita registrada correctamente.")
            return redirect('visitas:listar_visitas')
    else:
        form = VisitaForm()
    return render(request, 'visitas/registrar.html', {'form': form})

def listar_visitas(request):
    fecha = request.GET.get('fecha')
    if fecha:
        visitas = Visita.objects.filter(fecha=fecha).order_by('-hora_entrada')
    else:
        visitas = Visita.objects.all().order_by('-hora_entrada')
    return render(request, 'visitas/listar.html', {'visitas': visitas, 'fecha': fecha})

def marcar_salida(request, pk):
    visita = get_object_or_404(Visita, pk=pk)
    if visita.hora_salida is None:
        visita.hora_salida = now()
        visita.save()
        messages.success(request, f"Salida marcada para {visita.nombre}.")
    return redirect('visitas:listar_visitas')

def eliminar_visita(request, pk):
    visita = get_object_or_404(Visita, pk=pk)
    visita.delete()
    messages.success(request, f"Visita de {visita.nombre} eliminada correctamente.")
    return redirect('visitas:listar_visitas')
