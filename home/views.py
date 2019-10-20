from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from post.models import Post
from accounts.models import MyUser

# Create your views here.
@login_required
def HomeView(request):
    posts = Post.objects.filter(user__in=request.user.following.all()) 
    
    return render(request=request,
                  template_name='home/home.html',
                  context={'posts':posts})

