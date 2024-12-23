from django.urls import path
from . import views

urlpatterns = [
    path('',views.registration),
    path('login/',views.authentication,name='authentication'),
    
]