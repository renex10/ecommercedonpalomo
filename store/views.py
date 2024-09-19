from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from django.core.paginator import Paginator

def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
    else:
        products = Product.objects.all()
    
    # Paginamos los productos
    paged_products = pagination(request, products, 3)
    product_count = products.count()
    
    return render(request, 'store.html', {
        'products': paged_products,  # Pasamos los productos paginados
        'product_count': product_count,
    })

def pagination(request, products, products_by_page):
    paginator = Paginator(products, products_by_page)
    page = request.GET.get('page')  # Obtenemos el número de la página desde la URL
    paged_products = paginator.get_page(page)  # Usamos get_page
    return paged_products

def products_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category, is_available=True)
    paged_products = pagination(request, products, 3)
    product_count = products.count()
    
    return render(request, 'store.html', {
        'products': paged_products,
        'product_count': product_count,
    })

def product_details(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    return render(request, 'product_detail.html', {'product': product})
