from .models import UserU
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.urls import reverse

def create_user(request):
    if request.method == "POST":
        form = {
            'login': request.POST["login"],
            'mail': request.POST["mail"],
            'password': request.POST["password"]
        }
        if form["login"] and form["mail"] and form["password"]:
            try:
                User.objects.get(username = form["login"])
                form['errors'] = u"Не уникальное имя пользователя!"
                return render(request, 'create_user.html', {'form': form})
            except User.DoesNotExist:
                User.objects.create_user(form["login"], form["mail"], form["password"])
                return redirect('filbet')
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'create_user.html', {'form': form})
    else:
        return render(request, 'create_user.html', {})
def login_user(request):
    if request.method == "POST":
        form = {
            'login': request.POST["login"],
            'password': request.POST["password"]
        }
        if form["login"] and form["password"]:
            user = authenticate(username=form["login"], password=form["password"])
            if user == None:
                form['errors'] = u"Неверный логин или пароль"
                return render(request, 'login.html', {'form': form})
            else:
                login(request, user) 
                return redirect('filbet')
        else:
            form['errors'] = u"У вас имеются пустые поля!"
            return render(request, 'login.html', {'form': form})
    else:
        return render(request, 'login.html', {})
def logout_user(request):
	logout(request)
	

# Create your views here.
