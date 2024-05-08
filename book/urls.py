from django.urls import path

from book import views

urlpatterns = [
    path("", views.home, name='home'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('register/', views.registerView, name='register'),
]