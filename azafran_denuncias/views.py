from django.shortcuts import render

# Create your views here.

# Testing
def testing(request):
    return render(request, 'azafran_denuncias/index.html')

# Página de inicio
def inicio(request):
    return render(request, 'azafran_denuncias/index.html')
    
# Lista de denuncias actuales
def denuncias_list(request):
    return render(request, 'azafran_denuncias/testimonios.html')

# Formulario para crear denuncias
def denuncias_form(request):
    return

# Eliminar un denuncia
def denuncia_delete(request):
    return