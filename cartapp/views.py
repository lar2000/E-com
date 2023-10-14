from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from productsapp.models import Product
from cartapp.models import Cart, CartItem


def create_cartId(request):
    cart = request.session.session_key
    if not cart :
        cart = request.session.create()
    return cart

# Create your views here.
@login_required(login_url="/login")
def cart(request):
    counter = 0
    total = 0
    
    try:
        #ດຶງຂໍ້ມູນກະຕ່າ
        cart = Cart.objects.get(cart_id = create_cartId(request), customer = request.user)
        #ດຶງຂໍ້ມູນສິນຄ້າໃນກະຕ່າ
        cartItem = CartItem.objects.filter(cart = cart)
        
        for item in cartItem:
            counter += item.quantity
            total += (item.product.price * item.quantity)
    
    except (Cart.DoesNotExist,CartItem.DoesNotExist):    
        cart = None
        cartItem = None
    return render(request, 'cart.html', {"cartItem":cartItem, "total":total, "counter":counter})


@login_required(login_url="/login")
def addCart(request, pro_id):
    product  = Product.objects.get(pk=pro_id)
    # ສ້າງກະຕ່າສິນຄ້າ
    try:
        # ມີກະຕ່າຢູ່ແລ້ວ
        cart = Cart.objects.get(cart_id = create_cartId(request))
        
    except Cart.DoesNotExist:
        # ຍັງບໍ່ມີກະຕ່າ
        cart = Cart.objects.create(
            cart_id = create_cartId(request),
            customer = request.user)
        cart.save()
        
        try: 
    # ຊື້ສິນຄ້າເດີມ
            cartitem = CartItem.objects.get(product = product, cart = cart)
            if cartitem.quantity<cartitem.product.stock:
                cartitem.quantity+=1,
                cartitem.save()
                
        except CartItem.DoesNotExist:
    # ຊື້ສິນຄ້າໃຫມ່(ຄັ້ງແລກ)
          cartitem = CartItem.objects.create(
                product = product,
                cart = cart,
                quantity = 1
          )
          cartitem.save()
    
    return redirect('/cart')