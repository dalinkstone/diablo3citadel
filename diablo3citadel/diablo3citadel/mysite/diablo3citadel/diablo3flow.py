from diablo3citadel.diablo3tasks import get_item_type_index, get_item_type


def main_flow():
    print('Started the main_flow')

    item_type_index = get_item_type_index()

    list_of_values = []

    for item in item_type_index:
        list_of_values += list(item.values())

    return list_of_values



