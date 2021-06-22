import json
import random

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

for i in intentRO:
	for subject in subjects['classes']:
		f.write(i.replace("Ex", subject['shortname']) + "\n")

for i in intentEN:
	for subject in subjects['classes']:
		fEN.write(i.replace("Ex", subject['shortname']) + "\n")

f.close()
fEN.close()

fShuffle = open("generatedIntentMinConditionsROShuffle.yml", "w")
fENShuffle = open("generatedIntentMinConditionsENShuffle.yml", "w")
fR = open("generatedIntentMinConditionsRO.yml", "r")
fREN = open("generatedIntentMinConditionsEN.yml", "r")

linesRO = fR.readlines()
linesEN = fREN.readlines()
random.shuffle(linesRO)
random.shuffle(linesEN)
fShuffle.writelines(linesRO)
fENShuffle.writelines(linesEN)
fShuffle.close()
fENShuffle.close()

