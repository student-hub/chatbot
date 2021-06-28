import json

with open('classrooms.json') as classroomsJSON:
	classrooms = json.load(classroomsJSON)

with open('groupLeaders.json') as groupLeadersJSON:
	groupLeaders = json.load(groupLeadersJSON)

with open('srLeaders.json') as srLeadersJSON:
	srLeaders = json.load(srLeadersJSON)

def getClassroomLocation(name):
    try:
        classroom = classrooms[name]
    except:
        return ""
    return classroom

def getGroupLeader(groupName):
    try:
        return groupLeaders[groupName]["leader"]
    except:
        return ""

def getSrLeader(srName):
    try:
        return srLeaders[srName]["leader"]
    except:
        return ""

def getTeacherName(classroomName):
    try:
        return classrooms[classroomName]["teacher"]
    except:
        return ""

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

def getTypeRo(type):
    types = {
        "cursul": "lecture",
        "seminarul": "seminar",
        "laboratorul": "lab",
        "labul":"lab"
    }
    if types.get(type) is not None:
        return types.get(type)
    else:
        return "eveniment-nerecunoscut"