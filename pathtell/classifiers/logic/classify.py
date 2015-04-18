from classifiers.logic.brady import detect_daily_brady
from services.logic.retrieve import get_latest_person_data


def classify(person):

    # Get users latest information from connected services
    get_latest_user_data(person=person)

    # Run bradychardia classification
    detect_daily_brady() 
