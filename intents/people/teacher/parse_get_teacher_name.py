import json

with open('intentGetTeacherNameRO.json') as intentSearchTeacherRO:
	intentRO = json.load(intentSearchTeacherRO)
with open('intentGetTeacherNameEN.json') as intentSearchTeacherEN:
	intentEN = json.load(intentSearchTeacherEN)
with open('../../resources/classroomsFirebase.json') as classroomModel:
	classroom = json.load(classroomModel)
f = open("generatedIntentGetTeacherNameRO.yml", "w")
fEN = open("generatedIntentGetTeacherNameEN.yml", "w")

for i in intentRO:
	for c in classroom['classrooms']:
		f.write(i.replace("Cx", c['name']) + "\n")

for i in intentRO:
	for c in classroom['classrooms']:
		f.write(i.replace("Cx", c['name']) + "\n")

f.close()
fEN.close()