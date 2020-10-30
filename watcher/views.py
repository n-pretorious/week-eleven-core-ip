from django.shortcuts import render

# Create your views here.
def logout(request):
  logout(request)
  
def index(request):
  return render(request, 'index.html')