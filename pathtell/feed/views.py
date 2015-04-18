from django.shortcuts import render
from feed.models import Event, Alert
import copy

# Create your views here.
def feed(request, template='feed/feed.html'):
    context = {
            'alerts':Alert.objects.all(),
            'events':Event.objects.all()
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
