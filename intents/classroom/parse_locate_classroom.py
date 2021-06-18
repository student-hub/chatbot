import json

with open('intentLocateClassroomRO.json') as intentLocateClassroomRO:
	intentRO = json.load(intentLocateClassroomRO)
with open('intentLocateClassroomEN.json') as intentLocateClassroomEN:
	intentEN = json.load(intentLocateClassroomEN)
with open('../resources/classroomsFirebase.json') as classroomModel:
	classroom = json.load(classroomModel)
f = open("generatedIntentLocateClassroomRO.yml", "w")
fEN = open("generatedIntentLocateClassroomEN.yml", "w")

for i in intentRO:
	for c in classroom['classrooms']:
		f.write(i.replace("Cx", c['name']) + "\n")

for i in intentEN:
	for c in classroom['classrooms']:
		fEN.write(i.replace("Cx", c['name']) + "\n")

f.close()
fEN.close()