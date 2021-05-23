import json

with open('intentLocateEventRO.json') as intentLocateEventRO:
	intentRO = json.load(intentLocateEventRO)
with open('intentLocateEventEN.json') as intentLocateEventEN:
	intentEN = json.load(intentLocateEventEN)
with open('../../resources/classes.json') as subjectModel:
	subjects = json.load(subjectModel)
f = open("generatedIntentLocateEventRO.yml", "w")
fEN = open("generatedIntentLocateEventEN.yml", "w")

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