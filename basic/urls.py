
from django.contrib import admin
from django.urls import path

from basic import views
from django.contrib.auth import views as auth_views
app_name = 'basic'

urlpatterns = [
    path('', views.index, ),
    path('sign-up', views.signup, name='sign-up'),

    path('get-result/', views.get_view, name='get-result'),
]
