from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('redirect/', views.UserRedirectView.as_view(), name='redirect'),
    path('update/', views.UserUpdateView.as_view(), name='update'),
    path('explore/', views.UserListView.as_view(), name='list'),
    path('user/<str:username>/', view=views.UserDetailView.as_view(), name='detail'),
    path('user/<str:username>/follow/', views.UserFollowSystem.as_view(), name='follow'),
    path('user/<str:username>/following/', views.UserFollowing, name='following'),
    path('user/<str:username>/followers/', views.UserFollowers, name='followers')
]
