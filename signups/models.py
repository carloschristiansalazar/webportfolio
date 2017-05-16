from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.

class SignUp (models.Model):
    first_name = models.CharField(max_length=120,null=True,blank = True)
    last_name = models.CharField(max_length=120,null=True,blank = True)
    timestamp = models.DateTimeField(auto_now_add=True , auto_now = False)
    
    def __unicode__(self):
        return smart_unicode(self.first_name , self.last_name)