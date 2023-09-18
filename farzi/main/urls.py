from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('custlive/', views.custlive, name='custlive'),
    path('display_all_objects/', views.display_all_objects, name='display_all_objects'),
    path('singleview/<int:product_id>/',views.singleview,name='singleview'),
    path('inactiveseller/<int:stid2>/',views.inactiveseller, name='inactiveseller'),
    path('add_cart/<int:bookid2>/', views.add_cart, name='add_cart'),
    path('delete_cart/<int:bookid2>/', views.delete_cart, name='delete_cart'),
    path('cart',views.cart,name="cart"),
    path('wishlist',views.wishlist,name="wishlist"),
    path('add_wishlist/<int:bookid2>/', views.add_wishlist, name='add_wishlist'),
    path('delete_wishlist/<int:bookid2>/', views.delete_wishlist, name='delete_wishlist'),
    path('separate/', views.separate, name='separate'),
    path('product-list/', views.product_list, name='product_list'),
    path('full-list/', views.full_list, name='full_list'),
    

]
