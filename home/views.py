from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def HomeView(request):
    return render(request=request,
                  template_name='home/home.html',)

