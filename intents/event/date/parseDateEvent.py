import json

with open('intentGetDateEvent.json') as intentGetDateEvent:
	intent = json.load(intentGetDateEvent)
with open('../../resources/classes.json') as subjectModel:
	subjects = json.load(subjectModel)
f = open("generatedIntentGetDateEvent.yml", "w")

for i in intent:
	for subject in subjects:
		f.write(i.replace("Ex", subject) + "\n")
		f.write(i.replace("Ex", subjects[subject]['name']) + "\n")

f.close()