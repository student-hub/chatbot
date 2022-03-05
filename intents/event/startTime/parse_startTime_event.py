import json
import random
import sys

filename = ''
output_file = ''
if sys.argv[1] == "en":
	print("en")
	filename = "intentStartTimeEventEN.json"
	output_file = "generatedIntentStartTimeEventEN.yml"
else:
	print("ro")
	filename = "intentStartTimeEventRO.json'"
	output_file = "generatedIntentStartTimeEventRO.yml"

f = open(output_file, "w")
f.write("- intent: get_start_time_event\n" + "  " + "examples: |\n")

with open(filename) as intentStartTimeEvent:
	intent = json.load(intentStartTimeEvent)

with open('../../resources/classesFirebase.json') as subjectModel:
	subjects = json.load(subjectModel)

for i in range(int(len(intent) / 2)):
	random_subject = random.choice(subjects['classes'])
	f.write("   " + intent[i].replace("Ex", random_subject['name']) + "\n")

for i in range(int(len(intent) / 2) + 1, len(intent)):
	random_subject = random.choice(subjects['classes'])
	f.write("   " + intent[i].replace("Ex", random_subject['shortname']) + "\n")

f.close()