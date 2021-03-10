import json

with open('intentLocateEvent.json') as intentLocateEvent:
	intent = json.load(intentLocateEvent)
with open('../resources/classrooms.json') as classroomModel:
	classroom = json.load(classroomModel)
f = open("generatedIntentLocateEvent.yml", "w")

for i in intent:
	for c in classroom:
		f.write(i.replace("Cx", classroom[c]['name']) + "\n")

f.close()