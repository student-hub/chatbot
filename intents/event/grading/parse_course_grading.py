import json
import random
import sys

filename = ''
output_file = ''
if sys.argv[1] == "en":
	print("en")
	filename = "intentCourseGradingEN.json"
	output_file = "generatedIntentCourseGradingEN.yml"
else:
	print("ro")
	filename = "intentCourseGradingRO.json"
	output_file = "generatedIntentCourseGradingRO.yml"

f = open(output_file, "w")
f.write("- intent: get_course_grading\n" + "  " + "examples: |\n")

with open(filename) as intentCourseGrading:
	intent = json.load(intentCourseGrading)

with open('../../resources/classesFirebase.json') as subjectModel:
	subjects = json.load(subjectModel)

for i in range(int(len(intent) / 2)):
	random_subject = random.choice(subjects['classes'])
	f.write("   " + intent[i].replace("Ex", random_subject['name']) + "\n")

for i in range(int(len(intent) / 2) + 1, len(intent)):
	random_subject = random.choice(subjects['classes'])
	f.write("   " + intent[i].replace("Ex", random_subject['shortname']) + "\n")

f.close()
