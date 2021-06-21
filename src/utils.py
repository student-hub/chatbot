import json

with open('classrooms.json') as classroomsJSON:
	classrooms = json.load(classroomsJSON)

def getClassroomLocation(name):
    try:
        classroom = classrooms[name]
    except:
        return ""
    return classroom

def getDayRo(dayName):
    days = {
        "MO":"luni",
        "TU":"marți",
        "WE":"miercuri",
        "TH":"joi",
        "FR":"vineri",
        "SA":"sâmbată",
        "SU":"duminică",
    }

    if days.get(dayName) is not None:
        return days.get(dayName)
    else:
        return "(Nu știu)"

