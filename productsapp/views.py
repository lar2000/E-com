from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from productsapp.models import Product

from django.core.paginator import Paginator #Django page number.

def index(request):
    obj_product = Product.objects.filter(istrending=True) 
    return render(request,"index.html",{"products": obj_product})

def ProductDetials(request,id):
    pro_field=Product.objects.get(pk=id)
    return render(request,"detail.html",{"productfield":pro_field})

def products(request):
    pro_all = Product.objects.all().order_by("name")
    page = request.GET.get("page") #ກຳນົດເລກຫນ້າ
    pagin = Paginator(pro_all, 3) #ຈຳນວນຫນ້າ
    pro_all = pagin.get_page(page)
    
    return render(request,"products.html",{"pro_all":pro_all})