from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from productsapp.models import Product


def create_cartId(request):
    cart = request.session.session_key
    if not cart :
        cart = request.session.create()
        return cart

# Create your views here.
@login_required(login_url="/login")
def cart(request):
    return render(request, 'cart.html')


@login_required(login_url="/login")
def addCart(request, pro_id):
    product  = Product.objects.get(pk=pro_id)
    return render(request, 'cart.html')