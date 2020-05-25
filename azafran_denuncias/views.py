from django.shortcuts import render, redirect
from .forms import DenunciaForm

# Create your views here.

# Testing
def testing(request):
    return render(request, 'azafran_denuncias/index.html')

# Página de inicio
def inicio(request):
    return render(request, 'azafran_denuncias/index.html')

# Página de protocolos
def protocolos(request):
    return render(request, 'azafran_denuncias/protocolos.html')

# Página de testimonios
def denuncias_list(request):
    return render(request, 'azafran_denuncias/testimonios.html')

# Formulario para crear denuncias
def denuncias_form(request):
    if request.method == 'GET':
        form = DenunciaForm()
        return render(request, 'azafran_denuncias/alza_la_voz.html', {'form': form})
    else:
        form = DenunciaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/denuncias')

# Eliminar un denuncia
def denuncia_delete(request):
    return
