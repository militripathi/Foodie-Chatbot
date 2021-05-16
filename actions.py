from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import Restarted
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import smtplib
import pprint, json
import zomatopy
import requests

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

cities = ['ahmedabad', 'bengaluru', ' bangalore', 'chennai', 'madras', 'delhi', 'new delhi', 'hyderabad',
          'kolkata', 'culcatta', 'mumbai', 'bombay', 'pune', 'agra', 'ajmer', 'aligarh', 'amravati', 'amaravati',
          'amritsar',
          'asansol', 'aurangabad', 'bareilly', 'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal',
          'bhubaneswar', 'bikaner', 'bilaspur', 'bokaro', 'chandigarh', 'coimbatore',
          'cuttack', 'dehradun', 'dhanbad', 'bhilai', 'durgapur', 'erode', 'faridabad',
          'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gwalior', 'gurgaon',
          'guwahati', 'hamirpur', 'hubli–dharwad', 'indore', 'jabalpur', 'jaipur', 'jalandhar',
          'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kakinada', 'kannur',
          'kanpur', 'kochi', 'kolhapur', 'kollam', 'kozhikode', 'kurnool', 'ludhiana',
          'lucknow', 'madurai', 'malappuram', 'mathura', 'goa', 'mangalore', 'meerut',
          'moradabad', 'mysore', 'nagpur', 'nanded', 'nashik', 'nellore', 'noida', 'patna',
          'pondicherry', 'purulia prayagraj', 'raipur', 'rajkot', 'rajahmundry', 'ranchi',
          'rourkela', 'salem', 'sangli', 'shimla', 'siliguri', 'solapur', 'srinagar', 'surat',
          'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tiruppur', 'ujjain', 'bijapur',
          'vadodara', 'varanasi', 'vasai-virar', 'vijayawada', 'vijaywada', 'visakhapatnam', 'vellore',
          'warangal']

res = ''

class ActionRestarted(Action):
	def name(self):
		return 'action_restart'

	def run(self, dispatcher, tracker, domain):
		return[Restarted()]

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def fetch(self, loc='banglore', cuisine='north indian', price='high'):

        # adjust the price range
        price_min = 0
        price_max = 99999
        if price == 'low':
            price_max = 300
        elif price == 'mid':
            price_min = 300
            price_max = 700
        elif price == 'high':
            price_min = 700
        else:
            price_min = 300
            price_max = 9999

        # provide API key and initialise a 'zomato app' object
        config = {"user_key": "4734a24a9caf5cd3ae0a0e9161e66212"}
        zomato = zomatopy.initialize_app(config)
        cuisines_dict = {'mexican': 73, 'chinese': 25, 'cafe': 30, 'italian': 55, 'american': 1, 'north indian': 50,
                         'south indian': 85, 'north': 50, 'thai': 95, 'indian': 80}

        # get_location gets the lat-long coordinates of 'loc'
        loc_detail = zomato.get_location(loc, 1)
        loc_detail = json.loads(loc_detail)
        if loc_detail['status'] == 'success':
            data = zomato.restaurant_search(query='', latitude=loc_detail['location_suggestions'][0]['latitude'],
                                            longitude=loc_detail['location_suggestions'][0]['longitude'],
                                            cuisines=str(cuisines_dict.get(cuisine)), limit=100)
            data = json.loads(data)
            global res
            if data['results_found'] > 0:
                added = 0
                res =''
                for i in sorted(data['restaurants'], key=lambda x: x['restaurant']['user_rating']['aggregate_rating'], reverse=True):
                    if i['restaurant']['average_cost_for_two'] > price_min and i['restaurant'][
                        'average_cost_for_two'] < price_max and added < 5:
                        res = res + "\n\n" + str(i['restaurant']['name']) + "\nin " + str(
                            i['restaurant']['location']['address']) + "\nhas been rated :" + str(
                            i['restaurant']['user_rating']['aggregate_rating']) + "\n"
                        added = added + 1
                if len(res) == 0:
                    res = "No Results Found"
                    return res
                else:
                    return ("Showing you top rated restaurants: \n\n" + res)
            else:
                res = "No Results Found"
                return res
        else:
            return ("No Results Found")

    def run(self, dispatcher, tracker, domain):
        # config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
        # zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        if loc == None:
            return dispatcher.utter_message('Location got is None')
        if loc.lower() not in cities:
            dispatcher.utter_message("We don't operate in your location")
            return [AllSlotsReset()]
        cuisine = tracker.get_slot('cuisine')
        price = tracker.get_slot('price')
        res1 = ''
        res = ''
        if cuisine == None or price == None:
            dispatcher.utter_message("I didn't get all details, deafault results will be shown")
            cuisine = 'north'
            price = 'mid'
            return [SlotSet("results_found", False)]
        else:
            res = self.fetch(loc, cuisine, price)
            dispatcher.utter_message(res)
            if (res == "No Results Found"):
                return [SlotSet("results_found", False)]
            else:
                return [SlotSet("results_found", True)]



