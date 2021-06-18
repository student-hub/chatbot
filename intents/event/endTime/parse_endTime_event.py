import json

with open('intentEndTimeEventRO.json') as intentEndTimeEventRO:
	intentRO = json.load(intentEndTimeEventRO)
with open('intentEndTimeEventEN.json') as intentEndTimeEventEN:
	intentEN = json.load(intentEndTimeEventEN)
with open('../../resources/classesFirebase.json') as subjectModel:
	subjects = json.load(subjectModel)
f = open("generatedIntentEndTimeEventRO.yml", "w")
fEN = open("generatedIntentEndTimeEventEN.yml", "w")

for i in intentRO:
	for subject in subjects['classes']:
		f.write(i.replace("Ex", subject['name']) + "\n")

for i in intentEN:
	for subject in subjects['classes']:
		fEN.write(i.replace("Ex", subject['name']) + "\n")

f.close()
fEN.close()