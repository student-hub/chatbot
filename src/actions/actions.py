# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from multiprocessing import Event
import firebase_admin
import helper

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from firebase_admin import credentials, firestore, auth

from helper import LocateEventInfo
from helper import DateEventInfo

cred = credentials.Certificate("acs-upb-key.json")
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
        message = "Sala căutată nu a fost găsită, te rog să verifici dacă ai scris corect"
    
        location = helper.get_classroom_location(entity)

        if(len(location)):
            if(location["floor"] > 0):
               message = "Sala este locatalizată în " + location["building"] + ", etajul " + str(location["floor"])
            else:
                message = "Sala este locatalizată în " + location["building"] + ", la parter"
        dispatcher.utter_message(message)

        return []

class ActionGetDateEvent(Action):

    def name(self) -> Text:
        return "action_get_date_event"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        message = "Scuze, nu dețin această informație. Te rog verifică daca numele evenimentului este scris corect!"

        id = tracker.current_state()['sender_id']
        doc = snapshots.document(id).get().to_dict()
        classFields = doc["class"]
        sr, group, semigroup = helper.identify_student(classFields)

        entities = tracker.latest_message['entities']
        eventEntity, typeEventEntity = helper.get_entities(entities)

        event = helper.compute_event_name(classFields, eventEntity)
        typeEvent = helper.get_type_event(typeEventEntity)
    
        events = firestore_db.collection(u'events').get()

        results_list = []

        for e in events:
            currentEvent = e.to_dict()
            if "class" in currentEvent.keys():
                if currentEvent["class"] == event and currentEvent["type"] == typeEvent:
                    if currentEvent["relevance"] is not None:
                        for relevance in currentEvent["relevance"]:
                            if (relevance == sr or relevance == group or relevance == semigroup):
                                if currentEvent["rrule"] is not None:
                                    day, hour = helper.get_time(currentEvent)
                                    results_list.append(DateEventInfo(day, hour))

        if len(results_list) >= 2:
            message = typeEventEntity.capitalize() +  + " are loc "
            for info in results_list:
                message += info.day + ", la ora " + info.hour + ","
            message = message[:-1] + '.'
        elif len(results_list) == 1:
            info = results_list[0]
            message =  typeEventEntity.capitalize() + " de " + eventEntity + " are loc " + info.day + ", la ora " + info.hour + "."
        dispatcher.utter_message(text=message) 
        return []

class ActionGetEndTimeEvent(Action):

    def name(self) -> Text:
        return "action_get_end_time_event"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Scuze, nu dețin această informație. Te rog verifică daca numele evenimentului este scris corect!"

        id = tracker.current_state()['sender_id']
        doc = snapshots.document(id).get().to_dict()
        classFields = doc["class"]
        sr, group, semigroup = helper.identify_student(classFields)

        entities = tracker.latest_message['entities']
        eventEntity, typeEventEntity = helper.get_entities(entities)

        event = helper.compute_event_name(classFields, eventEntity)
        typeEvent = helper.get_type_event(typeEventEntity)
    
        events = firestore_db.collection(u'events').get()

        results_list = []

        for e in events:
            currentEvent = e.to_dict()
            if "class" in currentEvent.keys():
                if currentEvent["class"] == event and currentEvent["type"] == typeEvent:
                    if currentEvent["relevance"] is not None:
                        for relevance in currentEvent["relevance"]:
                            if (relevance == sr or relevance == group or relevance == semigroup):
                                if currentEvent["rrule"] is not None:
                                    day, hour = helper.get_end_time(currentEvent)
                                    results_list.append(DateEventInfo(day, hour))

        if len(results_list) >= 2:
            message = typeEventEntity.capitalize() + " de " + eventEntity +  " se termină "
            for info in results_list:
                message += info.day + ", la ora " + info.hour + ","
            message = message[:-1] + '.'
        elif len(results_list) == 1:
            info = results_list[0]
            message = typeEventEntity.capitalize() + " de " + eventEntity +  " se termină " + info.day + ", la ora " + info.hour + "."

        dispatcher.utter_message(text=message) 
        return []

