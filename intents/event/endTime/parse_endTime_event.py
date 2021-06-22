import json
import random

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
		
for i in intentRO:
	for subject in subjects['classes']:
		f.write(i.replace("Ex", subject['shortname']) + "\n")

for i in intentEN:
	for subject in subjects['classes']:
		fEN.write(i.replace("Ex", subject['shortname']) + "\n")
f.close()
fEN.close()

#randomize data:

fShuffle = open("generatedIntentEndTimeEventROShuffle.yml", "w")
fENShuffle = open("generatedIntentEndTimeEventENShuffle.yml", "w")
fR = open("generatedIntentEndTimeEventRO.yml", "r")
fREN = open("generatedIntentEndTimeEventEN.yml", "r")

linesRO = fR.readlines()
linesEN = fREN.readlines()
random.shuffle(linesRO)
random.shuffle(linesEN)
fShuffle.writelines(linesRO)
fENShuffle.writelines(linesEN)
fShuffle.close()
fENShuffle.close()