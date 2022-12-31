from django.db import models

# Create your models here.
class characterClass(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    skillCategories = models.JSONField()
    skills = models.JSONField()
    passive = models.JSONField()

    def __str__(self):
        return self.id

class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    skill = models.JSONField()
    runes = models.JSONField()

    def __str__(self):
        return self.id

class ItemTypeIndex(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=200)

    def __str__(self):
        return self.id

class ItemType(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=200)
    path = models.CharField(max_length=200)

    def __str__(self):
        return self.id

class Item(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    tooltipParams = models.CharField(max_length=200)
    requiredLevel = models.IntegerField()
    stackSizeMax = models.IntegerField()
    accountBound = models.BooleanField()
    flavorText = models.TextField(default='None', editable=True)
    flavorTextHtml = models.TextField(default='None', editable=True)
    typeName = models.CharField(max_length=100)
    type = models.JSONField()
    armor = models.TextField(default='0', editable=True)
    armorHtml = models.TextField(default='0', editable=True)
    damage = models.TextField(default='0', editable=True)
    dps = models.CharField(max_length=100, default='0', editable=True)
    damageHtml = models.TextField(default='0', editable=True)
    color = models.CharField(max_length=100)
    isSeasonRequiredToDrop = models.BooleanField()
    seasonRequiredToDrop = models.IntegerField()
    slots = models.JSONField()
    attributes = models.JSONField()
    randomAffixes = models.JSONField()
    setItems = models.JSONField()

    def __str__(self):
        return self.id
