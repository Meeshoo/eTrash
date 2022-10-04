from sys import getallocatedblocks
from django.conf import settings
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

class RankModel(Model):
    class Meta:
        table_name = settings.CSGORANKS_TABLE_NAME
        region = settings.CSGORANKS_REGION
    date = UnicodeAttribute(hash_key=True)
    username = UnicodeAttribute()
    rank = UnicodeAttribute()

class CSGORanks():

    def getCurrentCSGORanks(self):
        allRanks = RankModel.scan(limit=5)

        return allRanks
