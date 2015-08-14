from feed.models import Alert


def get_person_alerts(person):
    return Alert.objects.filter(person=person).order_by('-timestamp')
