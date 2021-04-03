import json

with open('intentLocateEvent.json') as intentLocateEvent:
	intent = json.load(intentLocateEvent)
with open('../../resources/classes.json') as subjectModel:
	subjects = json.load(subjectModel)
f = open("generatedIntentLocateEvent.yml", "w")

for i in intent:
	for subject in subjects:
		f.write(i.replace("Ex", subject) + "\n")
		f.write(i.replace("Ex", subjects[subject]['name']) + "\n")

f.close()