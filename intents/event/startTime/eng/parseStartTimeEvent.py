import json

with open('intentStartTimeEvent.json') as intentStartTimeEvent:
	intent = json.load(intentStartTimeEvent)
with open('../../resources/classes.json') as subjectModel:
	subjects = json.load(subjectModel)
f = open("generatedIntentStartTimeEvent.yml", "w")

for i in intent:
	for subject in subjects:
		f.write(i.replace("Ex", subject) + "\n")
		f.write(i.replace("Ex", subjects[subject]['name']) + "\n")

f.close()