import json

with open('intentMinNrOfAttendingsRO.json') as intentMinNrOfAttendingsRO:
	intentRO = json.load(intentMinNrOfAttendingsRO)
with open('intentMinNrOfAttendingsEN.json') as intentMinNrOfAttendingsEN:
	intentEN = json.load(intentMinNrOfAttendingsEN)
with open('../../resources/classes.json') as subjectModel:
	subjects = json.load(subjectModel)
f = open("generatedIntentMinNrOfAttendingsRO.yml", "w")
fEN = open("generatedIntentMinNrOfAttendingsEN.yml", "w")

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