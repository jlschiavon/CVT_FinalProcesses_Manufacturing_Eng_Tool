from datetime import datetime
import pandas as pd

def asignar_turno(ts):
    h = ts.hour + ts.minute / 60
    if 7 <= h < 15:
        return "1st Shift"
    elif 15 <= h < 22.5:
        return "2nd Shift"
    else:
        return "3rd Shift"
