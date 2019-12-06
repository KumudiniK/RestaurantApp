from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addQ/', views.addQ, name='addQ'),
    path('<int:restaurant_id>/detail/', views.detail, name='detail'),
    path('<int:restaurant_id>/addItems/',views.addItems, name='addItems')
    

    
]