## story_goodbye
* goodbye
    - utter_goodbye

## story_thankyou
* thanks
    - utter_noworries

## Visa story 1
* greet
    - utter_greet
    - utter_ask_information_type
* enquire_visa_info
    - utter_search_provider_visa_welcome
    - utter_enquire_visa_info
* thanks
    - utter_goodbye

## Visa Story 2
* greet
    - utter_greet
    - utter_ask_information_type
* inform{"information_type":"visa"}
    - action_default_ask_affirmation
* enquire_visa_info{"information_type":"visa"}
    - action_revert_fallback_events
* enquire_visa_info{"information_type":"visa"}
    - utter_search_provider_visa_welcome
    - utter_enquire_visa_info
* thanks
    - utter_goodbye

## Place to visit 1
* greet
    - utter_greet
    - utter_ask_information_type
* enquire_places_to_visit
    - utter_search_provider_placestovisit_lifetime
    - utter_enquire_places_to_visit
* thanks
    - utter_goodbye

## Place to visit spiritual 1
* greet
    - utter_greet
    - utter_ask_information_type
* enquire_places_to_visit
    - utter_search_provider_placestovisit_lifetime
    - utter_enquire_places_to_visit
* enquire_spiritual_place
    - utter_search_provider_spiritual_places
    - utter_search_spiritual_places_results
* thanks
    - utter_goodbye

## Place to visit spiritual 2
* greet
    - utter_greet
    - utter_ask_information_type
* enquire_places_to_visit
    - utter_search_provider_placestovisit_lifetime
    - utter_enquire_places_to_visit
* enquire_spiritual_place
    - utter_search_provider_spiritual_places
    - utter_search_spiritual_places_results
* spiritual_boudhanath{"spiritualplace_type":"Boudhanath"}
    - utter_search_spiritual_boudhanath
* spiritual_pashupatinath{"spiritualplace_type":"Pashupatinath"}
    - utter_search_spiritual_pashupatinath
* spiritual_swoyambhunath{"spiritualplace_type":"Swoyambhunath"}
    - utter_search_spiritual_swoyambhunath
* spiritual_muktinath{"spiritualplace_type":"Muktinath"}
    - utter_search_spiritual_muktinath
* spiritual_janaki{"spiritualplace_type":"Janaki Temple"}
    - utter_search_spiritual_janaki
* spiritual_other{"spiritualplace_type":"Other Spiritual Places"}
    - utter_search_spiritual_others
* thanks
    - utter_goodbye

## Place to visit historical 1
* greet
    - utter_greet
    - utter_ask_information_type
* enquire_places_to_visit
    - utter_search_provider_placestovisit_lifetime
    - utter_enquire_places_to_visit
* enquire_historical_place
    - utter_search_provider_historical_places
    - utter_search_historical_places_results
* thanks
    - utter_goodbye

## Place to visit historical 2
* greet
    - utter_greet
    - utter_ask_information_type
* enquire_places_to_visit
    - utter_search_provider_placestovisit_lifetime
    - utter_enquire_places_to_visit
* enquire_historical_place
    - utter_search_provider_historical_places
    - utter_search_historical_places_results
* historical_kathmandu{"historicalplace_type":"Kathmandu Durbar Square"}
    - utter_search_historical_kathmandu
* historical_bhaktapur{"historicalplace_type":"Bhaktapur Durbar Square"}
    - utter_search_historical_bhaktapur
* historical_patan{"historicalplace_type":"Patan Durbar Square"}
    - utter_search_historical_patan
* historical_lumbini{"historicalplace_type":"Lumbini"}
    - utter_search_historical_lumbini
* historical_gorkha{"historicalplace_type":"Gorkha"}
    - utter_search_historical_gorkha
* historical_other{"historicalplace_type":"Other Historical Places"}
    - utter_search_historical_others
* thanks
    - utter_goodbye

## Place to visit nature 1
* greet
    - utter_greet
    - utter_ask_information_type
* enquire_places_to_visit
    - utter_search_provider_placestovisit_lifetime
    - utter_enquire_places_to_visit
* enquire_nature_place
    - utter_search_provider_nature_places
    - utter_search_nature_places_results
* thanks
    - utter_goodbye

## Place to vist nature 2
* greet
    - utter_greet
    - utter_ask_information_type
* enquire_places_to_visit
    - utter_search_provider_placestovisit_lifetime
    - utter_enquire_places_to_visit
