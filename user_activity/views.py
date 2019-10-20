from django.shortcuts import render
from .models import Act

# Create your views here.
def activity(request):
    activities = Act.objects.filter(to_user=request.user).order_by('-act_time')
    
    return render(request=request,
                  template_name='activity/activity.html',
                  context={'activites':activities})