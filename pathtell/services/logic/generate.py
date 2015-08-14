from services.models import Service


def make_services():
    if Service.objects.filter(name='fitbit').count() < 1:
        fitbit = Service(id=1, name='fitbit')
        fitbit.save()

