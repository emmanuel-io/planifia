from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, HttpResponse
from .forms import CustomUserCreationForm
from .models import CustomUser

def user_list(request):
    users = CustomUser.objects.all()
    return render(request, "users/user_list.html", {"users": users})


# Vue pour créer un utilisateur
def create_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("user_list")  # Redirige vers la liste des utilisateurs
    else:
        form = CustomUserCreationForm()

    return render(request, "users/create_user.html", {"form": form})


# Vue pour supprimer un utilisateur
def delete_user(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
        user.delete()
        return redirect("user_list")  # Redirige vers la liste des utilisateurs
    except User.DoesNotExist:
        raise Http404("User not found")


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
