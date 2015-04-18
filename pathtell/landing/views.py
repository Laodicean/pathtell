from django.shortcuts import render

def home(request, template='landing/index.html'):
    context = {}
    return render(request, template, context)
