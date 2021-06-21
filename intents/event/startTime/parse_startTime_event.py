import json
import random

with open('intentStartTimeEventRO.json') as intentStartTimeEventRO:
	intentRO = json.load(intentStartTimeEventRO)
with open('intentStartTimeEventEN.json') as intentStartTimeEventEN:
	intentEN = json.load(intentStartTimeEventEN)
with open('../../resources/classesFirebase.json') as subjectModel:
	subjects = json.load(subjectModel)
f = open("generatedIntentStartTimeEventRO.yml", "w")
fEN = open("generatedIntentStartTimeEventEN.yml", "w")

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

fShuffle = open("generatedIntentStartTimeEventROShuffle.yml", "w")
fENShuffle = open("generatedIntentStartTimeEventENShuffle.yml", "w")
fR = open("generatedIntentStartTimeEventRO.yml", "r")
fREN = open("generatedIntentStartTimeEventEN.yml", "r")

linesRO = fR.readlines()
linesEN = fREN.readlines()
random.shuffle(linesRO)
random.shuffle(linesEN)
fShuffle.writelines(linesRO)
fENShuffle.writelines(linesEN)
fShuffle.close()
fENShuffle.close()