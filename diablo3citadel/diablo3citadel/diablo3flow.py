import requests
import json
import unittest as ut
from diablo3citadel.diablo3tasks import get_item_type_index
from diablo3citadel.mysite.diablo3citadel.models import ItemTypeIndex

# We need to store the client credentials and then use them as a f'{string}' in the url that can then be passed to the post request 
# To get the token we should use the 'auth' parameter to keep things separated, similar to how we are already doing it
# For the get requests for item data/act data etc, we will need to parse the token out of the post request response, and then
# store that token somehow so we can sue it in a f'{string}' for the get requests as well. I'm not sure how to do the 'access_token'
# part of the url. I think we should add some functionality to that, so it is more flexible than it currently is
# We will need to do lots of 'if' and validation loops to ensure that we aren't getting a new token every single time we 
# run the script. And to make sure that we are using the correct client credentials
# But in order to do the get request, you need the access token, and im not sure how to inject it into the get request
# as an actual parameter. So far we just need to explicitly include the access token portion of the url in the url that we are
# going to pass to the get request

def main_flow():
    print('Started the main_flow')

    item_type_index = get_item_type_index()

    return print(item_type_index)

main_flow()

