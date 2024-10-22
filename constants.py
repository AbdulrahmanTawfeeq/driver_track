from datetime import time, timedelta

VEHICLE_MIN_STUDENTS = {
    "taxi": 2,
    "minibus": 10,
    "bus": 17
}

MORNING_TIME_RANGE = (time(6, 25), time(8, 35))
AFTERNOON_TIME_RANGE = (time(13, 15), time(15, 45))

TIME_TOLERANCE = timedelta(minutes=5)