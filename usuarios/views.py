from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('productos:lista_zapatillas')  # Redirigir al usuario a la página de productos después de iniciar sesión
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('productos:lista_zapatillas')  # Redirigir al usuario a la página de productos después de registrarse
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registro.html', {'form_registro': form})
