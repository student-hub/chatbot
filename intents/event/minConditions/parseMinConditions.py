import json

with open('intentMinConditions.json') as intentMinConditions:
	intent = json.load(intentMinConditions)
with open('../../resources/classes.json') as subjectModel:
	subjects = json.load(subjectModel)
f = open("generatedIntentMinConditions.yml", "w")

for i in intent:
	for subject in subjects:
		f.write(i.replace("Ex", subject) + "\n")
		f.write(i.replace("Ex", subjects[subject]['name']) + "\n")

f.close()