from django.urls import path
from cartapp import views

urlpatterns=[
    path("cart",views.cart, name="cart"),
    path("cart/add/<int:pro_id>",views.addCart, name="addCart")
]