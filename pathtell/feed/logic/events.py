from feed.models import Event
from classifiers.logic.classify import classify


def get_person_events(person):
    # update events
    # call classify which will create events as necessary 
    classify(person=person)
    return Event.objects.filter(person=person).order_by('-timestamp')
