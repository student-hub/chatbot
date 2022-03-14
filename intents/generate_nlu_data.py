import sys
import ruamel.yaml
import os

def dump_intent(file_path, nlu_file):
    with open(file_path, 'r') as intent_faq:
        intent = yaml.load(intent_faq)
        yaml.dump(intent, nlu_file)

nlu_file = open("nlu_data.yml", "w")
nlu_file.write("version: '3.0'\n")
nlu_file.write("nlu:\n")

path = ''
yaml = ruamel.yaml.YAML()

if sys.argv[1] == "en":
    path = "faq\en"
else:
    path = "faq\\ro"

for faq_file in os.listdir(path):
    if faq_file.endswith(".yml"):
        file_path = f"{path}\{faq_file}"
        dump_intent(file_path, nlu_file)
       

dump_intent("./generatedIntents.yml", nlu_file)
nlu_file.close()