from django.urls import path
from . import views
from .views import cart_add,cart_detail,cart_remove

app_name ='cart'

urlpatterns = [
    path("add/<int:product_id>/",views.cart_add,name='cart_add'),
    path("",views.cart_detail,name="cart_detail"),
    path("remove/<int:product_id>/",cart_remove,name="remove")
]