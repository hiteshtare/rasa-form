# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ActionHelloWorld(FormAction):

    # ActionName name registed in domain
    def name(self) -> Text:
        return "admission_form"

    # Invoked automatically
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        # A list of required slots that form has to be filled
        print("required_slots(tracker: Tracker)")
        return ["name", "ssn", "subject"]

    # Invoked automatically
    @staticmethod
    def subject_db() -> List[Text]:
        return [
            "it",
            "space",
            "computers",
            "neurology",
            "datascience",
        ]

    # To validate subject using syntax validate_slotname
    def validate_subject(self, value: Text, dispatcher: CollectingDispatcher,
                         tracker: Tracker,
                         domain: Dict[Text, Any]) -> Dict[Text, Any]:
        # self is same as this in Typescript
        if value.lower() in self.subject_db():
            # slotname in string format
            return {"subject": value}
        else:
            # to invoke response defined in domain use template
            dispatcher.utter_message(template="utter_wrong_subject")
            return {"subject": None}

    # To validate ssn using syntax validate_slotname
    def validate_ssn(self, value: Text, dispatcher: CollectingDispatcher,
                     tracker: Tracker,
                     domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if len(value) == 6:
            # slotname in string format
            return {"ssn": value}
        else:
            # to invoke response defined in domain use template
            dispatcher.utter_message(template="utter_wrong_ssn")
            return {"ssn": None}

        # def slots_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        #     return {
        #         "subject_code": [
        #             self.from_entity(entity="subject", intent="subject_entry")
        #         ]
        #     }

    def submit(self, dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:

        # to invoke response defined in domain use template
        dispatcher.utter_message(template="utter_submit")

        return []
