import json
import random

with open('intentCourseGradingRO.json') as intentCourseGradingRO:
	intentRO = json.load(intentCourseGradingRO)
with open('intentCourseGradingEN.json') as intentCourseGradingEN:
	intentEN = json.load(intentCourseGradingEN)
with open('../../resources/classesFirebase.json') as subjectModel:
	subjects = json.load(subjectModel)
f = open("generatedIntentCourseGradingRO.yml", "w")
fEN = open("generatedIntentCourseGradingEN.yml", "w")

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

fShuffle = open("generatedIntentCourseGradingROShuffle.yml", "w")
fENShuffle = open("generatedIntentCourseGradingENShuffle.yml", "w")
fR = open("generatedIntentCourseGradingRO.yml", "r")
fREN = open("generatedIntentCourseGradingEN.yml", "r")

linesRO = fR.readlines()
linesEN = fREN.readlines()
random.shuffle(linesRO)
random.shuffle(linesEN)
fShuffle.writelines(linesRO)
fENShuffle.writelines(linesEN)
fShuffle.close()
fENShuffle.close()