class ActionCheckLocation(Action):

    def name(self):
        return 'action_check_location'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        cities = ['ahmedabad', 'bengaluru', ' bangalore', 'chennai', 'madras', 'delhi', 'new delhi', 'hyderabad',
                  'kolkata', 'culcatta', 'mumbai', 'bombay', 'pune', 'agra', 'ajmer', 'aligarh', 'amravati',
                  'amaravati', 'amritsar',
                  'asansol', 'aurangabad', 'bareilly', 'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal',
                  'bhubaneswar', 'bikaner', 'bilaspur', 'bokaro', 'chandigarh', 'coimbatore',
                  'cuttack', 'dehradun', 'dhanbad', 'bhilai', 'durgapur', 'erode', 'faridabad',
                  'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gwalior', 'gurgaon',
                  'guwahati', 'hamirpur', 'hubli–dharwad', 'indore', 'jabalpur', 'jaipur', 'jalandhar',
                  'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kakinada', 'kannur',
                  'kanpur', 'kochi', 'kolhapur', 'kollam', 'kozhikode', 'kurnool', 'ludhiana',
                  'lucknow', 'madurai', 'malappuram', 'mathura', 'goa', 'mangalore', 'meerut',
                  'moradabad', 'mysore', 'nagpur', 'nanded', 'nashik', 'nellore', 'noida', 'patna',
                  'pondicherry', 'purulia prayagraj', 'raipur', 'rajkot', 'rajahmundry', 'ranchi',
                  'rourkela', 'salem', 'sangli', 'shimla', 'siliguri', 'solapur', 'srinagar', 'surat',
                  'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tiruppur', 'ujjain', 'bijapur',
                  'vadodara', 'varanasi', 'vasai-virar', 'vijayawada', 'vijaywada', 'visakhapatnam', 'vellore',
                  'warangal']

        cities_all = ['mumbai', 'delhi', 'kolkata', 'chennai', 'bengaluru','bangalore', 'hyderabad', 'ahmedabad', 'surat', 'pune',
                      'kanpur','madras','new delhi', 'culcatta', 'bombay',
                      'indore', 'jaipur', 'vadodara', 'nagpur', 'lucknow', 'patna', 'vishakapatnam', 'bhopal',
                      'gwalior', 'jabalpur',
                      'aurangabad', 'gandhinagar', 'vellore', 'madurai[8]', 'aligarh', 'kochi', 'coimbatore[8]',
                      'vijayawada',
                      'tiruchirapalli', 'nashik', 'rajkot', 'solapur', 'anand', 'ludhiana', 'agra', 'meerut',
                      'thiruvananthapuram', 'kozhikode', 'faridabad', 'varanasi', 'jamshedpur', 'allahabad', 'amritsar',
                      'dhanbad',
                      'gorakhpur', 'hubli-dharwad', 'bhavnagar', 'raipur', 'mysore', 'thrissur', 'mangalore', 'guntur',
                      'bhubaneswar',
                      'amravati', 'srinagar', 'bhilai', 'warangal', 'tirunelveli', 'nellore', 'ranchi', 'guwahati',
                      'aurangabad',
                      'chandigarh', 'patiala', 'jodhpur', 'pondicherry', 'salem', 'dindigul', 'dehradun', 'hajipur',
                      'kollam', 'sangli',
                      'jamnagar', 'jammu', 'kurnool', 'roorkee', 'kannur', 'tiruvannamalai', 'etawah', 'rishikesh',
                      'ahmedabad', 'bengaluru', ' bangalore', 'chennai', 'madras', 'delhi', 'new delhi', 'hyderabad',
                  'kolkata', 'culcatta', 'mumbai', 'bombay', 'pune', 'agra', 'ajmer', 'aligarh', 'amravati',
                  'amaravati', 'amritsar',
                  'asansol', 'aurangabad', 'bareilly', 'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal',
                  'bhubaneswar', 'bikaner', 'bilaspur', 'bokaro', 'chandigarh', 'coimbatore',
                  'cuttack', 'dehradun', 'dhanbad', 'bhilai', 'durgapur', 'erode', 'faridabad',
                  'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gwalior', 'gurgaon',
                  'guwahati', 'hamirpur', 'hubli–dharwad', 'indore', 'jabalpur', 'jaipur', 'jalandhar',
                  'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kakinada', 'kannur',
                  'kanpur', 'kochi', 'kolhapur', 'kollam', 'kozhikode', 'kurnool', 'ludhiana',
                  'lucknow', 'madurai', 'malappuram', 'mathura', 'goa', 'mangalore', 'meerut',
                  'moradabad', 'mysore', 'nagpur', 'nanded', 'nashik', 'nellore', 'noida', 'patna',
                  'pondicherry', 'purulia prayagraj', 'raipur', 'rajkot', 'rajahmundry', 'ranchi',
                  'rourkela', 'salem', 'sangli', 'shimla', 'siliguri', 'solapur', 'srinagar', 'surat',
                  'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tiruppur', 'ujjain', 'bijapur',
                  'vadodara', 'varanasi', 'vasai-virar', 'vijayawada', 'vijaywada', 'visakhapatnam', 'vellore',
                  'warangal']

        cities_lower = [x.lower() for x in cities]

        if loc.lower() in cities_all:
            if loc.lower() not in cities_lower:
                dispatcher.utter_message("Sorry, we don’t operate in this city. Can you please specify some other location")
                return [SlotSet('location', None), SlotSet("location_ok", False)]
            else:
                return [SlotSet('location', loc.lower()), SlotSet("location_ok", True)]
        else:
            dispatcher.utter_message("Sorry, didn’t find any such location. Can you please tell again?")
            return [SlotSet('location', None), SlotSet("location_ok", False)]

