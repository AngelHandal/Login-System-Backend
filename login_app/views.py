from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages


# Create your views here.

def render_login(request):
    return render(request, "login.html")

def check_login(request):
    if request.method != 'POST':
        return HttpResponse("Method not allowed")
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = authenticate(request, username=username, password=password)
        if user_obj is not None:
            login(request, user_obj)
            return HttpResponseRedirect(reverse("mypage"))
        else:
            messages.error(request, "Username or password is incorrect")
            return HttpResponseRedirect("/")

def mypage(request):
    return render(request, "mypage.html", {'username': request.user.username})


def mypage_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


