import json
import random
import sys

filename = ''
output_file = ''
if sys.argv[1] == "en":
	print("en")
	filename = "intentEndTimeEventEN.json"
	output_file = "generatedIntentEndTimeEventEN.yml"
else:
	print("ro")
	filename = "intentEndTimeEventRO.json'"
	output_file = "generatedIntentEndTimeEventRO.yml"

f = open(output_file, "w")
f.write("- intent: get_end_time_event\n" + "  " + "examples: |\n")

with open(filename) as intentEndTimeEvent:
	intent = json.load(intentEndTimeEvent)

with open('../../resources/classesFirebase.json') as subjectModel:
	subjects = json.load(subjectModel)

for i in range(int(len(intent) / 2)):
	random_subject = random.choice(subjects['classes'])
	f.write("   " + intent[i].replace("Ex", random_subject['name']) + "\n")

for i in range(int(len(intent) / 2) + 1, len(intent)):
	random_subject = random.choice(subjects['classes'])
	f.write("   " + intent[i].replace("Ex", random_subject['shortname']) + "\n")

f.close()