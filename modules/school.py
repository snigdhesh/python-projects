def getSchoolStatus(currentTime):
    if 8 <= currentTime.hour < 18:
        return 'school is open'
    else:
        return 'school is closed'