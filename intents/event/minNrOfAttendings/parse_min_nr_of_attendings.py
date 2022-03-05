import json
import random
import sys

filename = ''
output_file = ''
if sys.argv[1] == "en":
	print("en")
	filename = "intentMinNrOfAttendingsEN.json"
	output_file = "generatedIntentMinNrOfAttendingsEN.yml"
else:
	print("ro")
	filename = "intentMinNrOfAttendingsRO.json"
	output_file = "generatedIntentMinNrOfAttendingsRO.yml"

f = open(output_file, "w")
f.write("- intent: get_min_nr_of_attendings\n" + "  " + "examples: |\n")

with open(filename) as intentMinNrOfAttendings:
	intent = json.load(intentMinNrOfAttendings)

with open('../../resources/classesFirebase.json') as subjectModel:
	subjects = json.load(subjectModel)

for i in range(int(len(intent) / 2)):
	random_subject = random.choice(subjects['classes'])
	f.write("   " + intent[i].replace("Ex", random_subject['name']) + "\n")

for i in range(int(len(intent) / 2) + 1, len(intent)):
	random_subject = random.choice(subjects['classes'])
	f.write("   " + intent[i].replace("Ex", random_subject['shortname']) + "\n")

f.close()
