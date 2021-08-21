import json
from os import write
import shutil

def load_from_file(file_name):
    with open(file_name) as file:
        return json.load(file)


def write_replaced_intents(file, raw_intent, data, pair):
    for entry in raw_intent:       
        for name in data:
            if not isinstance(data[name], list):
                data[name] = [data[name]]
            for subj in data[name]:
                file.write(entry.replace(pair[0], subj[pair[1]]) + "\n")

def clear_files(intent_raw_filename, intent_relative_pat, languages):

    for index in range(len(intent_raw_filename)):
        for lang in languages:
            for it in range(len(intent_raw_filename[index])): 
                open(intent_relative_path[index][it] + 'generated' +
                    intent_raw_filename[index][it].capitalize() + lang + '.yml', "w").close()



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
    [
        'event/date/',
        'event/endTime/',
        'event/grading/',
        'event/locateEvent/',
        'event/minConditions/',
        'event/minNrOfAttendings/',
        'event/startTime/'
    ],
    ['people/student/groupLeader/']

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
    [
        'intentGetDateEvent',
        'intentEndTimeEvent',
        'intentCourseGrading',
        'intentLocateEvent',
        'intentMinConditions',
        'intentMinNrOfAttendings',
        'intentStartTimeEvent'
    ],
    ['intentGroupLeader']

]

clear_files(intent_raw_filename, intent_relative_path, languages)

database_entry = [
    ['classroomsFirebase'],
    ['classesFirebase'],
    ['classesFirebase'],
    ['nrGroup', 'nrSR']
]

replacing_dict = [
    {
        'Cx' : 'name'
    },

    {
        'Ex' : 'name',
    },

    {
        'Ex' : 'shortname'
    },

    {
        'Gx' : 'nameGroup',
        'Sx' : 'nameSR',
    }

]

#to do: generate the intermediary file as json

for index in range(len(intent_raw_filename)):
    
   
    for lang in languages:
        for it in range(len(intent_raw_filename[index])): 
            path = intent_relative_path[index][it] + intent_raw_filename[index][it] + lang + '.json'
            for (key, value), database_name in zip(replacing_dict[index].items(), database_entry[index]):
                data = load_from_file('./resources/' + database_name + '.json')
                if(database_name == 'nrSR'):
                    print("here")
                raw_intent = load_from_file(path)
                if(database_name == 'nrSR'):
                    print("here")
                write_file = open(intent_relative_path[index][it] + 'generated' +
                intent_raw_filename[index][it].capitalize() + lang + '.yml', "a")
                write_replaced_intents(write_file, raw_intent, data, (key, value))
                path = intent_relative_path[index][it] + 'generated' + \
                    intent_raw_filename[index][it].capitalize() + lang + '.yml'
            write_file.close()


    



