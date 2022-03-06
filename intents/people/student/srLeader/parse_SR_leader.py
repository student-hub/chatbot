import json
import random
import sys

filename = ''
output_file = ''
if sys.argv[1] == "en":
	filename = "intentSRLeaderEN.json"
	output_file = "generatedIntentSRLeaderEN.yml"
else:
	filename = "intentSRLeaderRO.json"
	output_file = "generatedIntentSRLeaderRO.yml"

f = open(output_file, "w")
f.write("- intent: get_SR_leader_name\n" + "  " + "examples: |\n")

with open(filename) as intentSRLeader:
    intent = json.load(intentSRLeader)
with open('../../../resources/nrSR.json') as nrSRModel:
    nrSR = json.load(nrSRModel)

for i in intent:
    random_nrSR = random.choice(list(nrSR.values()))
    f.write("   "  + i.replace("Sx", random_nrSR['nameSR']) + "\n")


f.close()
