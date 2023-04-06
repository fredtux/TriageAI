# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

class AskOpenAI():
    @staticmethod
    def Ask(question) -> Text:
        return openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Descrie succint: " + question}],
            max_tokens=250
        )["choices"][0]["message"]["content"]


class ActionUtterAirwayDescription(Action):

    def name(self) -> Text:
        return "action_utter_airway_description"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        description = AskOpenAI.Ask("obstructia cailor aeriene")

        buttons = [
            {"title": "Da", "payload": "am caile respiratorii afectate"},
            {"title": "Nu", "payload": "respir bine"},
            {"title": "Vreau explicatii", "payload": "vreau explicatii despre caile respiratorii"}
        ]
        dispatcher.utter_message(text=f"O scurta definitie: {description}.<br><br>Aveti probleme cu caile respiratorii?", buttons=buttons)

        return []

class ActionUtterHemmorageDescription(Action):

    def name(self) -> Text:
        return "action_utter_hemmorage_description"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        description = AskOpenAI.Ask("hemoragie")

        dispatcher.utter_message(text=f"O scurta definitie: {description}.<br><br>Aveti hemoragie?")

        return []
    
class ActionUtterSeizingDescription(Action):

    def name(self) -> Text:
        return "action_utter_seizing_description"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        description = AskOpenAI.Ask("convulsii")

        dispatcher.utter_message(text=f"O scurta definitie: {description}.<br><br>Aveti convulsii?")

        return []
    
class ActionUtterPainHemmorageDescription(Action):

    def name(self) -> Text:
        return "action_utter_pain_hemmorage_description"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        description = AskOpenAI.Ask("scara medicala a durerii de la 1 la 10")

        dispatcher.utter_message(text=f"O scurta definitie: {description}.<br><br>Cum evaluati durerea pe o scara de la 1 la 10?")

        return []
    
class ActionUtterPainScaleDescription(Action):

    def name(self) -> Text:
        return "action_utter_pain_scale_description"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        description = AskOpenAI.Ask("scara medicala a durerii de la 1 la 10")

        buttons = [
            {"title": "Severa (7-10)", "payload": "durere severa"},
            {"title": "Moderata (4-6)", "payload": "durere moderata"},
            {"title": "Usoara (1-3)", "payload": "durere usoara"},
            {"title": "Nicio durere", "payload": "nicio durere"}
        ]
        dispatcher.utter_message(text=f"O scurta definitie: {description}.<br><br>Cum evaluati durerea pe o scara de la 1 la 10?", buttons=buttons)

        return []
    
class ActionUtterGCSDescription(Action):

    def name(self) -> Text:
        return "action_utter_gcs_description"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        description = AskOpenAI.Ask("GCS - Glasgow Coma Scale")
        
        buttons = [
            {"title": "Sub 12 (inclusiv)", "payload": "GCS mic"},
            {"title": "13 -14", "payload": "GCS mediu"},
            {"title": "15", "payload": "GCS mare"}
        ]
        dispatcher.utter_message(text=f"O scurta definitie: {description}.<br><br>Cum evaluati nivelul de constienta?", buttons=buttons)

        return []
    
class ActionUtterOxygenSaturationDescription(Action):

    def name(self) -> Text:
        return "action_utter_oxygen_saturation_description"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        description = AskOpenAI.Ask("saturatia de oxigen in sange")
        
        buttons = [
            {"title": "Sub 90%", "payload": "saturatie oxigen mica"},
            {"title": "90 - 92%", "payload": "saturatie oxigen medie"},
            {"title": "Peste 92%", "payload": "saturatie oxigen mare"}
        ]
        dispatcher.utter_message(text=f"O scurta definitie: {description}.<br><br>Cum evaluati saturatia de oxigen in sange?", buttons=buttons)

        return []
    
class ActionUtterCompensatedShockOrangeDescription(Action):

    def name(self) -> Text:
        return "action_compensated_shock_orange"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        SlotSet("compensated_shock", True)
        
        buttons = [
            {"title": "> 2 secunde", "payload": "timp CRT mic"},
            {"title": "<= 2 secunde", "payload": "timp CRT normal"}
        ]
        dispatcher.utter_message(text=f"Care este timpul CRT?", buttons=buttons)

        return []
    
class ActionUtterCompensatedShockYellowDescription(Action):

    def name(self) -> Text:
        return "action_compensated_shock_orange"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        SlotSet("compensated_shock", False)
        
        buttons = [
            {"title": "> 2 secunde", "payload": "timp CRT mic"},
            {"title": "<= 2 secunde", "payload": "timp CRT normal"}
        ]
        dispatcher.utter_message(text=f"Care este timpul CRT?", buttons=buttons)

        return []