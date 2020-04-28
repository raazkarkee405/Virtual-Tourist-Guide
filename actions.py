# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from typing import Dict, Text, Any, List

import requests
from rasa_sdk import Action
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormAction


ENDPOINTS = {
    "base": "https://raazkarkee.pythonanywhere.com/getJsonFromFile/{}.json",
    "5-star": 
    {
        "city_query": "?city={}",
        "id_query": "?id={}"
    },
    "4-star": 
    {
        "city_query": "?city={}",
        "id_query": "?id={}"
    },
    "3-star": 
    {
        "city_query": "?city={}",
        "id_query": "?id={}"
    },
    "tourist-standard-hotels": 
    {
        "city_query": "?city={}",
        "id_query": "?id={}"
    },
    "resorts":
    {
        "city_query": "?city={}",
        "id_query": "?id={}"
    },
    "hospitals":
    {
        "city_query": "?city={}",
        "id_query": "?id={}"
    },
     "clinics": {
         "city_query": "?city={}",
        "id_query": "?id={}"
     },
     "pharmacies": {
         "city_query": "?city={}",
        "id_query": "?id={}"
     }
}

HOTEL_TYPES = {
    "5_star":
        {
            "name": "5-star hotel",
            "resource": "5-star"
        },
    "4_star":
        {
            "name": "4-star hotel",
            "resource": "4-star"
        },
    "3_star":
        {
            "name": "3-star hotel",
            "resource": "3-star"
        },
    "tourist_standard_hotels":
        {
            "name": "tourist standard hotels",
            "resource": "tourist-standard-hotels"
        },
    "resorts":
        {
            "name": "resorts",
            "resource": "resorts"
        }
    
}

def _create_path(base: Text, resource: Text, query: Text, values: Text) -> Text:
    """Creates a path to find provider using the endpoints."""

    if isinstance(values, list):
        return (base + query).format(
            resource, ', '.join('"{0}"'.format(w) for w in values))
    else:
        return (base + query).format(resource, values)

def _find_hotels(location: Text, resource: Text) -> List[Dict]:
    """Returns json of hotels matching the search criteria."""

    if str(location):
        full_path = _create_path(ENDPOINTS["base"], resource, ENDPOINTS[resource]["city_query"],location.upper())
        
    else:
        full_path = _create_path(ENDPOINTS["base"], resource, ENDPOINTS[resource]["city_query"],location.upper())
        
    
    results = requests.get(full_path).json()

    return results

def _resolve_name(hotel_type, resource) ->Text:
    for key, value in hotel_type.items():
        if value.get("resource") == resource:
            return value.get("name")
    return ""

class FindHotelTypes(Action):
    """This action class allows to display buttons for each hotel_type 
    for the user to chose from to fill the hotel_type entity slot."""
    
    def name(self) -> Text:
        """Unique identifier of the action"""

        return "find_hotel_types"
     
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List:

        quick_replies = []
        for t in HOTEL_TYPES:
            hotel_type = HOTEL_TYPES[t]
            payload = "/inform{\"hotel_type\": \"" + hotel_type.get("resource") + "\"}"

            quick_replies.append({"content_type": "text", "title": "{}".format(hotel_type.get("name").title()), "payload": payload})
        dispatcher.utter_message(template="utter_search_accommodation_results", quick_replies=quick_replies)
        return []

