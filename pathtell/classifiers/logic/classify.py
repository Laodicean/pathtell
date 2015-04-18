from classifiers.logic.brady import detect_daily_brady
from services.logic.retrieve import get_latest_person_data
from feed.models import Event
from classifiers.models import HeartBeatData


def classify(person):

    # Get users latest information from connected services
    get_latest_person_data(person=person)

    # Run bradychardia classification
    """
    daily_heart_rate_grouped = HeartBeatData.objects.filter(
                                    person=person
                                ).group_by('beat_timestamp')
    """
    # unique_days = HeartBeatData.objects.filter(person=person).distinct('beat_date').order_by('beat_date')
    
    person_hrs = HeartBeatData.objects.filter(person=person).all()
    person_hr_by_date = {}
    for person_hr in person_hrs: 
        if str(beat_date) in person_hr:
            person_hr_by_date[str(beat_date)].append(person_hr)
        else:
            person_hr_by_date[str(beat_date)] = [person_hr]

    hr_per_day_list = []
    for hr_per_day in person_hr_by_date:
        hr_per_day_list.append(
            HeartBeatData.objects.filter(
                person=person,
                beat_date=hr_per_day.beat_date,
            )
        )
        
        # for daily_heart_rate in HeartBeatData.objects.filter(person=person).group_by('beat_date'):
        for daily_heart_rate in hr_per_day:
            if Event.objects.filter(person=person, daily_heart_rate=daily_heart_rate[0].beat_date).count() == 0:
                condition = detect_daily_brady(daily_heart_rate)
                new_event = Event(
                    person=person,
                    result=result,
                    condition=condition,
                    event_graph='',
                )
                new_event.save()

                if condition:
                    result = True
                    if condition == 'infantile' or 'ventricular':
                        new_alert(
                            person=person,
                            event=new_event,
                            condition=condition,
                        )
                        new_alert.save()
                else:
                    result = False
