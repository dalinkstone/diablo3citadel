# Generated by Django 4.1.4 on 2022-12-31 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diablo3citadel', '0003_remove_item_itemtypeid_item_armor_item_armorhtml_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
    ]
