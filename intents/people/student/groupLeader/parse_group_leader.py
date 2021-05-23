import json
import os

with open('intentGroupLeaderRO.json') as intentGroupLeaderRO:
    intentRO = json.load(intentGroupLeaderRO)
with open('intentGroupLeaderEN.json') as intentGroupLeaderEN:
    intentEN = json.load(intentGroupLeaderEN)
with open('../../../resources/nrGroup.json') as nrGroupModel:
    nrGroup = json.load(nrGroupModel)
with open('../../../resources/nrSR.json') as nrSRModel:
    nrSR = json.load(nrSRModel)
f = open("generatedIntentGroupLeaderRO.json", "w")
fEN = open("generatedIntentGroupLeaderEN.json", "w")

f.write("[" + "\n")
for i in intentRO:
    for g in nrGroup:
        f.write(f'"' + i.replace("Gx", nrGroup[g]['nameGroup']) + f'",' + "\n")

f.seek(f.tell() - 2, os.SEEK_SET)
f.truncate()
f.write("\n" + "]")
f.close()

fEN.write("[" + "\n")
for i in intentEN:
    for g in nrGroup:
        fEN.write(f'"' + i.replace("Gx", nrGroup[g]['nameGroup']) + f'",' + "\n")

fEN.seek(fEN.tell() - 2, os.SEEK_SET)
fEN.truncate()
fEN.write("\n" + "]")
fEN.close()

with open('generatedIntentGroupLeaderRO.json') as generatedIntentGroupLeaderRO:
    intentRO = json.load(generatedIntentGroupLeaderRO)
f = open("generatedIntentGroupLeaderRO.yml", "w")

with open('generatedIntentGroupLeaderEN.json') as generatedIntentGroupLeaderEN:
    intentEN = json.load(generatedIntentGroupLeaderEN)
fEN = open("generatedIntentGroupLeaderEN.yml", "w")

for i in intentRO:
    for n in nrSR:
        f.write(i.replace("Sx", nrSR[n]['nameSR']) + "\n")

for i in intentEN:
    for n in nrSR:
        fEN.write(i.replace("Sx", nrSR[n]['nameSR']) + "\n")

f.close()
fEN.close()