import json
import os

with open('intentSRLeaderRO.json') as intentSRLeaderRO:
    intentRO = json.load(intentSRLeaderRO)
with open('intentSRLeaderEN.json') as intentSRLeaderEN:
    intentEN = json.load(intentSRLeaderEN)
with open('../../../resources/nrSR.json') as nrSRModel:
    nrSR = json.load(nrSRModel)
f = open("generatedIntentSRLeaderRO.yml", "w")
fEN = open("generatedIntentSRLeaderEN.yml", "w")

for i in intentRO:
    for n in nrSR:
        f.write(i.replace("Sx", nrSR[n]['nameSR']) + "\n")

for i in intentEN:
    for n in nrSR:
        fEN.write(i.replace("Sx", nrSR[n]['nameSR']) + "\n")

f.close()
fEN.close()