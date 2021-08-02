# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionLocateClassroom(Action):

    def name(self) -> Text:
        return "action_locate_classroom"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        dispatcher.utter_message(text="The classroom is located...")

        return []

class ActionGetDateEvent(Action):

    def name(self) -> Text:
        return "action_get_date_event"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        dispatcher.utter_message(text="This event takes place on...")

        return []

class ActionGetEndTimeEvent(Action):

    def name(self) -> Text:
        return "action_get_end_time_event"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        dispatcher.utter_message(text="The event ends at...")

        return []

class ActionLocateEvent(Action):

    def name(self) -> Text:
        return "action_locate_event"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        dispatcher.utter_message(text="The event is located in the classroom...")

        return []

class ActionGetMinConditions(Action):

    def name(self) -> Text:
        return "action_get_min_conditions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        dispatcher.utter_message(text="The minimum promotion conditions are...")

        return []

class ActionGetMinNrOfAttendings(Action):

    def name(self) -> Text:
        return "action_get_min_nr_of_attendings"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        dispatcher.utter_message(text="The min number of attendings is...")

        return []

class ActionGetStartTimeEvent(Action):

    def name(self) -> Text:
        return "action_get_start_time_event"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        dispatcher.utter_message(text="The event starts at...")

        return []

class ActionGetTeacherName(Action):

    def name(self) -> Text:
        return "action_get_teacher_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        dispatcher.utter_message(text="The teacher's name is...")

        return []

class ActionGetGroupLeaderName(Action):

    def name(self) -> Text:
        return "action_get_group_leader_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        dispatcher.utter_message(text="The name of the group leader is...")

        return []

class ActionGetSRLeaderName(Action):

    def name(self) -> Text:
        return "action_get_SR_leader_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        dispatcher.utter_message(text="The name of the sr leader is...")

        return []

class ActionGetCourseGrading(Action):

    def name(self) -> Text:
        return "action_get_course_grading"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        dispatcher.utter_message(text="The grade score is...")

        return []