import json

with open('intentEndTimeEventRO.json') as intentEndTimeEventRO:
	intentRO = json.load(intentEndTimeEventRO)
with open('intentEndTimeEventEN.json') as intentEndTimeEventEN:
	intentEN = json.load(intentEndTimeEventEN)
with open('../../resources/classes.json') as subjectModel:
	subjects = json.load(subjectModel)
f = open("generatedIntentEndTimeEventRO.yml", "w")
fEN = open("generatedIntentEndTimeEventEN.yml", "w")

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