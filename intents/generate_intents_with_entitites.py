import json
import random
import os
import sys

f = open("generatedIntents.yml", "w")
with open('resources/classroomsFirebase.json') as classroomModel:
	classroom = json.load(classroomModel)
with open('resources/classesFirebase.json') as subjectModel:
	subjects = json.load(subjectModel)
with open('resources/nrGroup.json') as nrGroupModel:
    nrGroup = json.load(nrGroupModel)
with open('resources/nrSR.json') as nrSRModel:
    nrSR = json.load(nrSRModel)

if sys.argv[1] == "en":
	path = "data\en"
else:
	path = "data\\ro"

for intent_file in os.listdir(path):
    print(intent_file)
    f_name, f_ext = os.path.splitext(intent_file)
    f.write("- intent: " + f_name + "\n" + "  " + "examples: |\n")

    with open(path + "/" + intent_file) as intent_json:
	    intent = json.load(intent_json)
        
    length = len(intent)
    intent_with_events = False
    random_list = []

    if (f_name == "locate_classroom" or f_name == "get_teacher_name"):
        random_list = classroom["classrooms"]
        ent_name = "Cx"
        resource = "name"
    elif (f_name == "get_SR_leader_name" or f_name == "get_group_leader_name"):
        random_list = list(nrSR.values())
        ent_name = "Sx"
        resource = "nameSR"
    else:
        intent_with_events = True
        random_list = subjects['classes']
        ent_name = "Ex"
        resource = "name"
        length = int(len(intent) / 2)

    for i in range(length):
        random_entity = random.choice(random_list)
        intent[i] = intent[i].replace(ent_name, random_entity[resource])
        if (f_name == "get_group_leader_name"):
            random_nrGroup = random.choice(list(nrGroup.values()))
            intent[i] = intent[i].replace("Gx", random_nrGroup['nameGroup'])
        f.write("   " + intent[i] + "\n")

    if (intent_with_events == True):
        for i in range(length + 1, len(intent)):
            f.write("   " + intent[i].replace("Ex", random_entity['shortname']) + "\n")

f.write("- lookup: classroom\n" + "  " + "examples: |\n")
for c in classroom["classrooms"]:
	f.write("   -" + c['name'] + "\n")

f.write("- lookup: event\n" + "  " + "examples: |\n")
for subject in subjects['classes']:
	f.write("   -" + subject['name'] + "\n")
	f.write("   -" + subject['shortname'] + "\n")

f.write("- lookup: groupNr\n" + "  " + "examples: |\n")
for idx in nrGroup:
	f.write("   -" + nrGroup[idx]['nameGroup'] + "\n")

f.write("- lookup: srNr\n" + "  " + "examples: |\n")
for idx in nrSR:
	f.write("   -" + nrSR[idx]['nameSR'] + "\n")