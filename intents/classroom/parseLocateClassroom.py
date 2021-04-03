import json

with open('intentLocateClassroom.json') as intentLocateClassroom:
	intent = json.load(intentLocateClassroom)
with open('../resources/classrooms.json') as classroomModel:
	classroom = json.load(classroomModel)
f = open("generatedIntentLocateClassroom.yml", "w")

for i in intent:
	for c in classroom:
		f.write(i.replace("Cx", classroom[c]['name']) + "\n")

f.close()