* enquire_nature_place
    - utter_search_provider_nature_places
    - utter_search_nature_places_results
* nature_mountain_flights{"natureplace_type": "Mountain Flights"}
    - utter_search_nature_mountain_flights
* nature_bird_watching{"natureplace_type": "Bird Watching"}
    - utter_search_nature_bird_watching
* nature_mountain_viewing{"natureplace_type": "Mountain Viewing"}
    - utter_search_nature_mountain_viewing
* nature_jungle_discovery{"natureplace_type": "Jungle Discovery"}
    - utter_search_nature_jungle_discovery
* nature_butterfly_watching{"natureplace_type": "Butterfly Watching"}
    - utter_search_nature_butterfly_watching
* thanks
    - utter_goodbye

## Place to visit 3

* greet
    - utter_greet
    - utter_ask_information_type
* enquire_places_to_visit
    - utter_search_provider_placestovisit_lifetime
    - utter_enquire_places_to_visit
* enquire_historical_place
    - utter_search_provider_historical_places
    - utter_search_historical_places_results
* enquire_nature_place{"placetovisit_type":"nature"}
    - action_default_ask_affirmation
* enquire_nature_place
    - action_revert_fallback_events
* enquire_nature_place
    - utter_search_provider_nature_places
    - utter_search_nature_places_results
* thanks
    - utter_goodbye

## Place to visit 4

* greet
    - utter_greet
    - utter_ask_information_type
* enquire_nature_place
    - utter_search_provider_nature_places
    - utter_search_nature_places_results
* enquire_historical_place{"placetovisit_type":"historical"}
    - utter_search_provider_spiritual_places
    - utter_search_spiritual_places_results
* enquire_spiritual_place
    - utter_search_provider_spiritual_places
    - utter_search_spiritual_places_results
* thanks
    - utter_goodbye

## Things to do
* greet
    - utter_greet
    - utter_ask_information_type
* enquire_things_to_do
    - utter_search_provider_thingstodo
* thanks
    - utter_goodbye

## Things to do 2
* greet
    - utter_greet
    - utter_ask_information_type
* enquire_things_to_do
    - utter_search_provider_thingstodo
* enquire_rafting{"thingstodo_type":"rafting"}
    - utter_search_provider_rafting
    - utter_search_rafting_results
* enquire_paragliding{"thingstodo_type":"paragliding"}
    - utter_search_provider_paragliding
    - utter_search_paragliding_results
* enquire_canyoning{"thingstodo_type":"canyoning"}
    - utter_search_provider_canyoning
    - utter_search_canyoning_results
* enquire_hiking{"thingstodo_type":"hiking"}
    - utter_search_provider_hiking
    - utter_search_hiking_results
* enquire_bungee{"thingstodo_type":"bungee"}
    - utter_search_provider_bungee
    - utter_search_bungee_results
* enquire_trekking{"thingstodo_type":"trekking"}
    - utter_search_provider_trekking
    - utter_search_trekking_results
* thanks
    - utter_goodbye

## Things to do - hiking
* greet
    - utter_greet
    - utter_ask_information_type
* enquire_things_to_do
    - utter_search_provider_thingstodo
* enquire_hiking
    - utter_search_provider_hiking
    - utter_search_hiking_results
* thanks
    - utter_goodbye

## Things to do - trekking
* greet
    - utter_greet
    - utter_ask_information_type
* enquire_things_to_do
    - utter_search_provider_thingstodo
* enquire_trekking
    - utter_search_provider_trekking
    - utter_search_trekking_results
* thanks
    - utter_goodbye

## Things to do - canyoning
* greet
    - utter_greet
    - utter_ask_information_type
* enquire_things_to_do
    - utter_search_provider_thingstodo
* enquire_canyoning
    - utter_search_provider_canyoning
    - utter_search_canyoning_results
* thanks
    - utter_goodbye

## Things to do - rafting
* greet
    - utter_greet
    - utter_ask_information_type
* enquire_things_to_do
    - utter_search_provider_thingstodo
* enquire_rafting
    - utter_search_provider_rafting
    - utter_search_rafting_results
* thanks
    - utter_goodbye

## Things to do - bungee
* greet
    - utter_greet
    - utter_ask_information_type
* enquire_things_to_do
    - utter_search_provider_thingstodo
* enquire_bungee
    - utter_search_provider_bungee
    - utter_search_bungee_results
