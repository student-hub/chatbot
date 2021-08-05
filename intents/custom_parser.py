import json
from os import write


def load_from_file(file_name):
    with open(file_name) as file:
        return json.load(file)


def write_replaced_intents(file, raw_intent, data, key_info, replaceable_key, replace_key):
    for entry in raw_intent:
        for subj in data[key_info]:
            file.write(entry.replace(replaceable_key, subj[replace_key]) + "\n")


languages = [
    'RO',
    'EN'
]

intent_relative_path = [
    ['classroom/'],
    [
        'event/date/',
        'event/endTime/',
        'event/grading/',
        'event/locateEvent/',
        'event/minConditions/',
        'event/minNrOfAttendings/',
        'event/startTime/'
    ],
    ['people/student/groupLeader']

]


intent_raw_filename = [
    ['intentLocateClassroom'],
    [
        'intentGetDateEvent',
        'intentEndTimeEvent',
        'intentCourseGrading',
        'intentLocateEvent',
        'intentMinConditions',
        'intentMinNrOfAttendings',
        'intentStartTimeEvent'
    ],
]

database_entry = [
    'classroomsFirebase',
    'classesFirebase',
]



key_info = [
    'classrooms',
    'classes',
]

replacing_key = [
    ['name'],
    ['name', 'shortname'],
]

replaceable_key = [
    'Cx',
    'Ex',
]

for index in range(len(intent_raw_filename)):
    
    data = load_from_file('resources/' + database_entry[index] + '.json')
    for lang in languages:
        for it in range(len(intent_raw_filename[index])): 
            raw_intent = load_from_file(
                intent_relative_path[index][it] + intent_raw_filename[index][it] + lang + '.json')
            write_file = open(intent_relative_path[index][it] + 'generated' +
                intent_raw_filename[index][it].capitalize() + lang + '.yml', "w") 
            for rpl_key in replacing_key[index]:
                write_replaced_intents(write_file, raw_intent, data,
                        key_info[index], replaceable_key[index],
                        rpl_key)
            write_file.close()


    
    


