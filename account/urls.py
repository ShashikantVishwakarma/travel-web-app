from django.urls import path
from . import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('about',views.about,name='about'),
    path('contact', views.contact, name='contact'),
    path('open',views.open,name='open'),
    path('logout',views.logout,name='logout')

]