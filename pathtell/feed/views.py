from django.shortcuts import render, redirect
from feed.models import Event, Alert
from feed.logic.alerts import get_person_alerts
from feed.logic.events import get_person_events
# import copy


# Create your views here.
def feed(request, template='feed/feed.html'):
    if not request.user.is_authenticated():
        return redirect('appauth_home')
    person = request.user.person
    print(person)    
    context = {
        'alerts': get_person_alerts(person=person),
        'events': get_person_events(person=person),
    }
    
    return render(request, template, context)

"""
def testContext():
    context = {
            'alerts':[],
            'events':[]
        }

    a = Alert()

    e = Event()
    for i in range(10):
        e.id = i
        e.condition = "Condition %s" % i
        e.timestamp = str(i) * 10
        e.result = (e.id % 3 == 0)
        if e.result:
            a.id = i
            a.condition = "Condition %s" % i
            context['alerts'].append(copy.deepcopy(a))
        context['events'].append(copy.deepcopy(e))

    return context
"""
