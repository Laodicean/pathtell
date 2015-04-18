from django.shortcuts import render


<<<<<<< HEAD
def home(request, template='landing/home.html'):
    if request.user.is_authenticated():
        # return HttpResponseRedirect()
        pass
=======
def home(request, template='landing/index.html'):
>>>>>>> Starting login on landing
    context = {}
    return render(request, template, context)
