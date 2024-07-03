from django.urls import path
from . import views

urlpatterns = [
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:zapatilla_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar/<int:zapatilla_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
]