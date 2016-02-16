from __future__ import unicode_literals

from django.db import models


class Region(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=254, null=False)

    def __unicode__(self):
        return '{}: {}'.format(self.name, self.id)


class SolarSystem(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=254, null=True)

    def __unicode__(self):
        return '{}: {}'.format(self.name, self.id)


class MarketType(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=254, null=True)
    market_group = models.IntegerField(null=False)

    def __unicode__(self):
        return '{}: {}'.format(self.name, self.id)
