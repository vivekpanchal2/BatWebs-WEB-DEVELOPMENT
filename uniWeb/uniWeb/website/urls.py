from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('join', views.join , name='join'),
    path('manage', views.manage , name='manage'),
    path('delete/<int:phone>/', views.delete , name='delete'),
    path('update/<int:phone>/', views.update , name='update'),
    path('do_update/<int:phone>/', views.do_update , name='do_update')
]