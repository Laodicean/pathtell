from django.shortcuts import render


def home(request, template='landing/home.html'):
    if request.user.is_authenticated():
        # return HttpResponseRedirect()
        pass
    context = {}
    return render(request, template, context)
