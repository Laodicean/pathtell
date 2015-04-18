from classifiers.models import HeartBeatData


def _simulate_heart_beats(person_id, frequency, heart_rate, commit_to_db=True):
    """
    frequency: Frequency of the heart rate calculation in Hz
    heart_rate: the heart rate in BPM
    """
    heart_beats = []
    # day_req_count is the total number of times that the heart rate was 
    # measured in one day
    day_freq_count = (frequency*60) * 60 * 24

    initial_datetime = datetime.datetime.now()

    for i in xrange(day_freq_count):
        fsecs = max(1, int(1/float(frequency)))
        beat_timestamp  = initial_datetime + datetime.timedelta(seconds=fsecs)

        heart_beats.append(HeartBeatData(
            person_id=person_id,
            rate=heart_rate,
            frequency=frequency,
            beat_timestamp=beat_timestamp,
        ))

    if commit_to_db:
        HeartBeatData.objects.bulk_create(heart_beats)
    return heart_beats


def get_latest_person_data(person):
    for users_service in person.service_connections:
        # Retrieve the users information
        if users_service.service.name == 'fitbit':
            # TODO Actually retrieve FITBIT heart rate info from Partner API
            # What I'm actually doing is just making up heart rate information
            # and that looks exactly like the heart rate info from the fitbit partner API
            if person.id == 1:
                # For the Demo -- user 1 does not have any conditions
                _simulate_heart_beats(person_id=person.id, frequency=0.2, heart_rate=65)
            elif person.id == 2:
                # For the Demo -- user 2 has infantile Bradychardia
                _simulate_heart_beats(person_id=person.id, frequency=0.2, heart_rate=99)
                """
                # Frequency of the heart rate calculation in Hz
                frequency = 0.2
                # day_req_count is the total number of times that the heart rate was 
                # measured in one day
                day_freq_count = (frequency*60) * 60 * 24

                initial_datetime = datetime.datetime.now()

                for i in xrange(day_freq_count):
                    fsecs = max(1, int(1/float(frequency)))
                    beat_timestamp  = initial_datetime + datetime.timedelta(seconds=fsecs)
                    heart_beat = {
                        'user_id': 2,
                        'rate': 98,
                        'frequency': 0.2,
                        'beat_timestamp': beat_timestamp,
                    }
                """
            else:
                # For the Demo -- all other users have Ventricular Bradychardia!
                _simulate_heart_beats(person_id=person.id, frequency=0.2, heart_rate=49)
