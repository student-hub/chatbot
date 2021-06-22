import json
import random

with open('intentLocateEventRO.json') as intentLocateEventRO:
	intentRO = json.load(intentLocateEventRO)
with open('intentLocateEventEN.json') as intentLocateEventEN:
	intentEN = json.load(intentLocateEventEN)
with open('../../resources/classesFirebase.json') as subjectModel:
	subjects = json.load(subjectModel)
f = open("generatedIntentLocateEventRO.yml", "w")
fEN = open("generatedIntentLocateEventEN.yml", "w")

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

#randomize data:

fShuffle = open("generatedIntentLocateEventROShuffle.yml", "w")
fENShuffle = open("generatedIntentLocateEventENShuffle.yml", "w")
fR = open("generatedIntentLocateEventRO.yml", "r")
fREN = open("generatedIntentLocateEventEN.yml", "r")

linesRO = fR.readlines()
linesEN = fREN.readlines()
random.shuffle(linesRO)
random.shuffle(linesEN)
fShuffle.writelines(linesRO)
fENShuffle.writelines(linesEN)
fShuffle.close()
fENShuffle.close()