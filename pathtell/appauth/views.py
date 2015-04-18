from django.shortcuts import render, redirect
from appauth.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(request, template='landing/index.html'):
    context = {'anchor':'#login'}
    return render(request, template, context)


def register_view(request, template='appauth/home.html'):
    form = RegisterForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        dob = form.cleaned_data['dob']
        user = User.objects.create_user(email, email, password)
        person = user.person
        person.dob = dob
        person.save()
        user = authenticate(username=email, password=password)
        login(request, user)
        return redirect('feed')
        # TODO redirect user to feed
    context = {}
    context['form'] = form
    return render(request, template, context)


def login_view(request, template='appauth/home.html'):
    form = LoginForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(username=email, password=password)
        login(request, user)
        return redirect('feed')
    context = {}
    context['form'] = form
    return render(request, template, context)


def logout_view(request):
    logout(request)
    return redirect('appauth_home')