class ActionLocateEvent(Action):

    def name(self) -> Text:
        return "action_locate_event"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Scuze, nu dețin această informație. Te rog verifică daca numele evenimentului este scris corect!"

        id = tracker.current_state()['sender_id']
        doc = snapshots.document(id).get().to_dict()
        classFields = doc["class"]
        sr, group, semigroup = helper.identify_student(classFields)

        entities = tracker.latest_message['entities']
        eventEntity, typeEventEntity = helper.get_entities(entities)

        event = helper.compute_event_name(classFields, eventEntity)
        typeEvent = helper.get_type_event(typeEventEntity)
    
        events = firestore_db.collection(u'events').get()

        results_list = []

        for e in events:
            currentEvent = e.to_dict()
            if "class" in currentEvent.keys():
                if currentEvent["class"] == event and currentEvent["type"] == typeEvent:
                    if currentEvent["relevance"] is not None:
                        for relevance in currentEvent["relevance"]:
                            if (relevance == sr or relevance == group or relevance == semigroup):
                                print(currentEvent["location"])
                                if currentEvent["location"] is not None and currentEvent["rrule"] is not None:
                                    day, hour = helper.get_time(currentEvent)
                                    results_list.append(LocateEventInfo(day, hour, currentEvent["location"]))                          

        if len(results_list) >= 2:
            message = typeEventEntity.capitalize() + " de " + eventEntity + " are loc:" 
            for info in results_list:
                message += info.day + " în sala " + info.location + ", "
            message = message[:-2] + '.'
        elif len(results_list) == 1:
            info = results_list[0]
            message =  typeEventEntity.capitalize() + " de " + eventEntity + " are loc " + info.day + ", în sala " + info.location + " ."

        dispatcher.utter_message(text=message) 
        return []

class ActionGetCourseGrading(Action):

    def name(self) -> Text:
        return "action_get_course_grading"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Scuze, nu dețin această informație. Te rog verifică daca numele evenimentului este scris corect!"
        
        id = tracker.current_state()['sender_id']
        doc = snapshots.document(id).get().to_dict()
        classFields = doc["class"]

        entities = tracker.latest_message['entities']
        eventEntity, typeEventEntity = helper.get_entities(entities)

        event = helper.compute_event_name(classFields, eventEntity)
        typeEvent = helper.get_type_event(typeEventEntity)
    
        events = firestore_db.collection(u'classes').get()

        results_list = []

        for e in events:
            currentEventName = e.id
            currentEvent = e.to_dict()
            if currentEventName == event:
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

        message = "Scuze, încă nu avem date despre condițiile minime de promovare!"

        dispatcher.utter_message(message)

        return []

class ActionGetMinNrOfAttendings(Action):

    def name(self) -> Text:
        return "action_get_min_nr_of_attendings"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Scuze, încă nu avem date despre numărul minim de prezențe la materii!"

        dispatcher.utter_message(message)

        return []

class ActionGetStartTimeEvent(Action):

    def name(self) -> Text:
        return "action_get_start_time_event"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Scuze, nu dețin această informație. Te rog verifică daca numele evenimentului este scris corect!"
        
        id = tracker.current_state()['sender_id']
        doc = snapshots.document(id).get().to_dict()
        classFields = doc["class"]
        sr, group, semigroup = helper.identify_student(classFields)

        entities = tracker.latest_message['entities']
        eventEntity, typeEventEntity = helper.get_entities(entities)

        event = helper.compute_event_name(classFields, eventEntity)
        typeEvent = helper.get_type_event(typeEventEntity)
    
        events = firestore_db.collection(u'events').get()

        results_list = []

        for e in events:
            currentEvent = e.to_dict()
            if "class" in currentEvent.keys():
                if currentEvent["class"] == event and currentEvent["type"] == typeEvent:
                    if currentEvent["relevance"] is not None:
                        for relevance in currentEvent["relevance"]:
                            if (relevance == sr or relevance == group or relevance == semigroup):
                                if currentEvent["rrule"] is not None:
                                    day, hour = helper.get_time(currentEvent)
                                    results_list.append(DateEventInfo(day, hour))
                                
        if len(results_list) >= 2:
            message = typeEventEntity.capitalize() + " de " + eventEntity + " începe: "
            for info in results_list:
                message += info.day + ", la ora " + info.hour + ", "
            message = message[:-2] + '.'
        elif len(results_list) == 1:
            info = results_list[0]
            message =  typeEventEntity.capitalize() + " de " + eventEntity + " începe la ora " + info.hour + ", " + info.day + '.'

        dispatcher.utter_message(text=message) 
        return []

class ActionGetTeacherName(Action):

    def name(self) -> Text:
        return "action_get_teacher_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Scuze! Momentan nu deținem informațiile despre sălile ocupate de profesorii din facultate! :("
        dispatcher.utter_message(text=message)

        return []

class ActionGetGroupLeaderName(Action):

    def name(self) -> Text:
        return "action_get_group_leader_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Scuze! Momentan nu deținem informațiile despre șefii de grupă din facultate! :("

        dispatcher.utter_message(text=message)
        return []

class ActionGetSRLeaderName(Action):

    def name(self) -> Text:
        return "action_get_SR_leader_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Scuze! Momentan nu deținem informațiile despre șefii de serie din facultate! :("

        dispatcher.utter_message(text=message)