class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'

    def fetch(self, loc='delhi', cuisine='north indian', price='high'):

        # adjust the price range
        price_min = 0
        price_max = 99999
        if price == 'low':
            price_max = 300
        elif price == 'mid':
            price_min = 300
            price_max = 700
        elif price == 'high':
            price_min = 700
        else:
            price_min = 300
            price_max = 9999

        # provide API key and initialise a 'zomato app' object
        config = {"user_key": "d289054ac47b70565a76b4fc845501dc"}
        zomato = zomatopy.initialize_app(config)
        cuisines_dict = {'mexican': 73, 'chinese': 25, 'cafe': 30, 'italian': 55, 'american': 1, 'north indian': 50,
                         'south indian': 85, 'north': 50, 'thai': 95, 'indian': 80}

        # get_location gets the lat-long coordinates of 'loc'
        loc_detail = zomato.get_location(loc, 1)
        loc_detail = json.loads(loc_detail)
        if loc_detail['status'] == 'success':
            lat = loc_detail['location_suggestions'][0]['latitude']
            lon = loc_detail['location_suggestions'][0]['longitude']
            data = zomato.restaurant_search(query='', latitude=lat, longitude=lon,
                                            cuisines=str(cuisines_dict.get(cuisine)), limit=200)
            data = json.loads(data)
            global res
            if data['results_found'] > 0:
                added = 0
                res = ''
                for i in sorted(data['restaurants'], key=lambda x: x['restaurant']['user_rating']['aggregate_rating'], reverse=True):
                    if i['restaurant']['average_cost_for_two'] > price_min and i['restaurant'][
                        'average_cost_for_two'] < price_max and added < 10:
                        res = res + "\n\n Restaurant Name: " + str(i['restaurant']['name']) + "\n Restaurant locality address :" + str(
                            i['restaurant']['location']['address']) + "\n Average budget for two people: " + str(
                            i['restaurant']['average_cost_for_two']) + "\nZomato user rating :" + str(
                            i['restaurant']['user_rating']['aggregate_rating'])
                        added = added + 1
                if len(res) == 0:
                    return "can't get anything with your preferances"

                return "Showing you top rated restaurants: \n\n " + res
            else:
                return "can't retrive data properly"

        else:
            return "results not found..!!"

    def run(self, dispatcher, tracker, domain):
        # config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
        # zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price = tracker.get_slot('price')
        res = self.fetch(loc, cuisine, price)
        to_user = tracker.get_slot('email')
        if to_user == None:
            to_user = 'milinangalia@gmail.com'
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        try:
            s.login("foodiechatbot4@gmail.com", "upgrad123")
        except:
            dispatcher.utter_message("Bad credentials, Can't send email your preferences deleted")
            return [AllSlotsReset()]

        message = "The details of all the restaurants you inquried \n \n"
        message = message + res
        subject = 'Foodie Chatbot:Restaurant List'
        msg = MIMEMultipart()
        msg['From'] = "foodiechatbot4@gmail.com"
        msg['TO'] = to_user
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        text = msg.as_string()
        try:
            s.sendmail("foodiechatbot4@gmail.com", str(to_user), text)
            s.quit()
            return [AllSlotsReset()]
        except:
            dispatcher.utter_message("Can't send the email. deleted your preferances")
            return [AllSlotsReset()]
