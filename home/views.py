from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from post.models import Post

# Create your views here.
@login_required
def HomeView(request):
    posts = Post.objects.all().order_by('post_date') #to display the post of users in following 
    
    return render(request=request,
                  template_name='home/home.html',
                  context={'posts':posts})

