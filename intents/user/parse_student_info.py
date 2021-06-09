import json
import os

with open('intentInitStudentInfoRO.json') as intentInitStudentInfoRO:
    intentRO = json.load(intentInitStudentInfoRO)
with open('intentInitStudentInfoEN.json') as intentInitStudentInfoEN:
    intentEN = json.load(intentInitStudentInfoEN)
with open('../../../resources/nrSR.json') as nrSRModel:
    nrSR = json.load(nrSRModel)
f = open("generatedIntentInitStudentInfoRO.yml", "w")
fEN = open("generatedIntentInitStudentInfoEN.yml", "w")

for i in intentRO:
    for n in nrSR:
        f.write(i.replace("Sx", nrSR[n]['nameSR']) + "\n")

for i in intentEN:
    for n in nrSR:
        fEN.write(i.replace("Sx", nrSR[n]['nameSR']) + "\n")

f.close()
fEN.close()