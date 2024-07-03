from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from carrito.carrito import Carrito 
from productos.models import Zapatilla

def ver_carrito(request):
    carrito = Carrito(request)
    return render(request, 'carrito/ver_carrito.html', {'carrito': carrito})

def agregar_al_carrito(request, zapatilla_id):
    carrito = Carrito(request)
    zapatilla = get_object_or_404(Zapatilla, id=zapatilla_id)
    carrito.add(zapatilla=zapatilla)
    return redirect('ver_carrito', id=zapatilla.id)

def eliminar_del_carrito(request, zapatilla_id):
    carrito = Carrito(request)
    zapatilla = get_object_or_404(Zapatilla, id=zapatilla_id)
    carrito.remove(zapatilla=zapatilla)
    return redirect('ver_carrito')