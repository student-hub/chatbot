import json

with open('intentStartTimeEventRO.json') as intentStartTimeEventRO:
	intentRO = json.load(intentStartTimeEventRO)
with open('intentStartTimeEventEN.json') as intentStartTimeEventEN:
	intentEN = json.load(intentStartTimeEventEN)
with open('../../resources/classes.json') as subjectModel:
	subjects = json.load(subjectModel)
f = open("generatedIntentStartTimeEventRO.yml", "w")
fEN = open("generatedIntentStartTimeEventEN.yml", "w")

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