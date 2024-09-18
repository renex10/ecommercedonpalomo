from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

# configurando las rutas para las vistas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('store/', include('store.urls')),
    path('cart/', include('carts.urls')),  # Cambiar 'cart' a 'carts'
   path('account/', include('accounts.urls')),
]

if settings.DEBUG:  # Asegúrate de solo servir archivos media durante el desarrollo
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