* thanks
    - utter_goodbye

## Things to do - paragliding
* greet
    - utter_greet
    - utter_ask_information_type
* enquire_things_to_do
    - utter_search_provider_thingstodo
* enquire_paragliding
    - utter_search_provider_paragliding
    - utter_search_paragliding_results
* thanks
    - utter_goodbye

## canyoning

* greet
    - utter_greet
    - utter_ask_information_type
* enquire_things_to_do
    - utter_search_provider_thingstodo
* enquire_canyoning
    - utter_search_provider_canyoning
    - utter_search_canyoning_results
* goodbye
    - utter_goodbye

## New Story

* greet
    - utter_greet
    - utter_ask_information_type
* enquire_places_to_visit
    - utter_search_provider_placestovisit_lifetime
    - utter_enquire_places_to_visit
* enquire_spiritual_place
    - utter_search_provider_spiritual_places
    - utter_search_spiritual_places_results
* spiritual_pashupatinath{"spiritualplace_type":"Pashupatinath"}
    - utter_search_spiritual_pashupatinath

## New Story

* greet
    - utter_greet
    - utter_ask_information_type
* enquire_places_to_visit
    - utter_search_provider_placestovisit_lifetime
    - utter_enquire_places_to_visit
* enquire_spiritual_place
    - utter_search_provider_spiritual_places
    - utter_search_spiritual_places_results
* spiritual_boudhanath{"spiritualplace_type":"Boudhanath"}
    - utter_search_spiritual_boudhanath

## New Story

* greet
    - utter_greet
    - utter_ask_information_type
* enquire_places_to_visit
    - utter_search_provider_placestovisit_lifetime
    - utter_enquire_places_to_visit
* enquire_spiritual_place
    - utter_search_provider_spiritual_places
    - utter_search_spiritual_places_results
* spiritual_swoyambhunath{"spiritualplace_type":"Swoyambhunath"}
    - utter_search_spiritual_swoyambhunath

## New Story

* greet
    - utter_greet
    - utter_ask_information_type
* enquire_places_to_visit
    - utter_search_provider_placestovisit_lifetime
    - utter_enquire_places_to_visit
* enquire_spiritual_place
    - utter_search_provider_spiritual_places
    - utter_search_spiritual_places_results
* spiritual_muktinath{"spiritualplace_type":"Muktinath"}
    - utter_search_spiritual_muktinath

## New Story

* greet
    - utter_greet
    - utter_ask_information_type
* enquire_places_to_visit
    - utter_search_provider_placestovisit_lifetime
    - utter_enquire_places_to_visit
* enquire_spiritual_place
    - utter_search_provider_spiritual_places
    - utter_search_spiritual_places_results
* spiritual_janaki{"spiritualplace_type":"Janaki Temple"}
    - utter_search_spiritual_janaki

## New Story

* greet
    - utter_greet
    - utter_ask_information_type
* enquire_places_to_visit
    - utter_search_provider_placestovisit_lifetime
    - utter_enquire_places_to_visit
* enquire_spiritual_place
    - utter_search_provider_spiritual_places
    - utter_search_spiritual_places_results
* spiritual_other{"spiritualplace_type":"Other Spiritual Places"}
    - utter_search_spiritual_others

## New Story

* enquire_nature_place
    - utter_search_provider_nature_places
    - utter_search_nature_places_results
* nature_mountain_viewing{"natureplace_type":"Mountain Viewing"}
    - utter_search_nature_mountain_viewing
* nature_jungle_discovery{"natureplace_type":"Jungle Discovery"}
    - utter_search_nature_jungle_discovery
* nature_butterfly_watching{"natureplace_type":"butterfly watching"}
    - utter_search_nature_butterfly_watching
* nature_bird_watching{"natureplace_type":"bird watching"}
    - utter_search_nature_bird_watching

## New Story
* greet
    - utter_greet
    - utter_ask_information_type
* enquire_places_to_visit
    - utter_search_provider_placestovisit_lifetime
    - utter_enquire_places_to_visit
* enquire_historical_place{"placetovisit_type":"historical"}
    - utter_search_provider_spiritual_places
    - utter_search_spiritual_places_results
* spiritual_janaki{"spiritualplace_type":"janaki temple"}
    - utter_search_spiritual_janaki
* spiritual_other
    - utter_search_spiritual_others
* enquire_rafting{"thingstodo_type":"rafting"}
    - utter_search_provider_rafting
    - utter_search_rafting_results
