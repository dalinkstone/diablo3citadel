# Generated by Django 4.1.4 on 2022-12-31 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diablo3citadel', '0004_delete_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=100)),
                ('tooltipParams', models.CharField(max_length=200)),
                ('requiredLevel', models.IntegerField()),
                ('stackSizeMax', models.IntegerField()),
                ('accountBound', models.BooleanField()),
                ('flavorText', models.TextField()),
                ('flavorTextHtml', models.TextField()),
                ('typeName', models.CharField(max_length=100)),
                ('type', models.JSONField()),
                ('armor', models.TextField(default='0')),
                ('armorHtml', models.TextField(default='0')),
                ('damage', models.TextField(default='0')),
                ('dps', models.CharField(default='0', max_length=100)),
                ('damageHtml', models.TextField(default='0')),
                ('color', models.CharField(max_length=100)),
                ('isSeasonRequiredToDrop', models.BooleanField()),
                ('seasonRequiredToDrop', models.IntegerField()),
                ('slots', models.JSONField()),
                ('attributes', models.JSONField()),
                ('randomAffixes', models.JSONField()),
                ('setItems', models.JSONField()),
            ],
        ),
    ]
