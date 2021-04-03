import json

with open('intentGetTeacherName.json') as intentSearchTeacher:
	intent = json.load(intentSearchTeacher)
with open('../../resources/classrooms.json') as classroomModel:
	classroom = json.load(classroomModel)
f = open("generatedIntentGetTeacherName.yml", "w")

for i in intent:
	for c in classroom:
		f.write(i.replace("Cx", classroom[c]['name']) + "\n")

f.close()