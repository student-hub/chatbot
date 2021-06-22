import json
import random

with open('intentGetDateEventRO.json') as intentGetDateEventRO:
	intentRO = json.load(intentGetDateEventRO)
with open('intentGetDateEventEN.json') as intentGetDateEventEN:
	intentEN = json.load(intentGetDateEventEN)
with open('../../resources/classesFirebase.json') as subjectModel:
	subjects = json.load(subjectModel)
f = open("generatedIntentGetDateEventRO.yml", "w")
fEN = open("generatedIntentGetDateEventEN.yml", "w")

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

fShuffle = open("generatedIntentGetDateEventROShuffle.yml", "w")
fENShuffle = open("generatedIntentGetDateEventENShuffle.yml", "w")
fR = open("generatedIntentGetDateEventRO.yml", "r")
fREN = open("generatedIntentGetDateEventEN.yml", "r")

linesRO = fR.readlines()
linesEN = fREN.readlines()
random.shuffle(linesRO)
random.shuffle(linesEN)
fShuffle.writelines(linesRO)
fENShuffle.writelines(linesEN)
fShuffle.close()
fENShuffle.close()