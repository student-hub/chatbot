# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
import utils
import pandas as pd
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import firebase_admin
from firebase_admin import credentials, firestore, auth
cred = credentials.Certificate("acs-upb-mobile-dev-firebase-adminsdk-mgl5c-9617ffc92e.json")
firebase_admin.initialize_app(cred)
firestore_db = firestore.client()
snapshots = firestore_db.collection(u'users');

class ActionLocateClassroom(Action):

    def name(self) -> Text:
        return "action_locate_classroom"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entity = tracker.latest_message['entities'][0]['value']
        #remove whitespaces from string and make capital letters
        entity = entity.replace(" ", "").upper()
    
        location = utils.getClassroomLocation(entity)
        if(len(location)):
            if(location["floor"] > 0):
                dispatcher.utter_message(text="Sala este locatalizată în " + location["building"] + ", etajul " + str(location["floor"]))
            else:
                dispatcher.utter_message(text="Sala este locatalizată în " + location["building"] + ", la parter")
        else:
            dispatcher.utter_message(text="Sala căutată nu a fost găsită, te rog să verifici dacă ai scris corect")
        return []

class ActionGetDateEvent(Action):

    def name(self) -> Text:
        return "action_get_date_event"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        doc = snapshots.document(u"ceHKuicm86eCv2TVTCFkxKBzZvi2").get().to_dict()
        print(doc)
        message = "Scuze, nu dețin această informație. Te rog verifică daca numele evenimentului este scris corect!"
        id = tracker.current_state()['sender_id']
        classFields = doc["class"]
        event = ""
        eventEntity = ""
        typeEventEntity = ""
        try:
            entity = tracker.latest_message['entities']
            for ent in entity:
                if ent['confidence_entity'] > 0.7:
                    if ent['entity'] == "event":
                        eventEntity = ent['value']
                    if ent['entity'] == "typeEvent":
                        typeEventEntity = ent['value']
        except:
            #if something bad happens
            dispatcher.utter_message(text=message)
            return []
        
        #compute classes name
        event = "L" if classFields[0] == "BSc" else "M"
        words = classFields[3].split('-')
        year = words[0]
        serie = words[1]
        group = classFields[4]
        semigroup = classFields[5]
        event = event + "-A" + year + "-S1"
        if(len(eventEntity) < 6):
            event = event + "-" + eventEntity.upper() + "-" + serie
        else:
            abreviation = ""
            for x in eventEntity.split():
                if x[0].isalpha():
                    abreviation = abreviation + x[0]
            if(eventEntity[-1].isnumeric()):
                abreviation = abreviation + eventEntity[-1]
            event = event + "-" + abreviation.upper() + "-" + serie
        print(event)
        
        events = firestore_db.collection(u'events').get()
        eventFound = False
        another_hour = ""
        another_day = ""
        expectedType = ""

        #if it's not mentioned -> default event - curs
        if len(typeEventEntity) == 0:
            typeEventEntity = "cursul"
        expectedType = utils.getTypeRo(typeEventEntity)

        for e in events:
            currentEvent = e.to_dict()
            if "class" in currentEvent.keys():
                if currentEvent["class"] == event:
                    type = currentEvent["type"]

                    #find day
                    index = currentEvent["rrule"].find("BYDAY=")
                    day = currentEvent["rrule"][(index + 6) : (index + 8)]

                    #timezone
                    temp = pd.Timestamp(currentEvent["start"])
                    hour = temp.hour + 3
                    minute = temp.minute
                    h = str(hour) + str(minute) if minute > 0 else str(hour)
                    if currentEvent["relevance"] is not None:
                        if(expectedType == type):
                            if  ((type == "seminar" and group == currentEvent["relevance"][0])
                                or type == "lecture"
                                or (type == "lab" and (semigroup == currentEvent["relevance"][0] or group == currentEvent["relevance"][0]))):
                                if(eventFound):
                                    message = typeEventEntity.capitalize() + " de " + eventEntity + " are loc " + utils.getDayRo(day) + ", la ora " + h + " și " + utils.getDayRo(another_day) + " la ora " + another_hour
                                    break
                                message = typeEventEntity.capitalize() + " de " + eventEntity + " are loc " + utils.getDayRo(day) + ", la ora " + h
                                another_hour = h
                                another_day = day
                                eventFound = True
        dispatcher.utter_message(text=message) 
        return []

