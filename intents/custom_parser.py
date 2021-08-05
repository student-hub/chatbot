import json
from os import write


def load_from_file(file_name):
    with open(file_name) as file:
        return json.load(file)


def write_replaced_intents(file, raw_intent, data, key_info, replaceable_key, replace_key):
    for entry in raw_intent:
        for subj in data[key_info]:
            file.write(entry.replace(replaceable_key, subj[replace_key]) + "\n")

def main():

    languages = [
        'RO',
        'EN'
    ]

    intent_raw_filename = [
        'intentLocateClassroom'
    ]

    intent_replaced_filename = [
        'generatedIntentLocateClassroom',
    ]

    database_entry = [
        '../resources/classroomsFirebase.json'
    ]

    key_info = [
        'classrooms',
    ]

    replacing_key = [
        'name',
    ]

    replaceable_key = [
        'Cx',
    ]

    for index in range(len(intent_raw_filename)):
        for lang in languages:
            raw_intent = load_from_file(intent_raw_filename[index] + lang + '.json')
            write_file = open(intent_replaced_filename[index] + lang + '.yml') 
            data = load_from_file(database_entry[index])
            write_replaced_intents(write_file, raw_intent, data,
                    key_info[index], replaceable_key[index],
                    replacing_key[index])
            write_file.close()


    
    


