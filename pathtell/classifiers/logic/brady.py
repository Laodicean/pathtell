

def detect_daily_brady(daily_heart_rate):
    """
    --- Detect Ventricular Bradychardia ---
     -> If resting heart rate is ever under 50
     -> Not Infant
    --- Detect Infantile Bradychardia ---
     -> If resting heart rate is ever under 100
     -> Is infant
    """
    is_detected = False
    if user.is_infant():
        # Check for infantile bradychardia
        for hb in daily_heart_rate:
            if hb < 100:
                is_detected = True
    else:
        # Check for non-infantile cases of bradychardia
        # Ventricular Bradychardia
        for hb in daily_heart_rate:
            if hb < 50:
                is_detected = True
    return is_detected
