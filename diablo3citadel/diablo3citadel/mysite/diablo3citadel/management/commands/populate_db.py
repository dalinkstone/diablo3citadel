from django.core.management.base import BaseCommand
from diablo3citadel.models import ItemTypeIndex, ItemType, Item
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
        
        itemTypeSlugList = get_item_from_index(item_type_index)

        for item in itemTypeSlugList:
            item_type_values_list = get_item_type(item)
            item_type_values = json.loads(item_type_values_list)
            for value in item_type_values:
                item_row = value['slug']+'-'+value['id']
                print(item_row)
                if ('Ethereal' in item_row) or ('town-portal-stone-TownPortalStone' in item_row) or ('a-gift-ConsoleFriendGift' in item_row) or ('1h-mystery-weapon-PH_1HWeapon' in item_row) or ('2h-mystery-weapon-PH_2HWeapon' in item_row):
                    continue

                item_values = get_item(item_row)
                item_value = json.loads(item_values)
                

                if ('flavorText' in item_value) == False:
                    item_value['flavorText'] = 'None'
                    item_value['flavorTextHtml'] = 'None'

                if ('armor' in item_value) == False:
                    item_value['armor'] = '0'
                    item_value['armorHtml'] = '0'

                if ('damage' in item_value) == False:
                    item_value['damage'] = '0'
                    item_value['damageHtml'] = '0'
                    item_value['dps'] = '0'

                if ('attributes' in item_value) == False:
                    item_value['attributes'] = {'None': 'None'}

                if ('randomAffixes' in item_value) == False:
                    item_value['randomAffixes'] = {'None': 'None'}

                slots = item_value['slots']
                slot_dict = {}
                sd = range(len(slots))
                for int in sd:
                    slot_dict[int] = slots[int]
                setItems = item_value['setItems']
                setItems_dict = {}
                si = range(len(setItems))
                for int in si:
                    setItems_dict[int] = setItems[int]
                item_value_row = Item(id=item_value['id'], slug=item_value['slug'], name=item_value['name'], icon=item_value['icon'], tooltipParams=item_value['tooltipParams'], requiredLevel=item_value['requiredLevel'], stackSizeMax=item_value['stackSizeMax'], accountBound=item_value['accountBound'], flavorText=item_value['flavorText'], flavorTextHtml=item_value['flavorTextHtml'], typeName=item_value['typeName'], type=item_value['type'], armor=item_value['armor'], armorHtml=item_value['armorHtml'], damage=item_value['damage'], dps=item_value['dps'], damageHtml=item_value['damageHtml'], color=item_value['color'], isSeasonRequiredToDrop=item_value['isSeasonRequiredToDrop'], seasonRequiredToDrop=item_value['seasonRequiredToDrop'], slots=slot_dict, attributes=item_value['attributes'], randomAffixes=item_value['randomAffixes'], setItems=setItems_dict)
                item_value_row.save()


    def handle(self, *args, **options):
        self._create_rows()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with the rows.'))

        
