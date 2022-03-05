import json
import random
import sys

filename = ''
output_file = ''
if sys.argv[1] == "en":
	print("en")
	filename = "intentGetDateEventEN.json"
	output_file = "generatedIntentGetDateEventEN.yml"
else:
	print("ro")
	filename = "intentGetDateEventRO.json"
	output_file = "generatedIntentGetDateEventRO.yml"

f = open(output_file, "w")
f.write("- intent: get_date_event\n" + "  " + "examples: |\n")

with open(filename) as intentGetDateEvent:
	intent = json.load(intentGetDateEvent)

with open('../../resources/classesFirebase.json') as subjectModel:
	subjects = json.load(subjectModel)

for i in range(int(len(intent) / 2)):
	random_subject = random.choice(subjects['classes'])
	f.write("   " + intent[i].replace("Ex", random_subject['name']) + "\n")

for i in range(int(len(intent) / 2) + 1, len(intent)):
	random_subject = random.choice(subjects['classes'])
	f.write("   " + intent[i].replace("Ex", random_subject['shortname']) + "\n")

f.write("- lookup: event\n" + "  " + "examples: |\n")
for subject in subjects['classes']:
	f.write("   -" + subject['name'] + "\n")
	f.write("   -" + subject['shortname'] + "\n")

f.close()