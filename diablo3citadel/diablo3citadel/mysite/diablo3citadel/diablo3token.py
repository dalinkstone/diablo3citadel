import requests 
import json
from diablo3citadel.keys import get_credentials
from datetime import date
import unittest as ut 

#This is going to get a token that is required to be used to interact with the api
#The token request requires 3 parameters:
#   :params
#       token_url: This is the url of the token site
#       auth: the authorization is the client credentials, these are accessed through the blizzard site 
#               upon creation of a client, you will see a prompt UI that displays a Client ID and a Client Secret
#               both are required to be passed to the site in order to receive a token in response
#       token_data: The token data is passed as a dict object with the value being 'grant_type' and the attribute 'client_credentials'
#                   I'm not entirely sure how it works, but it appears to identify the auth as being a 'grant_type' and then 
#                   the site knows what 'auth' is being passed
#                       This logic implies there is something like 'blizzard_admin' grant type or something similar to a tier structure

def get_token():

    credentials = get_credentials()
    token_url = 'https://oauth.battle.net/token'
    token_data = {'grant_type': 'client_credentials'}
    
    token_request_response = requests.post(token_url, auth=credentials, data=token_data)

    token_response = json.loads(token_request_response.text)

    return token_response["access_token"]


