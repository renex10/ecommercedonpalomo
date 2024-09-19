from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('store/', include('store.urls')),  # Incluye las URL de la app 'store'
    path('cart/', include('carts.urls')),  # Incluye las URL de la app 'carts'
    path('account/', include('accounts.urls')),  # Incluye las URL de la app 'accounts'
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

