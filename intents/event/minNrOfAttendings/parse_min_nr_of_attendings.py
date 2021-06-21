import json
import random

with open('intentMinNrOfAttendingsRO.json') as intentMinNrOfAttendingsRO:
	intentRO = json.load(intentMinNrOfAttendingsRO)
with open('intentMinNrOfAttendingsEN.json') as intentMinNrOfAttendingsEN:
	intentEN = json.load(intentMinNrOfAttendingsEN)
with open('../../resources/classesFirebase.json') as subjectModel:
	subjects = json.load(subjectModel)
f = open("generatedIntentMinNrOfAttendingsRO.yml", "w")
fEN = open("generatedIntentMinNrOfAttendingsEN.yml", "w")

for i in intentRO:
	for subject in subjects['classes']:
		f.write(i.replace("Ex", subject['name']) + "\n")

for i in intentEN:
	for subject in subjects['classes']:
		fEN.write(i.replace("Ex", subject['name']) + "\n")

for i in intentRO:
	for subject in subjects['classes']:
		f.write(i.replace("Ex", subject['shortname']) + "\n")

for i in intentEN:
	for subject in subjects['classes']:
		fEN.write(i.replace("Ex", subject['shortname']) + "\n")

f.close()
fEN.close()

fShuffle = open("generatedIntentMinNrOfAttendingsROShuffle.yml", "w")
fENShuffle = open("generatedIntentMinNrOfAttendingsENShuffle.yml", "w")
fR = open("generatedIntentMinNrOfAttendingsRO.yml", "r")
fREN = open("generatedIntentMinNrOfAttendingsEN.yml", "r")

linesRO = fR.readlines()
linesEN = fREN.readlines()
random.shuffle(linesRO)
random.shuffle(linesEN)
fShuffle.writelines(linesRO)
fENShuffle.writelines(linesEN)
fShuffle.close()
fENShuffle.close()