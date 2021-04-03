import json
import os

with open('intentGroupLeader.json') as intentGroupLeader:
    intent = json.load(intentGroupLeader)
with open('../../../resources/nrGroup.json') as nrGroupModel:
    nrGroup = json.load(nrGroupModel)
with open('../../../resources/nrSR.json') as nrSRModel:
    nrSR = json.load(nrSRModel)
f = open("generatedIntentGroupLeader.json", "w")

f.write("[" + "\n")
for i in intent:
    for g in nrGroup:
        f.write(f'"' + i.replace("Gx", nrGroup[g]['nameGroup']) + f'",' + "\n")

f.seek(f.tell() - 2, os.SEEK_SET)
f.truncate()
f.write("\n" + "]")
f.close()

with open('generatedIntentGroupLeader.json') as generatedIntentGroupLeader:
    intent = json.load(generatedIntentGroupLeader)
f = open("generatedIntentGroupLeader.yml", "w")

for i in intent:
    for n in nrSR:
        f.write(i.replace("Sx", nrSR[n]['nameSR']) + "\n")

f.close()