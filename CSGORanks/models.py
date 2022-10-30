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
        allRanks = RankModel.scan()

        def dateSort(obj):
            return obj.date

        rankList = list(allRanks)
        rankList.sort(reverse = True, key = dateSort)

        rankList = rankList[:5]

        return rankList
