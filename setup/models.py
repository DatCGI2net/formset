from __future__ import unicode_literals

from django.db import models
#from imghdr import what

# Create your models here.


class Setup(models.Model):
    description = models.CharField(max_length=100)
    
    def get(self, what):
        print 'what:', what
        
        return self.description
    
class Specification(models.Model):
    setup = models.ForeignKey(Setup, related_name="target_specs")
    result = models.FloatField(default=0.)
    
    