from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('index', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('add', views.addbook, name='addbook'),
    path('delete/<str:id>', views.deletebook, name='deletebook'),
    path('updatebook/<str:id>', views.updatebook, name='updatebook'),
    path('update', views.update, name='update'),



    path('showbooks', views.showbook, name='showbook'),

    #path('s1', views.signup1, name='signup1'),
    #path('',views.sign1,name= 'signin1'),

]
