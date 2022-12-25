from django.core.management.base import BaseCommand
from diablo3citadel.models import ItemTypeIndex
from diablo3citadel.diablo3flow import main_flow

class Command(BaseCommand):
    args = ''
    help = 'This command populates the PostgreSQL database with the ItemTypeIndex values'

    def _get_values(self):
        values = main_flow()
        id_counter = 0
        name_counter = 1
        path_counter = 2
        
