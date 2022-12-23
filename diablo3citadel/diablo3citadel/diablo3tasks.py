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

    #Here we are using the itemTypeSlug in order to return all of the items that are associated
    #with that specific itemTypeSlug. For example, the sword2h slug has like ~50 different 2h-sword items
    #that are associated with it. In order to get the one that we want we would need to pass a keyword
    #just like in the get_item_type_index function. The value we would want to use for the icon
    #and for the specific itemTypeSlug is after the path, like in the previous function
    #I think passing a keyword here or some type of an exchange with the item_type_index function would
    #be very valuable

    return print(item_type)





