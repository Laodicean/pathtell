from django.shortcuts import render, redirect
from feed.models import Event, Alert
from feed.logic.alerts import get_person_alerts
from feed.logic.events import get_person_events
import copy
import random


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
    context = testContext()
    return render(request, template, context)

def testContext():
    context = {
            'alerts':[],
            'events':[]
        }
    a = Alert()

    e = Event()
    for i in range(15):
        if i == 12:
            e.getGraph = [(5*j+1,110-random.randint(0,20)) for j in range(20)]
            e.result = False
            e.condition = "Infantile Ventricular Bradychardia"
        elif i == 10 or random.randint(0,3) == 0:
            e.getGraph = [(5*j+1,60-random.randint(0,20)) for j in range(20)]
            e.result = False
            e.condition = "Ventricular Bradychardia"
        else:
            e.getGraph = [(5*j+1,75-random.randint(0,20)) for j in range(20)]
            e.result = True
            e.condition = "Ventricular Bradychardia"


        e.id = i
        e.timestamp = "%s/4/2015 2:29 am" % (19 - i)
        if e.result == False:
            a.id = i
            a.condition = e.condition
            context['alerts'].append(copy.deepcopy(a))
        context['events'].append(copy.deepcopy(e))

    return context
