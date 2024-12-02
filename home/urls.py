

# home/urls.py
from django.urls import path
from . import views
from .views import sell_device, privacy_policy
from .views import terms_conditions, franchise_view
from .views import career_view, apply_for_job, contact_page
from .views import blogs_page, blog_detail, products_view, product_details
from .views import cart_view, update_cart_view


urlpatterns = [
    path('', views.index, name='index'),
    path('repair/', views.repair_page, name='repair_page'),
    path('sell/', sell_device, name='sell_device'),
    path('terms-and-conditions/', terms_conditions, name='terms_conditions'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('franchise/', franchise_view, name='franchise'),
    path('career/', career_view, name='career'),
    path('contact/', contact_page, name='contact'),
    path('apply/<int:job_id>/', apply_for_job, name='apply_for_job'),
    path('blogs/', blogs_page, name='blogs_page'),
    path('blogs/<slug:slug>/', blog_detail, name='blog_detail'),
    path('products/', products_view, name='products'),
    
    path('products/<int:product_id>/', product_details, name='product_details'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='view_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/confirm_order/', views.confirm_order, name='confirm_order'),
    path('update-cart/', update_cart_view, name='update_cart_view'),
    path('cart/increment/<int:accessory_id>/', views.increment_quantity, name='increment_quantity'),
    path('cart/decrement/<int:accessory_id>/', views.decrement_quantity, name='decrement_quantity'),
    

    
]
