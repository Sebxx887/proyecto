from django.urls import path
from . import views

urlpatterns = [
    path('productos/<int:id>/', views.detalle_zapatilla, name='detalle_zapatilla'),
    path('', views.lista_zapatillas, name='lista_zapatillas'),
]
