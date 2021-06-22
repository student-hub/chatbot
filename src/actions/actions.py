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
            dispatcher.utter_message(text="Scuze, nu dețin această informație. Te rog verifică daca numele evenimentului este scris corect!")
            return []
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
        typeNotFound = False
        another_hour = 0
        another_day = ""
        message = "Scuze, nu dețin această informație. Te rog verifică daca numele evenimentului este scris corect!"
        for e in events:
            currentEvent = e.to_dict()
            if "class" in currentEvent.keys():
                if currentEvent["class"] == event:
                    temp = pd.Timestamp(currentEvent["start"])
                    type = currentEvent["type"]
                    if(type == "lecture"):
                        type = "curs"
                    index = currentEvent["rrule"].find("BYDAY=")
                    day = currentEvent["rrule"][(index + 6) : (index + 8)]
                    hour = temp.hour + 3 #timezone
                    minute = temp.minute
                    h = str(hour) + str(minute) if minute > 0 else str(hour)

                    if len(typeEventEntity) == 0:
                        if currentEvent["relevance"] is not None:
                            dispatcher.utter_message(text=eventEntity + "-" + type + "-" + currentEvent["relevance"][0] +" are loc " + utils.getDayRo(day) + ", la ora " + h)
                            typeNotFound = True
                    else:
                        if ((typeEventEntity == "seminarul" and currentEvent["type"] == "seminar" and group == currentEvent["relevance"][0])
                            or (typeEventEntity == "laboratorul" and currentEvent["type"] == "lab" and (semigroup == currentEvent["relevance"][0] or group == currentEvent["relevance"][0])
                            or (typeEventEntity == "cursul" and currentEvent["type"] == "lecture"))):
                            if(eventFound):
                                message = typeEventEntity.capitalize() + " de " + eventEntity + " are loc " + utils.getDayRo(day) + ", la ora " + h + " și " + utils.getDayRo(another_day) + " la ora " + another_hour
                                break
                            message = typeEventEntity.capitalize() + " de " + eventEntity + " are loc " + utils.getDayRo(day) + ", la ora " + h
                            another_hour = h
                            another_day = day
                            eventFound = True
        if typeNotFound:
            return []
        dispatcher.utter_message(text=message) 
        return []

class ActionGetEndTimeEvent(Action):

    def name(self) -> Text:
        return "action_get_end_time_event"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Evenimentul se termină la ora...")

        return []

class ActionLocateEvent(Action):

    def name(self) -> Text:
        return "action_locate_event"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Evenimentul se desfășoară...")

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

        dispatcher.utter_message(text="Evenimentul începe la ora...")

        return []

class ActionGetTeacherName(Action):

    def name(self) -> Text:
        return "action_get_teacher_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Numele profesorului este...")

        return []

class ActionGetGroupLeaderName(Action):

    def name(self) -> Text:
        return "action_get_group_leader_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Numele șefului de grupă este...")

        return []

class ActionGetSRLeaderName(Action):

    def name(self) -> Text:
        return "action_get_SR_leader_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Numele șefului de serie este...")

        return []