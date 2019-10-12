from django.shortcuts import render
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def view_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.all().filter(post=post)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.comment_user = request.user
            instance.post = post
            instance.save()
    form = CommentForm()

    context={
        'post':post, 
        'comments':comments,
        'form':form
    }

    return render(request=request,
                  template_name='post/post.html',
                  context=context)

@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
    form = PostForm()

    return render(request=request,
                    template_name='post/new_post.html',
                    context={
                        'form':form
                    })

def post_like_system(request):
    pass
