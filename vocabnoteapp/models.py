from django.db import models

class User(models.Model):
    Name = models.CharField(max_length=100)
    Email  = models.EmailField(max_length=100)
    Gender = models.CharField(max_length=100)





"""
class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()



    class Meta:
        unique_together = ('album', 'order')


    def __unicode__(self):
        return '%d: %s' % (self.order, self.title)"""

