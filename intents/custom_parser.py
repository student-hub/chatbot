import json
import os

def load_from_file(file_name):
    with open(file_name) as file:
        return json.load(file)

def convertJsonToWYaml(json_file, yaml_file):
    js = json.load(json_file)
    for entry in js:
        yaml_file.write(entry + "\n")
    

def write_replaced_intents(file, raw_intent, data, pair):
    file.write("[" + "\n")
    for entry in raw_intent:       
        for name in data:
            if not isinstance(data[name], list):
                data[name] = [data[name]]
            for subj in data[name]:
                file.write(f'"' + entry.replace(pair[0], subj[pair[1]]) + f'",'+ "\n")
    file.seek(file.tell() - 2, os.SEEK_SET)
    file.truncate()
    file.write("\n" + "]")

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
    ['people/student/groupLeader/'],
    ['people/student/srLeader/'],
    ['people/teacher/']

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
    ['intentGroupLeader'],
    ['intentSRLeader'],
    ['intentGetTeacherName']

]

clear_files(intent_raw_filename, intent_relative_path, languages)

database_entry = [
    ['classroomsFirebase'],
    ['classesFirebase'],
    ['classesFirebase'],
    ['nrGroup', 'nrSR'],
    ['nrSR'],
    ['classroomsFirebase']
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
    },

    {
        'Sx' : 'nameSR'
    },
    {
        'Cx' : 'name'
    }

]

for index in range(len(intent_raw_filename)):
    
   
    for lang in languages:
        for it in range(len(intent_raw_filename[index])): 
            path = intent_relative_path[index][it] + intent_raw_filename[index][it] + lang + '.json'
            raw_intent = load_from_file(path)          
            path = 'temp.json'
            for (key, value), database_name in zip(replacing_dict[index].items(), database_entry[index]):
                data = load_from_file('./resources/' + database_name + '.json')           
                temp_file = open("temp.json", "w")             
                write_replaced_intents(temp_file, raw_intent, data, (key, value))
                temp_file.close()
                raw_intent = load_from_file(path)
                
                

            write_file = open(intent_relative_path[index][it] + 'generated' +
                intent_raw_filename[index][it].capitalize() + lang + '.yml', "w")
            temp_file = open("temp.json")
            convertJsonToWYaml(temp_file, write_file)
            write_file.close()


    



