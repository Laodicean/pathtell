from django.shortcuts import render
from services.models import PersonServiceConnection
from services.forms import AddPersonServiceConnectionForm
from services.logic.generate import make_services


def person_add_service_view(request, template='services/home.html'):
    make_services()
    if not request.user.is_authenticated():
        return redirect('/')

    form = AddPersonServiceConnectionForm(request.POST)
    person = request.user.person

    context = {}
    if form.is_valid():
        psc = PersonServiceConnection(
            user=person,
            service_id=form.cleaned_data['service_id'],
            auth_token='faked',
        )
        psc.save()
        context['success'] = True

    return render(request, template, context)
