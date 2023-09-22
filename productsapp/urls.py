from django.urls import path
from productsapp import views

urlpatterns=[
    path("",views.index, name="Home"),
    path("product/details/<int:id>",views.ProductDetials,name="productdetails"),
    path("products",views.products, name="all_product"),
]