class ActionGetEndTimeEvent(Action):

    def name(self) -> Text:
        return "action_get_end_time_event"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        doc = snapshots.document(u"ceHKuicm86eCv2TVTCFkxKBzZvi2").get().to_dict()
        print(doc)
        message = "Scuze, nu dețin această informație. Te rog verifică daca numele evenimentului este scris corect!"
        id = tracker.current_state()['sender_id']
        classFields = doc["class"]
        event = ""
        eventEntity = ""
        typeEventEntity = ""
        try:
            entity = tracker.latest_message['entities']
            for ent in entity:
                if ent['confidence_entity'] > 0.7:
                    if ent['entity'] == "event":
                        eventEntity = ent['value']
                    if ent['entity'] == "typeEvent":
                        typeEventEntity = ent['value']
        except:
            #if something bad happens
            dispatcher.utter_message(text=message)
            return []
        
        #compute classes name
        event = "L" if classFields[0] == "BSc" else "M"
        words = classFields[3].split('-')
        year = words[0]
        serie = words[1]
        group = classFields[4]
        semigroup = classFields[5]
        event = event + "-A" + year + "-S1"
        if(len(eventEntity) < 6):
            event = event + "-" + eventEntity.upper() + "-" + serie
        else:
            abreviation = ""
            for x in eventEntity.split():
                if x[0].isalpha():
                    abreviation = abreviation + x[0]
            if(eventEntity[-1].isnumeric()):
                abreviation = abreviation + eventEntity[-1]
            event = event + "-" + abreviation.upper() + "-" + serie
        print(event)
        
        events = firestore_db.collection(u'events').get()
        eventFound = False
        another_hour = ""
        another_day = ""
        expectedType = ""
        duration = 2

        #if it's not mentioned -> default event - curs
        if len(typeEventEntity) == 0:
            typeEventEntity = "cursul"
        expectedType = utils.getTypeRo(typeEventEntity)

        for e in events:
            currentEvent = e.to_dict()
            if "class" in currentEvent.keys():
                if currentEvent["class"] == event:
                    type = currentEvent["type"]

                    #find day
                    index = currentEvent["rrule"].find("BYDAY=")
                    day = currentEvent["rrule"][(index + 6) : (index + 8)]

                    #timezone
                    temp = pd.Timestamp(currentEvent["start"])
                    if currentEvent["duration"] is not None:
                        duration = currentEvent["duration"]["hours"]
                    hour = temp.hour + 3 + duration
                    minute = temp.minute
                    h = str(hour) + str(minute) if minute > 0 else str(hour)
                    if currentEvent["relevance"] is not None:
                        if(expectedType == type):
                            if  ((type == "seminar" and group == currentEvent["relevance"][0])
                                or type == "lecture"
                                or (type == "lab" and (semigroup == currentEvent["relevance"][0] or group == currentEvent["relevance"][0]))):
                                if(eventFound):
                                    message = typeEventEntity.capitalize() + " de " + eventEntity + " se termină " + utils.getDayRo(day) + ", la ora " + h + " și " + utils.getDayRo(another_day) + " la ora " + another_hour
                                    break
                                message = typeEventEntity.capitalize() + " de " + eventEntity + " se termină " + utils.getDayRo(day) + ", la ora " + h
                                another_hour = h
                                another_day = day
                                eventFound = True
        dispatcher.utter_message(text=message) 
        return []

