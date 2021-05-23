import json

with open('intentMinConditionsRO.json') as intentMinConditionsRO:
	intentRO = json.load(intentMinConditionsRO)
with open('intentMinConditionsEN.json') as intentMinConditionsEN:
	intentEN = json.load(intentMinConditionsEN)
with open('../../resources/classes.json') as subjectModel:
	subjects = json.load(subjectModel)
f = open("generatedIntentMinConditionsRO.yml", "w")
fEN = open("generatedIntentMinConditionsEN.yml", "w")

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