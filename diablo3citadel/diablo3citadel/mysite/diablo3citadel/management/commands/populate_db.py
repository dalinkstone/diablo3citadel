from django.core.management.base import BaseCommand
from diablo3citadel.models import ItemTypeIndex
from diablo3citadel.diablo3flow import main_flow

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

    def handle(self, *args, **options):
        self._create_rows()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with the rows.'))

        
