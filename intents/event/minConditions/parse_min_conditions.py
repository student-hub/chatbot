import json

with open('intentMinConditionsRO.json') as intentMinConditionsRO:
	intentRO = json.load(intentMinConditionsRO)
with open('intentMinConditionsEN.json') as intentMinConditionsEN:
	intentEN = json.load(intentMinConditionsEN)
with open('../../resources/classesFirebase.json') as subjectModel:
	subjects = json.load(subjectModel)
f = open("generatedIntentMinConditionsRO.yml", "w")
fEN = open("generatedIntentMinConditionsEN.yml", "w")

for i in intentRO:
	for subject in subjects['classes']:
		f.write(i.replace("Ex", subject['name']) + "\n")

for i in intentEN:
	for subject in subjects['classes']:
		fEN.write(i.replace("Ex", subject['name']) + "\n")

f.close()
fEN.close()