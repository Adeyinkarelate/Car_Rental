from django.urls import path 
from . import views

urlpatterns = [
    path('',views.car_list, name='car_list'),
    path('search', views.search , name='search'),
    path('brand', views.brand , name='brand'),
    path('brand_delete/<int:id>',views.brand_delete , name='brand_delete'),
    path('car_detail/<int:id>', views.car_detail, name='car_detail'),
    path('brand_update/<int:id>', views.brand_update, name='brand_update'),
    path('booking/<int:id>', views.booking, name='booking'),
]