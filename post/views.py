from django.shortcuts import render
from .models import Post, Comment

# Create your views here.
def PostView(request, pk):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.all().filter(post=post)
    return render(request=request,
                  template_name='post/post.html',
                  context={
                      'post':post, 
                      'comments':comment
                  })