class ActionLocateEvent(Action):

    def name(self) -> Text:
        return "action_locate_event"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        doc = snapshots.document(u"ceHKuicm86eCv2TVTCFkxKBzZvi2").get().to_dict()
        print(doc)
        message = "Scuze, nu dețin această informație. Te rog verifică daca numele evenimentului este scris corect!"
        id = tracker.current_state()['sender_id']
        classFields = doc["class"]
        event = ""
        eventEntity = ""
        typeEventEntity = ""
        try:
            entity = tracker.latest_message['entities']
            for ent in entity:
                if ent['confidence_entity'] > 0.7:
                    if ent['entity'] == "event":
                        eventEntity = ent['value']
                    if ent['entity'] == "typeEvent":
                        typeEventEntity = ent['value']
        except:
            #if something bad happens
            dispatcher.utter_message(text=message)
            return []
        
        #compute classes name
        event = "L" if classFields[0] == "BSc" else "M"
        words = classFields[3].split('-')
        year = words[0]
        serie = words[1]
        group = classFields[4]
        semigroup = classFields[5]
        event = event + "-A" + year + "-S1"
        if(len(eventEntity) < 6):
            event = event + "-" + eventEntity.upper() + "-" + serie
        else:
            abreviation = ""
            for x in eventEntity.split():
                if x[0].isalpha():
                    abreviation = abreviation + x[0]
            if(eventEntity[-1].isnumeric()):
                abreviation = abreviation + eventEntity[-1]
            event = event + "-" + abreviation.upper() + "-" + serie
        print(event)
        
        events = firestore_db.collection(u'events').get()
        eventFound = False
        another_day = ""
        expectedType = ""
        location = ""
        another_location =""

        #if it's not mentioned -> default event - curs
        if len(typeEventEntity) == 0:
            typeEventEntity = "cursul"
        expectedType = utils.getTypeRo(typeEventEntity)

        for e in events:
            currentEvent = e.to_dict()
            if "class" in currentEvent.keys():
                if currentEvent["class"] == event:
                    type = currentEvent["type"]

                    #find day
                    index = currentEvent["rrule"].find("BYDAY=")
                    day = currentEvent["rrule"][(index + 6) : (index + 8)]
                    if currentEvent["location"] is not None:
                        location = currentEvent["location"]
                    if currentEvent["relevance"] is not None:
                        if expectedType == type and len(location) > 0:
                            if  ((type == "seminar" and group == currentEvent["relevance"][0])
                                or type == "lecture"
                                or (type == "lab" and (semigroup == currentEvent["relevance"][0] or group == currentEvent["relevance"][0]))):
                                if eventFound and len(another_location):
                                    message = typeEventEntity.capitalize() + " de " + eventEntity + " are loc " + utils.getDayRo(day) + ", în " + location + " și " + utils.getDayRo(another_day) + ", în " + another_location
                                    break
                                message = typeEventEntity.capitalize() + " de " + eventEntity + " are loc " + utils.getDayRo(day) + ", în " + location
                                another_day = day
                                another_location = location
                                eventFound = True
        dispatcher.utter_message(text=message) 
        return []

