from classifiers.logic.brady import detect_daily_brady
from services.logic.retrieve import get_latest_person_data


def classify(person):

    # Get users latest information from connected services
    get_latest_user_data(person=person)

    # Run bradychardia classification
    daily_heart_rate_grouped = HeartBeatData.objects.filter(
                                    person=person
                                ).group_by('beat_timestamp')
    for daily_heart_rate in HeartBeatData.objects.filter(person=person).group_by('beat_date'):
        detect_daily_brady(daily_heart_rate)