class FindHotelAddress(Action):
    """This action class retrieves the address of the user's hotel choice to display it to the user."""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "find_hotel_address"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        hotel_type = tracker.get_slot("hotel_type")
        hotel_id = tracker.get_slot("hotel_id")
        hotel_city = tracker.get_slot("hotel_city")
        full_path = _create_path(ENDPOINTS["base"], hotel_type, ENDPOINTS[hotel_type]["id_query"], hotel_id)
        results = requests.get(full_path).json()
        num = int(hotel_id) - 1
        if results:
            selected = results[num]
            if hotel_type == HOTEL_TYPES["5_star"]["resource"]:
                address = "{}, {}, {}, {}".format(selected["address"].title(),
                                                 selected["contact"].title(),
                                                 selected["email"].title(),
                                                 selected["website"].title())
            elif hotel_type == HOTEL_TYPES["4_star"]["resource"]:
                address = "{}, {}, {}, {}".format(selected["address"].title(),
                                                 selected["contact"].title(),
                                                 selected["email"].title(),
                                                 selected["website"].title())      
            elif hotel_type == HOTEL_TYPES["3_star"]["resource"]:
                address = "{}, {}, {}, {}".format(selected["address"].title(),
                                                 selected["contact"].title(),
                                                 selected["email"].title(),
                                                 selected["website"].title()) 
            elif hotel_type == HOTEL_TYPES["tourist_standard_hotels"]["resource"]:
                address = "{}, {}, {}, {}".format(selected["address"].title(),
                                                 selected["contact"].title(),
                                                 selected["email"].title(),
                                                 selected["website"].title())                                     
            elif hotel_type == HOTEL_TYPES["resorts"]["resource"]:
                address = "{}, {}, {}, {}".format(selected["address"].title(),
                                                 selected["contact"].title(),
                                                 selected["email"].title(),
                                                 selected["website"].title())                                    
            else:
                address = "{}, {}".format(selected["address"].title(),
                                                 selected["contact"].title())

            return [SlotSet("hotel_address", address)]
        else:
            return [SlotSet("hotel_address", "not found")]  

class HotelForm(FormAction):
    """Custom form action to fill all slots required to find specific type
    of hotel in a certain city."""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "hotel_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that form has to fill"""

        return ["hotel_type", "location"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"hotel_type": self.from_entity(entity="hotel_type", intent=["inform", "search_provider_hotel"]),
                "location": self.from_entity(entity="location", intent=["inform", "search_provider_hotel"])}                                                             

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        """Once required slots are filled, print buttons for found hotels"""

        local = tracker.get_slot('location')
        if type(local) == list:
            location = local[0]
        else:
            location = local
        hotel_type = tracker.get_slot('hotel_type')

        results = _find_hotels(location, hotel_type)
        button_name = _resolve_name(HOTEL_TYPES, hotel_type)
        if len(results) == 0:
            dispatcher.utter_message("Sorry, we could not find a {} in {}.".format(button_name, location.title()))
            return []
        
        buttons = []
        # limit number of results to 3 for clear presentation purposes
        for r in results[:3]:
            if hotel_type == HOTEL_TYPES["5_star"]["resource"]:
                hotel_id = r.get("id")
                name = r["hotel_name"]
            elif hotel_type == HOTEL_TYPES["4_star"]["resource"]:
                hotel_id = r.get("id")
                name = r["hotel_name"]
            elif hotel_type == HOTEL_TYPES["3_star"]["resource"]:
                hotel_id = r.get("id")
                name = r["hotel_name"]
            elif hotel_type == HOTEL_TYPES["tourist_standard_hotels"]["resource"]:
                hotel_id = r.get("id")
                name = r["hotel_name"]
            elif hotel_type == HOTEL_TYPES["resorts"]["resource"]:
                hotel_id = r.get("id")
                name = r["hotel_name"]
            else:
                hotel_id = r["id"]
                name = r["hotel_name"]
            
            payload = "/inform{\"hotel_id\":\"" + hotel_id + "\"}"
            buttons.append({"type": "postback", "title": "{}".format(name.title()), "payload": payload})

        if len(buttons) == 1:
            message = "Here is a {} near you:".format(button_name)
        else:
            if button_name == "tourist standard hotel":
                button_name == "standard hotels"
            message = "Here are {} {}s near you:".format(len(buttons), button_name)
        
        dispatcher.utter_button_message(message, buttons)

        return []

## To extract different health facilities

FACILITY_TYPES = {
    "hospital":
        {
            "name": "hospital",
            "resource": "hospitals"
        },
    "clinic":
        {
            "name": "clinic",
            "resource": "clinics"
        },
    "pharmacy":
        {
            "name": "pharmacy",
            "resource": "pharmacies"
        }
}


def _create_path_2(base: Text, resource: Text,
                 query: Text, values: Text) -> Text:
    """Creates a path to find provider using the endpoints."""

    if isinstance(values, list):
        return (base + query).format(
            resource, ', '.join('"{0}"'.format(w) for w in values))
    else:
        return (base + query).format(resource, values)


def _find_facilities(location: Text, resource: Text) -> List[Dict]:
    """Returns json of hospitals matching the search criteria."""

    if str(location):
       full_path = _create_path_2(ENDPOINTS["base"], resource, ENDPOINTS[resource]["city_query"],location.upper())
   
    else:
        full_path = _create_path_2(ENDPOINTS["base"], resource, ENDPOINTS[resource]["city_query"],location.upper())

    
    results = requests.get(full_path).json()
    
    return results


