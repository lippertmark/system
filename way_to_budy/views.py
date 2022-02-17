from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.template import RequestContext
from .models import Goods, Profile
from django.contrib.auth import logout, authenticate, login
from .forms import UserRegistrationForm, LoginForm



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                    return render(request, 'home')
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            return render(request, 'registration/login.html', {'form': new_user})
        else:
            return HttpResponse('<h1>что-то пошло не так</h1>')
    else:
        user_form = UserRegistrationForm()
        return render(request, 'registration/signup.html', {'form': user_form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):
    context = {"name": request.user}
    return render(request, 'way_to_budy/home.html', context)


@login_required
def store(request):
    context = {'goods': Goods.objects.all()}
    return render(request, 'way_to_budy/store.html', context)


@login_required
def form(request):
    context = {}
    return render(request, 'way_to_budy/form.html', context)


@login_required
def collection(request):
    context = {}
    return render(request, 'way_to_budy/collection.html', context)


@login_required
def calls(request):
    context = {}
    return render(request, 'way_to_budy/calls.html', context)


@login_required
def profile(request):
    context = {}
    return render(request, 'way_to_budy/profile.html', context)
