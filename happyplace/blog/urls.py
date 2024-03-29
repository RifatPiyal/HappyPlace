from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),
    path('FAQ/', views.FAQ, name='blog-FAQ'),
    path('advice/', views.advice, name='blog-advice'),
    path('login/', views.login, name='blog-login'),
    path('login/dashboard/', views.dashboard, name='blog-dashboard'),
    path('loginCounselor/', views.loginCounselor, name='blog-loginCounselor'),
    path('loginCounselor/cdashboard/', views.c_dashboard, name='blog-Cdashboard'),

]
