import json
import random
import sys

filename = ''
output_file = ''
if sys.argv[1] == "en":
	filename = "intentGroupLeaderEN.json"
	output_file = "generatedIntentGroupLeaderEN.yml"
else:
	filename = "intentGroupLeaderRO.json"
	output_file = "generatedIntentGroupLeaderRO.yml"

f = open(output_file, "w")
f.write("- intent: get_group_leader_name\n" + "  " + "examples: |\n")

with open(filename) as intentGroupLeaderName:
	intent = json.load(intentGroupLeaderName)
with open('../../../resources/nrGroup.json') as nrGroupModel:
    nrGroup = json.load(nrGroupModel)
with open('../../../resources/nrSR.json') as nrSRModel:
    nrSR = json.load(nrSRModel)

for i in intent:
    random_nrGroup = random.choice(list(nrGroup.values()))
    random_nrSR = random.choice(list(nrSR.values()))
    i = i.replace("Gx", random_nrGroup['nameGroup'])
    f.write("   "  + i.replace("Sx", random_nrSR['nameSR']) + "\n")

f.write("- lookup: groupNr\n" + "  " + "examples: |\n")
for idx in nrGroup:
	f.write("   -" + nrGroup[idx]['nameGroup'] + "\n")

f.write("- lookup: srNr\n" + "  " + "examples: |\n")
for idx in nrSR:
	f.write("   -" + nrSR[idx]['nameSR'] + "\n")

f.close()