* enquire_paragliding{"thingstodo_type":"paragliding"}
    - utter_search_provider_paragliding
    - utter_search_paragliding_results
* enquire_canyoning{"thingstodo_type":"canyoning"}
    - utter_search_provider_canyoning
    - utter_search_canyoning_results
* enquire_hiking{"thingstodo_type":"hiking"}
    - utter_search_provider_hiking
    - utter_search_hiking_results
* enquire_bungee{"thingstodo_type":"bungee"}
    - utter_search_provider_bungee
    - utter_search_bungee_results
* enquire_trekking{"thingstodo_type":"trekking"}
    - utter_search_provider_trekking
    - utter_search_trekking_results
* enquire_rafting{"thingstodo_type":"rafting"}
    - utter_search_provider_rafting
    - utter_search_rafting_results
* thanks
    - utter_goodbye

## Festivals

* greet
    - utter_greet
    - utter_ask_information_type
* enquire_culture
    - utter_search_provider_culture
* culture_festivals{"culture_type":"Festivals"}
    - utter_search_provider_festivals
    - utter_search_festivals_results

## Customs

* greet
    - utter_greet
    - utter_ask_information_type
* enquire_culture
    - utter_search_provider_culture
* culture_customs{"culture_type":"Customs"}
    - utter_search_provider_customs
    - utter_search_customs_results

## Foods & Cuisine

* greet
    - utter_greet
    - utter_ask_information_type
* enquire_culture
    - utter_search_provider_culture
* culture_food{"culture_type":"Foods"}
    - utter_search_provider_foods
    - utter_search_foods_results

## Culture
* greet
    - utter_greet
    - utter_ask_information_type
* enquire_culture
    - utter_search_provider_culture
* culture_festivals{"culture_type":"Festivals"}
    - utter_search_provider_festivals
    - utter_search_festivals_results
* culture_customs{"culture_type":"Customs"}
    - utter_search_provider_customs
    - utter_search_customs_results
* culture_food{"culture_type":"Foods"}
    - utter_search_provider_foods
    - utter_search_foods_results
* thanks
    - utter_goodbye

## New Story

* greet
    - utter_greet
    - utter_ask_information_type
* enquire_culture
    - utter_search_provider_culture
* culture_festivals{"culture_type":"Festivals"}
    - utter_search_provider_festivals
    - utter_search_festivals_results
* culture_customs{"culture_type":"customs"}
    - utter_search_provider_customs
    - utter_search_customs_results
* culture_festivals{"culture_type":"festivals"}
    - utter_search_provider_festivals
    - utter_search_festivals_results
* culture_food
    - utter_search_provider_foods
    - utter_search_foods_results

## Quick Facts
* greet
    - utter_greet
    - utter_ask_information_type
* enquire_quick_facts
    - utter_search_provider_quickfacts
    - utter_search_quickfacts_results

## New Story

* greet
    - utter_greet
    - utter_ask_information_type
* currency
    - utter_search_currency_results
    - utter_search_currency_results_2

## New Story

* greet
    - utter_greet
    - utter_ask_information_type
* greet{"quickfacts_type":"internet"}
    - utter_search_internet_results

## New Story

* greet
    - utter_greet
    - utter_ask_information_type
* safety{"quickfacts_type":"safety"}
    - utter_search_safety_results
    - utter_search_safety_results_2

## New Story

* greet
    - utter_greet
    - utter_ask_information_type
* language{"quickfacts_type":"language"}
    - utter_search_language_resuts

## New Story

* greet
    - utter_greet
    - utter_ask_information_type
* enquire_explore_more
    - utter_search_explore_more_results_1
    - utter_search_explore_more_results_2

## New Story
* greet
    - utter_greet
    - utter_ask_information_type
* enquire_explore_more
    - utter_search_explore_more_results_1
    - utter_search_explore_more_results_2
* currency
    - utter_search_currency_results
    - utter_search_currency_results_2

## accommodation
* greet
    - utter_greet
    - utter_ask_information_type
* enquire_accommodation
    - find_hotel_types
* inform{"hotel_type": "5-star"}
    - hotel_form
    - form{"name": "hotel_form"}
    - form{"name" : null}
* inform{"hotel_id": "1"}
    - find_hotel_address
    - utter_hotel_address

## accommodations 2
* greet
    - utter_greet
    - utter_ask_information_type
