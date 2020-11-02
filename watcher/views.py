from watcher.models import Business, Neighborhood, Post, Profile
from django.contrib.auth.decorators import login_required
from django.http import request
from django.shortcuts import render

# Create your views here.
def logout(request):
    logout(request)


def welcome(request):
  return render(request, 'welcome.html')

@login_required(login_url="/accounts/login/")
def index(request):
    profile = Profile.objects.get(user=request.user)
    posts = Post.objects.filter(neighborhood=profile.neighborhood)

    if request.method == "POST":
        tag = request.POST.get("selectOption")
        details = request.POST.get("postDetail")

        newPost = Post(
            tag=tag,
            details=details,
            user=request.user,
            neighborhood=profile.neighborhood,
        )
        newPost.save()

    context = {"profile": profile, "posts": posts}
    return render(request, "index.html", context)

@login_required(login_url="/accounts/login/")
def profile(request):
    profile = Profile.objects.get(user=request.user)

    context = {"profile": profile}
    return render(request, "profile.html", context)

@login_required(login_url="/accounts/login/")
def business(request):
    profile = Profile.objects.get(user=request.user)
    businesses = Business.objects.filter(neighborhood=profile.neighborhood)
    print(businesses)

    if request.method == "POST":
        name = request.POST.get("businessName")
        email = request.POST.get("businessEmail")

        newBusiness = Business(
            name=name, user=request.user, neighborhood=profile.neighborhood, email=email
        )

        newBusiness.saveBusniess()

    context = {
        "businesses" : businesses
    }

    return render(request, "business.html", context)