class ActionGetCourseGrading(Action):

    def name(self) -> Text:
        return "action_get_course_grading"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        doc = snapshots.document(u"ceHKuicm86eCv2TVTCFkxKBzZvi2").get().to_dict()
        print(doc)
        message = "Scuze, nu dețin această informație. Te rog verifică daca numele evenimentului este scris corect!"
        id = tracker.current_state()['sender_id']
        classFields = doc["class"]
        event = ""
        eventEntity = ""
        typeEventEntity = ""
        try:
            entity = tracker.latest_message['entities']
            for ent in entity:
                if ent['confidence_entity'] > 0.7:
                    if ent['entity'] == "event":
                        eventEntity = ent['value']
                    if ent['entity'] == "typeEvent":
                        typeEventEntity = ent['value']
        except:
            #if something bad happens
            dispatcher.utter_message(text=message)
            return []
        
        #compute classes name
        event = "L" if classFields[0] == "BSc" else "M"
        words = classFields[3].split('-')
        year = words[0]
        serie = words[1]
        group = classFields[4]
        semigroup = classFields[5]
        event = event + "-A" + year + "-S1"
        if(len(eventEntity) < 6):
            event = event + "-" + eventEntity.upper() + "-" + serie
        else:
            abreviation = ""
            for x in eventEntity.split():
                if x[0].isalpha():
                    abreviation = abreviation + x[0]
            if(eventEntity[-1].isnumeric()):
                abreviation = abreviation + eventEntity[-1]
            event = event + "-" + abreviation.upper() + "-" + serie
        print(event)
        
        events = firestore_db.collection(u'classes').get()

        #if it's not mentioned -> default event - curs
        if len(typeEventEntity) == 0:
            typeEventEntity = "cursul"
        expectedType = utils.getTypeRo(typeEventEntity)

        for e in events:
            currentEventName = e.id
            currentEvent = e.to_dict()
            if currentEventName == event :
                if "grading" in currentEvent.keys():
                    message = "Punctajul la " + eventEntity + " este: "
                    for grade in currentEvent["grading"]:
                        message = message + grade + ": " + str(currentEvent["grading"][grade]) + "; "
        dispatcher.utter_message(text=message) 
        return []

class ActionGetMinConditions(Action):

    def name(self) -> Text:
        return "action_get_min_conditions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Condițiile minime de promovare pentru...")

        return []

class ActionGetMinNrOfAttendings(Action):

    def name(self) -> Text:
        return "action_get_min_nr_of_attendings"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Numărul minim de prezențe pentru a trece...")

        return []

class ActionGetStartTimeEvent(Action):

    def name(self) -> Text:
        return "action_get_start_time_event"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        doc = snapshots.document(u"ceHKuicm86eCv2TVTCFkxKBzZvi2").get().to_dict()
        print(doc)
        message = "Scuze, nu dețin această informație. Te rog verifică daca numele evenimentului este scris corect!"
        id = tracker.current_state()['sender_id']
        classFields = doc["class"]
        event = ""
        eventEntity = ""
        typeEventEntity = ""
        try:
            entity = tracker.latest_message['entities']
            for ent in entity:
                if ent['confidence_entity'] > 0.7:
                    if ent['entity'] == "event":
                        eventEntity = ent['value']
                    if ent['entity'] == "typeEvent":
                        typeEventEntity = ent['value']
        except:
            #if something bad happens
            dispatcher.utter_message(text=message)
            return []
        
        #compute classes name
        event = "L" if classFields[0] == "BSc" else "M"
        words = classFields[3].split('-')
        year = words[0]
        serie = words[1]
        group = classFields[4]
        semigroup = classFields[5]
        event = event + "-A" + year + "-S1"
        if(len(eventEntity) < 6):
            event = event + "-" + eventEntity.upper() + "-" + serie
        else:
            abreviation = ""
            for x in eventEntity.split():
                if x[0].isalpha():
                    abreviation = abreviation + x[0]
            if(eventEntity[-1].isnumeric()):
                abreviation = abreviation + eventEntity[-1]
            event = event + "-" + abreviation.upper() + "-" + serie
        print(event)
        
        events = firestore_db.collection(u'events').get()
        eventFound = False
        another_hour = ""
        another_day = ""
        expectedType = ""

        #if it's not mentioned -> default event - curs
        if len(typeEventEntity) == 0:
            typeEventEntity = "cursul"
        expectedType = utils.getTypeRo(typeEventEntity)

        for e in events:
            currentEvent = e.to_dict()
            if "class" in currentEvent.keys():
                if currentEvent["class"] == event:
                    type = currentEvent["type"]

                    #find day
                    index = currentEvent["rrule"].find("BYDAY=")
                    day = currentEvent["rrule"][(index + 6) : (index + 8)]

                    #timezone
                    temp = pd.Timestamp(currentEvent["start"])
                    hour = temp.hour + 3
                    minute = temp.minute
                    h = str(hour) + str(minute) if minute > 0 else str(hour)
                    if currentEvent["relevance"] is not None:
                        if(expectedType == type):
                            if  ((type == "seminar" and group == currentEvent["relevance"][0])
                                or type == "lecture"
                                or (type == "lab" and (semigroup == currentEvent["relevance"][0] or group == currentEvent["relevance"][0]))):
                                if(eventFound):
                                    message = typeEventEntity.capitalize() + " de " + eventEntity + " începe la ora " + h + ", " + utils.getDayRo(day) + ", " + "și la ora " + another_hour + ", " + utils.getDayRo(another_day)
                                    break
                                message = typeEventEntity.capitalize() + " de " + eventEntity + " începe la ora " + h + ", " + utils.getDayRo(day)
                                another_hour = h
                                another_day = day
                                eventFound = True
        dispatcher.utter_message(text=message) 
        return []

