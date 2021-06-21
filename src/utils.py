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
        "Monday":"luni",
        "Tuesday":"marți",
        "Wednesday":"miercuri",
        "Thursday":"joi",
        "Friday":"vineri",
        "Saturday":"sâmbată",
        "Sunday":"duminică",
    }
    return days.get(dayName, lambda: "zi invalidă")
