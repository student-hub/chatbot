import json

with open('intentGetDateEventRO.json') as intentGetDateEventRO:
	intentRO = json.load(intentGetDateEventRO)
with open('intentGetDateEventEN.json') as intentGetDateEventEN:
	intentEN = json.load(intentGetDateEventEN)
with open('../../resources/classes.json') as subjectModel:
	subjects = json.load(subjectModel)
f = open("generatedIntentGetDateEventRO.yml", "w")
fEN = open("generatedIntentGetDateEventEN.yml", "w")

for i in intentRO:
	for subject in subjects:
		f.write(i.replace("Ex", subject) + "\n")
		f.write(i.replace("Ex", subjects[subject]['name']) + "\n")

for i in intentEN:
	for subject in subjects:
		fEN.write(i.replace("Ex", subject) + "\n")
		fEN.write(i.replace("Ex", subjects[subject]['name']) + "\n")

f.close()
fEN.close()