class ActionGetTeacherName(Action):

    def name(self) -> Text:
        return "action_get_teacher_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Scuze, nu dețin această informație. Te rog verifică daca numele sălii este scris corect!"
        classroomName = ""
        try:
            entity = tracker.latest_message['entities']
            for ent in entity:
                if ent['entity'] == "classroom":
                    classroomName = ent['value']
        except:
            #if something bad happens
            dispatcher.utter_message(text=message)
            return []
        if len(classroomName) > 0:
            #remove whitespaces from string and make capital letters
            classroomName = classroomName.replace(" ", "").upper()

            teacherName = utils.getTeacherName(classroomName)
            print(entity)
            if len(teacherName) > 0:
                message = teacherName + " predă în " + classroomName
        dispatcher.utter_message(text=message)

        return []

class ActionGetGroupLeaderName(Action):

    def name(self) -> Text:
        return "action_get_group_leader_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = "Scuze, nu dețin această informație. Te rog verifică daca numele grupei este corect!"
        srNr = ""
        groupNr = ""
        try:
            entity = tracker.latest_message['entities']
            for ent in entity:
                if ent['confidence_entity'] > 0.7:
                    if ent['entity'] == "groupNr":
                        groupNr = ent['value']
                    if ent['entity'] == "srNr":
                        srNr = ent['value']
        except:
            #if something bad happens
            dispatcher.utter_message(text=message)
            return []
        if len(groupNr) > 0:
            groupName = groupNr + srNr
        else:
            groupName = tracker.latest_message['entities'][0]['value']
        #remove whitespaces from string and make capital letters
        groupName = groupName.replace(" ", "").upper()
        print(groupName)
        groupLeader = utils.getGroupLeader(groupName)
        if len(groupLeader) > 0:
            message = "Șeful de grupă la " + groupName + " este " + groupLeader
        else:
            message = "Scuze!Momentan nu știu cine este șef de grupă la " + groupName
        dispatcher.utter_message(text=message)
        return []

class ActionGetSRLeaderName(Action):

    def name(self) -> Text:
        return "action_get_SR_leader_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        doc = snapshots.document(u"ceHKuicm86eCv2TVTCFkxKBzZvi2").get().to_dict()
        year = doc["class"][3][0]
        print(year)
        message = "Scuze, nu dețin această informație. Te rog verifică daca numele grupei este corect!"
        srNr = ""
        try:
            entity = tracker.latest_message['entities']
            for ent in entity:
                if ent['confidence_entity'] > 0.7:
                    srNr = ent['value']
        except:
            #if something bad happens
            dispatcher.utter_message(text=message)
            return []
        #remove whitespaces from string and make capital letters
        srNr =srNr.replace(" ", "").upper()
        if srNr[0].isalpha():
            srNr = year + "-"+ srNr
        print(srNr)
        srLeader = utils.getSrLeader(srNr)
        if len(srLeader) > 0:
            message = "Șeful de serie la " + srNr + " este " + srLeader
        else:
            message = "Scuze!Momentan nu știu cine este șef de serie la " + srNr
        dispatcher.utter_message(text=message)