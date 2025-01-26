from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product

def index(request):
    items = Product.objects.all()
    context = {'items':items}
    return render(request, 'myapp/index.html', context)

def indexItem(request, productId):
    item = Product.objects.get(id=productId)
    context = {
        'item':item
    }
    return render(request, 'myapp/detail.html', context)

def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES['upload']
        item = Product(name=name, price=price, description=description, image=image)
        item.save()
        
    return render(request, 'myapp/additem.html')

def update_item(request, productId):
    item = Product.objects.get(id=productId)
    
    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.price = request.POST.get('price')
        item.description = request.POST.get('description')
        item.image = request.FILES.get('upload', item.image)
        item.save()
        return redirect("/myapp/")
        
    context = {'item':item}
    return render(request, 'myapp/updateItem.html', context)

def delete_item(request, productId):
    item = Product.objects.get(id=productId)
    
    if request.method == 'POST':
        item.delete()
        return redirect("/myapp/")
        
    context = {'item':item}
    return render(request, 'myapp/deleteItem.html', context)