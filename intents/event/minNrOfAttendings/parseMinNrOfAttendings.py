import json

with open('intentMinNrOfAttendings.json') as intentMinNrOfAttendings:
	intent = json.load(intentMinNrOfAttendings)
with open('../../resources/classes.json') as subjectModel:
	subjects = json.load(subjectModel)
f = open("generatedIntentMinNrOfAttendings.yml", "w")

for i in intent:
	for subject in subjects:
		f.write(i.replace("Ex", subject) + "\n")
		f.write(i.replace("Ex", subjects[subject]['name']) + "\n")

f.close()