# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSicknesSearch(Action):

     def name(self) -> Text:
         return "action_sicknes_search"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         for blob in tracker.latest_message['entities']:
            print(tracker.latest_message)
            if blob['entity'] == 'disease':
                sicknes = blob['value']

         dispatcher.utter_message(text=f"{sicknes} is a very serious disease")

         return []
