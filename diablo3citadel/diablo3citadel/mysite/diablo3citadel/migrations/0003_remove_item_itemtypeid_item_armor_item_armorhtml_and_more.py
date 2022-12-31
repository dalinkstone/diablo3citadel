# Generated by Django 4.1.4 on 2022-12-31 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diablo3citadel', '0002_characterclass_itemtype_skill_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='itemTypeId',
        ),
        migrations.AddField(
            model_name='item',
            name='armor',
            field=models.TextField(default='0'),
        ),
        migrations.AddField(
            model_name='item',
            name='armorHtml',
            field=models.TextField(default='0'),
        ),
        migrations.AlterField(
            model_name='item',
            name='damage',
            field=models.TextField(default='0'),
        ),
        migrations.AlterField(
            model_name='item',
            name='damageHtml',
            field=models.TextField(default='0'),
        ),
        migrations.AlterField(
            model_name='item',
            name='dps',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
