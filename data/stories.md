## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_check_location
    - slot{"location": "bengaluru"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* email{"email": "rlakshminarayana@gmail.com"}
    - slot{"email": "rlakshminarayana@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - action_restart
    
    
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_check_location
    - slot{"location": "bengaluru"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_price
* price{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* email{"email": "rlakshminarayana@gmail.com"}
    - slot{"email": "rlakshminarayana@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* email{"email": "xyz@sth.edu"}
    - slot{"email": "xyz@sth.edu"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - action_restart
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Lucknow"}
    - slot{"location": "Lucknow"}
    - action_check_location
    - slot{"location": "lucknow"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* email{"email": "xyz@sth.edu"}
    - slot{"email": "xyz@sth.edu"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"location": "kolkata"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* email{"email": "jddk.2jmd@kdl.co.in"}
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"location": "kolkata"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "milinangalia@gmail.com"}
    - slot{"email": "milinangalia@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"results_found": false}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"results_found": false}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalre"}
    - slot{"location": "bangalre"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"results_found": false}
    - utter_goodbye
    - action_restart
    
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"results_found": false}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"results_found": false}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"results_found": false}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* email{"email": "milinangalia@gmail.com"}
    - slot{"email": "milinangalia@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"results_found": false}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart
    
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* cuisine{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart
    
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_check_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "milinangalia@gmail.com"}
    - slot{"email": "milinangalia@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - action_restart
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_check_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* cuisine{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "milinangalia@gmail.com"}
    - slot{"email": "milinangalia@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "low", "location": "pune"}
    - slot{"location": "pune"}
    - slot{"price": "low"}
    - action_check_location
    - slot{"location": "pune"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* cuisine{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_search_restaurants
    - slot{"results_found": false}
    - utter_goodbye
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"price": "high", "cuisine": "mexican", "location": "pune"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "pune"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"location": "pune"}
    - slot{"location_ok": true}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "milinangalia@gmail.com"}
    - slot{"email": "milinangalia@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - action_restart

## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"price": "low", "cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - slot{"price": "low"}
    - utter_ask_location
* location{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_4
* greet
    - utter_greet
* restaurant_search{"price": "high", "location": "mysore"}
    - slot{"location": "mysore"}
    - slot{"price": "high"}
    - action_check_location
    - slot{"location": "mysore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* email{"email": "milinangalia@gmail.com"}
    - slot{"email": "milinangalia@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - action_restart

## interactive_story_5
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"location": "chandigarh"}
    - slot{"location_ok": true}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_6
* greet
    - utter_greet
* restaurant_search{"location": "puri"}
    - slot{"location": "puri"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "cuttack"}
    - slot{"location": "cuttack"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_ok": false}
* restaurant_search{"location": "indore"}
    - slot{"location": "indore"}
    - action_check_location
    - slot{"location": "indore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* cuisine{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* price{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* email{"email": "milinangalia@gmail.com"}
    - slot{"email": "milinangalia@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_check_location
    - slot{"location": "bengaluru"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_price
* price{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* email{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"location": "chandigarh"}
    - slot{"location_ok": true}
    - utter_ask_price
* price{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* goodbye
    - action_restart
    
## interactive_story_1
* greet
    - utter_greet
* goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "high", "cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "gajulajagadeesh7@gmail.com"}
    - slot{"email": "gajulajagadeesh7@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart
    
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "low", "cuisine": "mexican", "location": "jodhpur"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "jodhpur"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart
    
## interactive_story_1
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_location
* location{"location": "jhansi"}
    - slot{"location": "jhansi"}
    - utter_ask_cuisine
* cuisine{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - utter_ask_location
* location{"location": "varanasi"}
    - slot{"location": "varanasi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart
    
## interactive_story_1
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_location
* location{"location": "jodhpur"}
    - slot{"location": "jodhpur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* affirm
    - utter_request_email
* email{"email": "gajulajagadeesh7@gmail.com"}
    - slot{"email": "gajulajagadeesh7@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye
    - action_restart
    
## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_location
* location{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - utter_ask_cuisine
* location{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* not{"not": "never"}
    - utter_goodbye
    - action_restart
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* location{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_check_location
    - slot{"location": "bengaluru"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_price
* price{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* email{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* location{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_price
* price{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* not
    - utter_goodbye
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - utter_ask_location
* location{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"location": "pune"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_search_restaurants
    - slot{"results_found": true}
    - utter_email_prompt
* email{"email": "abcd@gmail.com"}
    - slot{"email": "abcd@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - action_restart
