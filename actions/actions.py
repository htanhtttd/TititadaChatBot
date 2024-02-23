# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas 
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

class ActionAskTerminology(Action):
    
    def name(sefl) -> Text:
        return "action_ask_terminology"
    
    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
        entities = tracker.latest_message['entities'][0]
        definition = entities['value']      
        print(definition)
        df = pandas.read_csv('C:\\Users\\htanh\\Desktop\\Tititada\\TititadaChatBot\\Definitioin.csv')
        df['length_definition'] = df['Definition'].apply(len)
        result = df[(df["Definition"].str.contains(definition)) & (df['length_definition'] <= len(definition)+2) & (df['length_definition'] >= len(definition)-2)]['Description'].values

        if result is None:
            message = 'Not have data'
        else:
            message = result[0]
        
        dispatcher.utter_message(text=str(message))
        
        return []  
