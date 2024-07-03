from django.contrib import admin
from django.urls import path, include
from usuarios import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    path('registro/', user_views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('productos/', include('productos.urls')),
    path('carrito/', include('carrito.urls')),
    path('usuarios/', include('usuarios.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)