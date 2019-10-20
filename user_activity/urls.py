from django.urls import path
from . import views

app_name = 'user_activity'

urlpatterns = [
    path('activity/', views.activity, name='activity'),
]
