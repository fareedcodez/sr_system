from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    
     path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutUser, name='logout'),
    path('register/',views.registerPage, name='register'),
    path('profile/<str:pk>/',views.userProfile, name='user-profile'),
    
    path('',views.home, name= 'home'),
    path('repository/<str:pk>/',views.repository, name= 'repository'),

    path('create-repository/', views.createRepository, name= "create-repository"),
    path('update-repository/<str:pk>/', views.updateRepository, name= "update-repository"),
    path('delete-repository/<str:pk>/', views.deleteRepository, name= "delete-repository"),

     path('colleges/',views.collegePage, name='communities'),
    path('titles/', views.titlePage, name= "titles"),
     path('authors/<str:pk>/', views.authorsPage, name= "authors"),
    
]