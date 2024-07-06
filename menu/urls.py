# menu/urls.py
from django.urls import path
from .import views
from .views import customer_form_view, success_view

urlpatterns = [
    path('', views.menu_view, name='menu_view'),
    path('index/', views.slider_view, name='slider_view'),
    path('customer_form/', customer_form_view, name='customer_form'),
    path('success/', success_view, name='success'),
    path('about/', views.about, name='about'),

]


