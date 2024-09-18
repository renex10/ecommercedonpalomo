from django.shortcuts import render, redirect
from store.models import Product
from .models import Cart, CartItem

# Función para generar o recuperar el ID del carrito
def cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

# Vista del carrito
""" def cart(reques,total=0,quanity=0,cart_item=None):
    cart = Cart.objects.get(cart_id=cart_id(request))
    cart_items = CartItem.objects.filter(cart=cart,is_active=True)
    for cart_item in cart_items:
        total+= (cart_item.product.price * cart_item.quantity)
        quanity +=cart_item.quantity
    context = {
        'total': total,
        'quanity': quanity,
        'cart_items': cart_items
    }
    
    return render(request, 'cart.html',context=context)  """
    
# Vista del carrito
def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=cart_id(request))  # Obtener el carrito actual
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)  # Obtener items activos del carrito

        # Calcular el total y la cantidad
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity

    except Cart.DoesNotExist:
        cart_items = []  # Si el carrito no existe, el carrito está vacío

    # Pasar los valores al contexto
    context = {
        'total': total,
        'quantity': quantity,  # Corregido: antes estaba mal escrito como "quanity"
        'cart_items': cart_items
    }

    return render(request, 'cart.html', context=context)

# Función para añadir productos al carrito
def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    
    # Obtener o crear un carrito basado en la sesión
    try:
        cart = Cart.objects.get(cart_id=cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=cart_id(request))
    cart.save()

    # Intentar obtener o crear un CartItem
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1  # Aumentar la cantidad si el producto ya está en el carrito
        cart_item.save()
    except CartItem.DoesNotExist:  # Aquí se atrapa la excepción correcta
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart,  # Corregido: falta la coma después de 'quantity'
        )
        cart_item.save()

    return redirect('cart')  # Asegúrate de haber configurado la URL 'cart'


