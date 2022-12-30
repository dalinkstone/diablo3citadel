from diablo3citadel.diablo3token import get_token
import requests
import json


def get_item_type_index():

    token = get_token()

    item_type_index_uri = f'https://us.api.blizzard.com/d3/data/item-type?access_token={token}'

    item_type_index_response = requests.get(url=item_type_index_uri)

    item_type_index = item_type_index_response.json()

    return item_type_index


def get_item_from_index(values_list):

    path_list = 0
    itemTypeIndexSlugList = []
    itemTypeIndexSlug = [item['path'] for item in values_list]

    while path_list < len(itemTypeIndexSlug):
        itemTypeIndexSlugList += itemTypeIndexSlug[path_list].rsplit('/', 1)
        path_list += 1

    remove_item_type = 0
    while remove_item_type < len(itemTypeIndexSlugList):
        itemTypeIndexSlugList.pop(remove_item_type)
        remove_item_type += 1
    
    return itemTypeIndexSlugList


def get_item_type(
    item_type_slug: str
):

    token = get_token()

    item_type_uri = f'https://us.api.blizzard.com/d3/data/item-type/{item_type_slug}?access_token={token}'

    item_type_response = requests.get(url=item_type_uri)

    item_type = item_type_response.text

    return item_type

def get_item(
    item_slug_and_id: str
):
    token = get_token()

    item_uri = f'https://us.api.blizzard.com/d3/data/item/{item_slug_and_id}?access_token={token}'

    item_response = requests.get(url=item_uri)

    items = item_response.text

    items = json.loads(items)

    return items


#
# Update these functionalities so we can have a person input their profile name and the app will run the name through the API
# Retrieve the items and make it all look really pretty
# Then we can compare the heroes items against better item sets for the specific character class