* enquire_accommodation
    - find_hotel_types
* inform{"hotel_type": "5-star"}
    - hotel_form
    - form{"name": "hotel_form"}
    - form{"name" : null}
* inform{"hotel_id": "3"}
    - find_hotel_address
    - utter_hotel_address

* search_provider_hotel{"hotel_type": "3-star"}
    - hotel_form
    - form{"name": "hotel_form"}
    - form{"name": null}
* inform{"hotel_id": 5}
    - find_hotel_address
    - utter_hotel_address

## accommodations 3
* search_provider_hotel{"location": "Bhaktapur", "hotel_type": "tourist-standard-hotels"}
    - hotel_form
    - form{"name": "hotel_form"}
    - form{"name": null}
* inform{"hotel_id": "1"}
    - find_hotel_address
    - utter_hotel_address
* thanks
    - utter_noworries

<!-- ## accommodation_interactive_story
* out_of_scope
    - find_hotel_types
* inform{"hotel_type": "3-star"}
    - slot{"hotel_type": "3-star"}
    - hotel_form
    - form{"name": "hotel_form"}
    - slot{"hotel_type": "3-star"}
    - slot{"hotel_type": "3-star"}
    - slot{"requested_slot": "location"}
* form: inform{"location": "Kathmandu"}
    - slot{"location": "Kathmandu"}
    - form: hotel_form
    - slot{"location": "Kathmandu"}
    - form{"name": null}
    - slot{"requested_slot": null} -->

<!-- ## New Story

    - slot{"hotel_type":"4-star"}
* greet
    - utter_greet
    - utter_ask_information_type
* enquire_accommodation
    - find_hotel_types
* inform{"hotel_type":"4-star"}
    - slot{"hotel_type":"4-star"}
    - hotel_form
* inform{"location":"Kathmandu"}
    - hotel_form
    - form{"name":"hotel_form"}
    - slot{"hotel_type":"4-star"}
    - slot{"location":"Kathmandu"}
    - slot{"location":["Kathmandu","Kathmandu"]}
    - form{"name":null}
    - slot{"requested_slot":null}
* inform{"hotel_id":"2"}
    - slot{"hotel_id":"2"}
    - find_hotel_address
    - slot{"hotel_address":"Ravi Bhanvan, +977-1-5234725, Reservation@Crowneimperial.Com, Https://Www.Crowneimperial.Com"}
    - utter_hotel_address -->

## New Story

* greet
    - utter_greet
    - utter_ask_information_type
* enquire_accommodation
    - find_hotel_types
* inform{"hotel_type":"4-star"}
    - slot{"hotel_type":"4-star"}
    - hotel_form
    - form{"name":"hotel_form"}
    - slot{"hotel_type":"4-star"}
    - slot{"hotel_type":"4-star"}
    - slot{"requested_slot":"location"}
* inform{"location":"Kathmandu"}
    - slot{"location":"Kathmandu"}
    - hotel_form
    - slot{"location":["Kathmandu","Kathmandu"]}
    - form{"name":null}
    - slot{"requested_slot":null}
* inform{"hotel_id":"4"}
    - slot{"hotel_id":"4"}
    - find_hotel_address
    - slot{"hotel_address":"Lazimpat, +977-1-4410151,4410152, Sales@Shankerhotel.Com, Https://Www.Shankerhotel.Com.Np"}
    - utter_hotel_address
* thanks
    - utter_noworries

## New Story

* greet
    - utter_greet
    - utter_ask_information_type
* enquire_accommodation
    - find_hotel_types
* inform{"hotel_type":"5-star"}
    - slot{"hotel_type":"5-star"}
    - hotel_form
    - form{"name":"hotel_form"}
    - slot{"hotel_type":"5-star"}
    - slot{"hotel_type":"5-star"}
    - slot{"requested_slot":"location"}
* inform{"location":"Thimi"}
    - slot{"location":"Thimi"}
    - hotel_form
    - slot{"location":["Thimi","Thimi"]}
    - form{"name":null}
    - slot{"requested_slot":null}
* thanks
    - utter_noworries

## hospital
* greet
    - utter_greet
    - utter_ask_information_type
* enquire_healthfacility
    - find_facility_types
* inform{"facility_type": "hospital"}
    - facility_form
    - form{"name": "facility_form"}
    - form{"name" : null}
* inform{"facility_id": "1"}
    - find_healthcare_address
    - utter_healthcare_address