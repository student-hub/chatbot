# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
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
  
        dispatcher.utter_message(text="Sorry, I don't have the necessary information.")

        return []

class ActionGetDateEvent(Action):

    def name(self) -> Text:
        return "action_get_date_event"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Sorry, I did not understand. Please repeat the question and check the name of the event!"

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
                if currentEvent["class"] == event and currentEvent["type"] == typeEvent and currentEvent["calendar"] == "2021":
                    if currentEvent["relevance"] is not None:
                        for relevance in currentEvent["relevance"]:
                            if (relevance == sr or relevance == group or relevance == semigroup):
                                if currentEvent["rrule"] is not None:
                                    day, hour = helper.get_time(currentEvent)
                                    results_list.append(DateEventInfo(day, hour))
                                
        if len(results_list) >= 2:
            message = "The " + eventEntity + " " + typeEventEntity +  " takes place:"
            for info in results_list:
                message += " on " + info.day + ", at " + info.hour + ","
            message = message[:-1] + '.'
        elif len(results_list) == 1:
            info = results_list[0]
            message = "The " + eventEntity + " " + typeEventEntity +  " takes place on " + info.day + " at " + info.hour + "."
        
        dispatcher.utter_message(text=message)

        return []

class ActionGetEndTimeEvent(Action):

    def name(self) -> Text:
        return "action_get_end_time_event"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Sorry, I did not understand. Please repeat the question and check the name of the event!"

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
                if currentEvent["class"] == event and currentEvent["type"] == typeEvent and currentEvent["calendar"] == "2021":
                    if currentEvent["relevance"] is not None:
                        for relevance in currentEvent["relevance"]:
                            if (relevance == sr or relevance == group or relevance == semigroup):
                                if currentEvent["rrule"] is not None:
                                    day, hour = helper.get_end_time(currentEvent)
                                    results_list.append(DateEventInfo(day, hour))
                                
        if len(results_list) >= 2:
            message = "The " + eventEntity + " " + typeEventEntity +  " ends:"
            for info in results_list:
                message += " at " + info.hour + ", on " + info.day + ","
            message = message[:-1] + '.'
        elif len(results_list) == 1:
            info = results_list[0]
            message = "The " + eventEntity + " " + typeEventEntity +  " ends at " + info.hour + " on " + info.day + "."

        dispatcher.utter_message(text=message)

        return []

class ActionLocateEvent(Action):

    def name(self) -> Text:
        return "action_locate_event"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        message = "Sorry, I did not understand. Please repeat the question and check the name of the event!"

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
                if currentEvent["class"] == event and currentEvent["type"] == typeEvent and currentEvent["calendar"] == "2021":
                    if currentEvent["relevance"] is not None:
                        for relevance in currentEvent["relevance"]:
                            if (relevance == sr or relevance == group or relevance == semigroup):
                                if currentEvent["location"] is not None and len(currentEvent["location"]) and currentEvent["rrule"] is not None:
                                    day, hour = helper.get_time(currentEvent)
                                    results_list.append(LocateEventInfo(day, hour, currentEvent["location"]))                          

        if len(results_list) >= 2:
            message = "The " + eventEntity + " " + typeEventEntity +  " takes place:"
            for info in results_list:
                message += " on " + info.day + ", at " + info.hour + " in the " + info.location + " classroom,"
            message = message[:-1] + '.'
        elif len(results_list) == 1:
            info = results_list[0]
            message = "The " + eventEntity + " " + typeEventEntity +  " takes place on " + info.day + " at " + info.hour + " in the " + info.location + " classroom."
        
        dispatcher.utter_message(text=message)

        return []

class ActionGetMinConditions(Action):

    def name(self) -> Text:
        return "action_get_min_conditions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        dispatcher.utter_message(text="Sorry, I don't have the necessary information.")

        return []

class ActionGetMinNrOfAttendings(Action):

    def name(self) -> Text:
        return "action_get_min_nr_of_attendings"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        dispatcher.utter_message(text="Sorry, I don't have the necessary information.")

        return []

class ActionGetStartTimeEvent(Action):

    def name(self) -> Text:
        return "action_get_start_time_event"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Sorry, I did not understand. Please repeat the question and check the name of the event!"

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
                if currentEvent["class"] == event and currentEvent["type"] == typeEvent and currentEvent["calendar"] == "2021":
                    if currentEvent["relevance"] is not None:
                        for relevance in currentEvent["relevance"]:
                            if (relevance == sr or relevance == group or relevance == semigroup):
                                if currentEvent["rrule"] is not None:
                                    day, hour = helper.get_time(currentEvent)
                                    results_list.append(DateEventInfo(day, hour))
                                
        if len(results_list) >= 2:
            message = "The " + eventEntity + " " + typeEventEntity +  " starts:"
            for info in results_list:
                message += " at " + info.hour + ", on " + info.day + ","
            message = message[:-1] + '.'
        elif len(results_list) == 1:
            info = results_list[0]
            message = "The " + eventEntity + " " + typeEventEntity +  " starts at " + info.hour + " on " + info.day + "."

        dispatcher.utter_message(text=message)

        return []

class ActionGetTeacherName(Action):

    def name(self) -> Text:
        return "action_get_teacher_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        dispatcher.utter_message(text="Sorry, I don't have the necessary information.")

        return []

class ActionGetGroupLeaderName(Action):

    def name(self) -> Text:
        return "action_get_group_leader_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        dispatcher.utter_message(text="Sorry, I don't have the necessary information.")

        return []

class ActionGetSRLeaderName(Action):

    def name(self) -> Text:
        return "action_get_SR_leader_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        dispatcher.utter_message(text="Sorry, I don't have the necessary information.")

        return []

class ActionGetCourseGrade(Action):

    def name(self) -> Text:
        return "action_get_course_grading"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = "Sorry, I did not understand. Please repeat the question and check the name of the event!"

        id = tracker.current_state()['sender_id']
        doc = snapshots.document(id).get().to_dict()
        classFields = doc["class"]

        entities = tracker.latest_message['entities']
        eventEntity, typeEventEntity = helper.get_entities(entities)

        event = helper.compute_event_name(classFields, eventEntity)
    
        events = firestore_db.collection(u'classes').get()

        for e in events:
            currentEventName = e.id
            currentEvent = e.to_dict()
            if currentEventName == event:
                if "grading" in currentEvent.keys():
                    message = "The grade score for " + eventEntity + " is: "
                    for grade in currentEvent["grading"]:
                        message = message + grade + ": " + str(currentEvent["grading"][grade]) + "; "
        
        dispatcher.utter_message(text=message)

        return []