from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now
from django.contrib import messages
from .models import Visita
from .forms import VisitaForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Página inicio
def inicio(request):
    return render(request, 'visitas/inicio.html')

# Registrar una nueva visita
def registrar_visita(request):
    if request.method == 'POST':
        form = VisitaForm(request.POST) #Si se envió formulario
        if form.is_valid():
            visita = form.save(commit=False) # No guardes en la BD todavía
            if request.user.is_authenticated: # Revisa si el usuario está conectado
                visita.registrado_por = request.user # Asigna el usuario actual
            visita.save() #guarda en la BD
            messages.success(request, "Visita registrada correctamente.")
            return redirect('visitas:listar_visitas') #Redirige a lista
    else:
        form = VisitaForm()
    return render(request, 'visitas/registrar.html', {'form': form})

#Listar visitas
def listar_visitas(request):
    fecha = request.GET.get('fecha') # Filtrar por fecha
    if fecha:
        visitas_list = Visita.objects.filter(fecha=fecha).order_by('-hora_entrada')
    else:
        visitas_list = Visita.objects.all().order_by('-hora_entrada')

    paginator = Paginator(visitas_list, 10) #Paginator con esta lista, mostrando 10 por pagina
    page_number = request.GET.get('page') #Vemos que numero de pagina nos piden en la url
    visitas_page = paginator.get_page(page_number) #Solo las visitas de ESA pagina

    return render(request, 'visitas/listar.html',{
        'visitas': visitas_page, #pasamos el objeto de la pagina
        'fecha': fecha
    })

# Marcar salida de una visita
def marcar_salida(request, pk):
    visita = get_object_or_404(Visita, pk=pk)
    if visita.hora_salida is None: # Solo marcar si no tiene salida registrada
        visita.hora_salida = now()
        visita.save()
        messages.success(request, f"Salida marcada para {visita.nombre}.")
    return redirect('visitas:listar_visitas')

# Eliminar una visita
def eliminar_visita(request, pk):
    visita = get_object_or_404(Visita, pk=pk)
    visita.delete()
    messages.success(request, f"Visita de {visita.nombre} eliminada correctamente.")
    return redirect('visitas:listar_visitas')

def editar_visita(request, pk):
    # busca la visita específica por su ID (pk) o muestra error 404
    visita = get_object_or_404(Visita, pk=pk)

    # Revisa si el usuario está enviando el formulario con cambios
    if request.method == 'POST':
        # Carga el formulario con los datos nuevos (request.POST)
        # sobre la visita que ya existía (instance=visita)
        form = VisitaForm(request.POST, instance=visita)
        if form.is_valid():
            form.save() # Guarda los cambios en la base de datos
            messages.success(request, f"Visita de {visita.nombre} actualizada correctamente.")
            return redirect('visitas:listar_visitas')

    # Si no es POST, solo está cargando la página por primera vez
    else:
        # Muestra el formulario relleno con los datos de esa visita
        form = VisitaForm(instance=visita)

    # Muestra la plantilla HTML
    return render(request, 'visitas/editar.html', {
        'form': form,
        'visita': visita # Le pasamos la visita para mostrar el título
    })