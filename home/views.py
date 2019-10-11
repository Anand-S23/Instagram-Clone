from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from post.models import Post

# Create your views here.
@login_required
def HomeView(request):
    #posts = Post.objects.filter(request.user__following) to desplay the post of users in following 
    
    return render(request=request,
                  template_name='home/home.html',)

