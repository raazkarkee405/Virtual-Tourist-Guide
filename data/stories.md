## happy_path
* greet
    - find_facility_types
* inform{"facility_type": "xubh-q36u"}    
    - facility_form
    - form{"name": "facility_form"}
    - form{"name": null}
* inform{"facility_id": 5}
    - find_healthcare_address
    - utter_address
* thanks
    - utter_noworries

## happy_path_multi_requests
* greet
    - find_facility_types
* inform{"facility_type": "xubh-q36u"}
    - facility_form
    - form{"name": "facility_form"}
    - form{"name": null}
* inform{"facility_id": "7"}
    - find_healthcare_address
    - utter_address 
     
* search_provider{"facility_type": "xubh-q36u"}
    - facility_form
    - form{"name": "facility_form"}
    - form{"name": null}
* inform{"facility_id": 2}   
    - find_healthcare_address
    - utter_address

## happy_path2
* search_provider{"location": "Bhaktapur", "facility_type": "xubh-q36u"}
    - facility_form
    - form{"name": "facility_form"}
    - form{"name": null}
* inform{"facility_id": "1"}
    - find_healthcare_address
    - utter_address
* thanks
    - utter_noworries

## story_goodbye
* goodbye
    - utter_goodbye

## story_thankyou
* thanks
    - utter_noworries
## interactive_story_1
* out_of_scope
    - find_facility_types
* inform{"facility_type": "xubh-q36u"}
    - slot{"facility_type": "xubh-q36u"}
    - facility_form
    - form{"name": "facility_form"}
    - slot{"facility_type": "xubh-q36u"}
    - slot{"facility_type": "xubh-q36u"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Kathmandu"}
    - slot{"location": "Kathmandu"}
    - form: facility_form
    - slot{"location": "Kathmandu"}
    - form{"name": null}
    - slot{"requested_slot": null}
