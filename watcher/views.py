from watcher.models import Profile
from django.http import request
from django.shortcuts import render

# Create your views here.
def logout(request):
  logout(request)
  
def index(request):
  return render(request, 'index.html')

def profile(request):
  profile = Profile.objects.get(user = request.user)
  
  context = {
    'profile' : profile
  }
  return render(request, 'profile.html', context)