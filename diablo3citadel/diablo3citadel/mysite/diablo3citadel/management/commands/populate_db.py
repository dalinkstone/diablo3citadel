from django.core.management.base import BaseCommand
from diablo3citadel.models import ItemTypeIndex, ItemType
from diablo3citadel.diablo3flow import main_flow
from diablo3citadel.diablo3tasks import get_item_type_index, get_item_from_index, get_item_type, get_item
import json

class Command(BaseCommand):
    args = ''
    help = 'This command populates the PostgreSQL database with the ItemTypeIndex values'

    def _create_rows(self):
        values = main_flow()
        id_counter = 0
        name_counter = 1
        path_counter = 2

        while path_counter < len(values):
            input_row = ItemTypeIndex(id=values[id_counter], name=values[name_counter], path=values[path_counter])
            input_row.save()
            id_counter += 3
            name_counter += 3
            path_counter += 3

        item_type_index = get_item_type_index()

        item_type_slug_list = get_item_from_index(item_type_index)
        
        for item in item_type_slug_list:
            item_type_list = get_item_type(item)
            item_types = json.loads(item_type_list)
            for value in item_types:
                item_type_input_row = ItemType(id=value['id'], name=value['name'], slug=value['slug'], icon=value['icon'], path=value['path'])
                item_type_input_row.save()

        for item in item_type_slug_list:
            item_type_list = get_item_type(item)
            item_types = json.loads(item_type_list)
            for value in item_types:
                item_row = value['slug']+'-'+value['id']
                item_value = get_item(item_row)
                

    def handle(self, *args, **options):
        self._create_rows()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with the rows.'))

        
