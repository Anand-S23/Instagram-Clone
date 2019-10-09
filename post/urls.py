from django.urls import path
from . import views

urlpatterns = [
    path('post/new/', views.new_post, name='new_post'),
    path('post/<int:pk>/', views.view_post, name='view_post')
]