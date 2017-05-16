from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.template import loader 
from django.shortcuts import render, get_object_or_404
from .forms import UserForm


def index(request):
    template = loader.get_template('portfolio/index.html')
    return render(request, 'portfolio/index.html')







def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'portfolio/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'portfolio/index.html')
                #if active user do stuff. import stock data etc
            else:
                return render(request, 'portfolio/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'portfolio/login.html', {'error_message': 'Invalid login'})
    return render(request, 'portfolio/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'portfolio/index.html')
    context = {
        "form": form,
    }
    return render(request, 'portfolio/register.html', context)

