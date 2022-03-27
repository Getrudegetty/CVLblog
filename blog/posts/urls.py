from django.urls import path 
from  . import views

app_name= 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('post/<str:pk>', views.post, name='post'),
]