import json

with open('classrooms.json') as classroomsJSON:
	classrooms = json.load(classroomsJSON)

def getClassroomLocation(name):
    try:
        classroom = classrooms[name]
    except:
        return ""
    return classroom