import json
import random
import sys

filename = ''
output_file = ''
if sys.argv[1] == "en":
	print("en")
	filename = "intentLocateClassroomEN.json"
	output_file = "generatedIntentLocateClassroomEN.yml"
else:
	print("ro")
	filename = "intentLocateClassroomRO.json"
	output_file = "generatedIntentLocateClassroomRO.yml"


f = open(output_file, "w")
f.write("- intent: locate_classroom\n" + "  " + "examples: |\n")

with open(filename) as intentLocateClassroom:
	intent = json.load(intentLocateClassroom)
with open('../resources/classroomsFirebase.json') as classroomModel:
	classroom = json.load(classroomModel)

for i in intent:
	random_classroom = random.choice(classroom["classrooms"])
	f.write("   " + i.replace("Cx", random_classroom['name']) + "\n")

f.write("- lookup: classroom\n" + "  " + "examples: |\n")
for c in classroom["classrooms"]:
	f.write("   -" + c['name'] + "\n")

f.close()
