import json
import random
import sys

filename = ''
output_file = ''
if sys.argv[1] == "en":
	print("en")
	filename = "intentGetTeacherNameEN.json"
	output_file = "generatedIntentGetTeacherNameEN.yml"
else:
	print("ro")
	filename = "intentGetTeacherNameRO.json"
	output_file = "generatedIntentGetTeacherNameRO.yml"

f = open(output_file, "w")
f.write("- intent: get_teacher_name\n" + "  " + "examples: |\n")

with open(filename) as intentSearchTeacher:
	intent = json.load(intentSearchTeacher)

with open('../../resources/classroomsFirebase.json') as classroomModel:
	classroom = json.load(classroomModel)

for i in intent:
	random_classroom = random.choice(classroom["classrooms"])
	f.write("   " + i.replace("Cx", random_classroom['name']) + "\n")

f.close()
