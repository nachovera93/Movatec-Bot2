import datetime
from datetime import date, timedelta
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import Restarted


def month_converter(i):
       month = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
       return month[i]


def ConverterDate():
     global mes
     global dia
     global anio
     global nombreMes 
     global hora
     now = datetime.datetime.now()
     dia=now.day
     mes=now.month
     anio=now.year
     nombreMes=month_converter(mes)
     hora=f'{now.hour}:{now.minute}'
     


class FechaVencimiento(Action):
    def name(self):
        return "action_fecha"

    def run(self, dispatcher, tracker, domain):
        ConverterDate()
        dispatcher.utter_message(f'Estamos a {dia} de {nombreMes} del {anio}')
        return []


class ActionGreetTimeofday(Action):
    def name(self): 
        return "action_greet_timeofday"

    def run(self, dispatcher, tracker, domain):  #metodo para describir lo que hará la acción

        t = datetime.datetime.now()
        print("hora :",t)
        if 23 >= int(t.hour) >= 12:
             print("Buenas tardes mi nombre es Eva :)")
             dispatcher.utter_message("Buenas tardes mi nombre es Evva :)")
        else:
             print("Buenos días mi nombre es Eva :)")
             dispatcher.utter_message("Buenos días mi nombre es Evva :)")
            
        return []

class ActionDarHora(Action):
    def name(self):   
        return "action_dar_hora"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ConverterDate()
        t = datetime.datetime.now()
        if 23 >= int(t.hour) >= 12:
             t2 = "PM"
        else:
             t2 = "AM"
        dispatcher.utter_message(text=f"Son las {hora} {t2}")

        return []





