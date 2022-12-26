from diablo3citadel.diablo3token import get_token
import requests
import json


def get_item_type_index():

    token = get_token()

    item_type_index_uri = f'https://us.api.blizzard.com/d3/data/item-type?access_token={token}'

    item_type_index_response = requests.get(url=item_type_index_uri)

    item_type_index = item_type_index_response.json()

    return item_type_index


def get_item_from_index(item_type_index, item_name: str):

    get_itemTypeIndexSlug = [item['path'] for item in item_type_index if item['name'] == {item_name}]

    split_result = get_itemTypeIndexSlug[0].rsplit('/', 1)

    return print(split_result[1])


def get_item_type(
    item_type_slug: str
):

    token = get_token()

    item_type_uri = f'https://us.api.blizzard.com/d3/data/item-type/{item_type_slug}?access_token={token}'

    item_type_response = requests.get(url=item_type_uri)

    item_type = item_type_response.text

    return print(item_type)

#
# Update these functionalities so we can have a person input their profile name and the app will run the name through the API
# Retrieve the items and make it all look really pretty
# Then we can compare the heroes items against better item sets for the specific character class




