from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Event


def index(request):
    events = Event.objects.all()
    return render(request, "events/index.html", {"events": events})


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("home")

    return render(request, "events/register.html")


def user_login(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("home")

    return render(request, "events/login.html")


def user_logout(request):
    logout(request)
    return redirect("login")


# 👇 ADD THIS LINE
@login_required
def add_event(request):

    if request.method == "POST":

        title = request.POST["title"]
        description = request.POST["description"]
        date = request.POST["date"]
        location = request.POST["location"]

        Event.objects.create(
            title=title,
            description=description,
            date=date,
            location=location,
            created_by=request.user
        )

        return redirect("home")

    return render(request, "events/add_event.html")