def _resolve_name_2(facility_types, resource) ->Text:
    for key, value in facility_types.items():
        if value.get("resource") == resource:
            return value.get("name")
    return ""


class FindFacilityTypes(Action):
    """This action class allows to display buttons for each facility type
    for the user to chose from to fill the facility_type entity slot."""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "find_facility_types"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        buttons = []
        for t in FACILITY_TYPES:
            facility_type = FACILITY_TYPES[t]
            payload = "/inform{\"facility_type\": \"" + facility_type.get(
                "resource") + "\"}"

            buttons.append(
                {"type": "postback", "title": "{}".format(facility_type.get("name").title()), "payload": payload})

        dispatcher.utter_button_template("utter_search_healthcare_results", buttons, tracker)
        return []


class FindHealthCareAddress(Action):
    """This action class retrieves the address of the user's
    healthcare facility choice to display it to the user."""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "find_healthcare_address"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        facility_type = tracker.get_slot("facility_type")
        healthcare_id = tracker.get_slot("facility_id")
        full_path = _create_path_2(ENDPOINTS["base"], facility_type,
                                 ENDPOINTS[facility_type]["id_query"],
                                 healthcare_id)
        results = requests.get(full_path).json()
        num = int(healthcare_id) - 1
        if results:
            selected = results[num]
            if facility_type == FACILITY_TYPES["hospital"]["resource"]:
                address = "{}, {}, {}, {}".format(selected["address"].title(),
                                                 selected["contact"].title(),
                                                 selected["email"].title(),
                                                 selected["website"].title())
            elif facility_type == FACILITY_TYPES["clinic"]["resource"]:
                address = "{}, {}".format(selected["address"].title(),
                                                 selected["contact"].title())                                                  
            elif facility_type == FACILITY_TYPES["pharmacy"]["resource"]:
                address = "{}, {}".format(selected["address"].title(),
                                                 selected["contact"].title())                                          
            else:
                address = "{}, {}".format(selected["address"].title(),
                                                 selected["contact"].title())

            return [SlotSet("facility_address", address)]
        else:
            return [SlotSet("facility_address", "not found")]


class FacilityForm(FormAction):
    """Custom form action to fill all slots required to find specific type
    of healthcare facilities in a certain city or zip code."""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "facility_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["facility_type", "location"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"facility_type": self.from_entity(entity="facility_type",
                                                  intent=["inform",
                                                          "search_provider_hospital"]),
                "location": self.from_entity(entity="location",
                                             intent=["inform",
                                                     "search_provider_hospital"])}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:
        """Once required slots are filled, print buttons for found facilities"""

        local = tracker.get_slot('location')
        if type(local) == list:
            location = local[0]
        else:
            location = local
        facility_type = tracker.get_slot('facility_type')

        results = _find_facilities(location, facility_type)
        button_name = _resolve_name_2(FACILITY_TYPES, facility_type)
        if len(results) == 0:
            dispatcher.utter_message(
                "Sorry, we could not find a {} in {}.".format(button_name,
                                                              location.title()))
            return []

        buttons = []
        # limit number of results to 3 for clear presentation purposes
        for r in results[:3]:
            if facility_type == FACILITY_TYPES["hospital"]["resource"]:
                facility_id = r.get("id")
                name = r["hospital_name"]
            elif facility_type == FACILITY_TYPES["clinic"]["resource"]:
                facility_id = r.get("id")
                name = r["clinic_name"]
            elif facility_type == FACILITY_TYPES["pharmacy"]["resource"]:
                facility_id = r.get("id")
                name = r["pharmacy_name"]
            else:
                facility_id = r["id"]
                name = r["facility_name"]

            payload = "/inform{\"facility_id\":\"" + facility_id + "\"}"
            buttons.append(
                {"type": "postback", "title": "{}".format(name.title()), "payload": payload})

        if len(buttons) == 1:
            message = "Here is a {} near you:".format(button_name)
        else:
            if button_name == "pharmacy":
                button_name = "pharmacies"
            message = "Here are {} {}s near you:".format(len(buttons),
                                                         button_name)
                                                         
        dispatcher.utter_button_message(message, buttons)

        return []
