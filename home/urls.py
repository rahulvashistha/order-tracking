from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('trackorder', views.trackorder, name='trackorder'),
    path('search', views.search, name='search'),
]