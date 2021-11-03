from django.urls import path
from . import views

urlpattersn = [
    path('', views.post_list, name='post_list'),
]