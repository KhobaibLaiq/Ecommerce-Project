from django.shortcuts import render, redirect, get_object_or_404
from store.models import Category, Product
from .forms import CategoryForm, ProductForm
from django.contrib.auth.decorators import user_passes_test

def admin_required(user):
    return user.is_staff

@user_passes_test(admin_required)
def admin_dashboard(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {'categories': categories, 'products': products}
    return render(request, 'custom_admin/dashboard.html', context)

@user_passes_test(admin_required)
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = CategoryForm()
    context = {'form': form}
    return render(request, 'custom_admin/add_category.html', context)

@user_passes_test(admin_required)
def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = CategoryForm(instance=category)
    context = {'form': form}
    return render(request, 'custom_admin/edit_category.html', context)

@user_passes_test(admin_required)
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('admin_dashboard')
    context = {'category': category}
    return render(request, 'custom_admin/delete_category.html', context)



@user_passes_test(admin_required)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'custom_admin/add_product.html', context)

@user_passes_test(admin_required)
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ProductForm(instance=product)
    context = {'form': form}
    return render(request, 'custom_admin/edit_product.html', context)

@user_passes_test(admin_required)
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('admin_dashboard')
    context = {'product': product}
    return render(request, 'custom_admin/delete_product.html', context)
