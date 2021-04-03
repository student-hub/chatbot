import json
import os

with open('intentSRLeader.json') as intentSRLeader:
    intent = json.load(intentSRLeader)
with open('../../../resources/nrSR.json') as nrSRModel:
    nrSR = json.load(nrSRModel)
f = open("generatedIntentSRLeader.yml", "w")

for i in intent:
    for n in nrSR:
        f.write(i.replace("Sx", nrSR[n]['nameSR']) + "\n")

f.close()