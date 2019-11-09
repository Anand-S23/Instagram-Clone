from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login as dj_login, get_user_model, logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserCreationForm, UserLoginForm
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, TemplateView
from django.contrib import messages  
from django.contrib.auth.decorators import login_required
from .models import MyUser
from post.models import Post
from user_activity.models import Act

# Create your views here.

# Register User 
def register(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # request.FILES - profile picture 
        if form.is_valid():
            form.save()
            # Logs in user when registration complete 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            dj_login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
        
    context = {
        'form': form
    }

    return render(request=request, 
                  template_name='accounts/register.html', 
                  context=context)    


# Log in User 
def login_view(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        dj_login(request, user_obj)
        return HttpResponseRedirect("/")

    context = {
        'form': form
    }

    return render(request=request, 
                  template_name="accounts/login.html", 
                  context=context)    


# Logs Out User 
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/login")


# User Details 
class UserDetailView(LoginRequiredMixin, DetailView):
    model = MyUser
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username' 

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(user=self.object)
        return context


 
# Redirects to user detail 
class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('accounts:detail',
                       kwargs={'username': self.request.user.username})


# Let's user update info 
class UserUpdateView(LoginRequiredMixin, UpdateView):
    fields = ['email', 'name', 'picture', 'bio', ]
    model = MyUser

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('accounts:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return MyUser.objects.get(username=self.request.user.username)


# List of all the users - Discover 
class UserListView(LoginRequiredMixin, ListView):
    model = MyUser
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'
    users = MyUser.objects.all()


# Follow System
class UserFollowSystem(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        username = self.kwargs.get('username')
        obj = get_object_or_404(MyUser, username=username)
        user = self.request.user 
        act = Act(to_user=obj, from_user=user, act='followed')
        if user in obj.followers.all():
            obj.followers.remove(user)
            user.following.remove(obj)
        else: 
            obj.followers.add(user)
            user.following.add(obj)
            act.save()
        return reverse('accounts:detail',
                       kwargs={'username': username})


# View to see the following of a user 
@login_required
def UserFollowing(request, username):
    user = get_object_or_404(MyUser, username=username)
    
    context = {
        'user':user
    }

    return render(request=request, 
                  template_name='accounts/myuser_following.html',
                  context=context)


# View to see the followers of a user 
@login_required
def UserFollowers(request, username):
    user = get_object_or_404(MyUser, username=username)
    
    context = {
        'user':user
    }
    
    return render(request=request, 
                  template_name='accounts/myuser_followers.html',
                  context=context)


# Show the activity for users 
@login_required
def Activity(request):
    return render(request=request,
                  template_name='accounts/activity.html')
