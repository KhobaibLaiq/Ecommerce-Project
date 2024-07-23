from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product

def home(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'store/home.html', context)

def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'store/category_detail.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
       'product': product,
    }
    return render(request, 'store/product_detail.html', context)

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    
    quantity = int(request.POST.get('quantity', 1))

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += quantity
    else:
        cart[str(product_id)] = {'name': product.name, 'price': str(product.price), 'quantity': quantity}
    
    request.session['cart'] = cart
    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    totalprice = 0
    total_picks = 0
    for item_id, item_data in cart.items():
        quantity = int(item_data['quantity'])
        price = float(item_data['price'])
        totalprice += quantity * price
        total_picks += quantity
    
    context = {
        'cart': cart,
        'totalprice': totalprice,
        'total_picks' : total_picks
    }
    # print(cart)
    # print(total)
    # print(total_pick)
    return render(request, 'store/cart.html', context)


def update_cart(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})

        if str(product_id) in cart:
                cart[str(product_id)]['quantity'] = quantity

        request.session['cart'] = cart
    return redirect('view_cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart.pop(str(product_id))

    request.session['cart'] = cart
    return redirect('view_cart')
