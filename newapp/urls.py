from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('mumbai/<int:id>',views.news,name='mumbai'),

]