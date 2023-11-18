from sys import getallocatedblocks

from django.db import models

class ranks(models.Model):
    name = models.TextField(max_length=50)
    rank = models.TextField(max_length=50)
    date = models.TextField(max_length=50)

class CSGORanks():

    def getCurrentCSGORanks(self):

        def dateSort(obj):
            return obj.date

        # Get all DB objects and sort by score
        retreivedObjects = ranks.objects.all()
        objectList = list(retreivedObjects)
        objectList.sort(reverse = True, key = dateSort)

        objectList = objectList[:5]

        return objectList
