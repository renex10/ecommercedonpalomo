from django.shortcuts import render
from store.models import Product

def home(request):
    # Obtener productos aleatorios (puedes ajustar la lógica según tus necesidades)
    random_products = Product.objects.filter(is_available=True).order_by('?')[:8]
    
    # Obtener productos populares (puedes ajustar la lógica según tus necesidades)
    popular_products = Product.objects.filter(is_available=True).order_by('-create_date')[:8]
    
    return render(request, 'home.html', {
        'random_products': random_products,
        'popular_products': popular_products
    })

