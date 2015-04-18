from django.shortcuts import render


def home(request, template='landing/home.html'):
    context = {}
    return render(request, template, context)
