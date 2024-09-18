from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),  # Aquí se define el nombre 'store'
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    path('<slug:category_slug>/', views.product_details, name='product_details')

]
