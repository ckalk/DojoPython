# Inside models.py
from __future__ import unicode_literals

from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '%s %s %s %s' % (self.name, self.city, self.state, self.desc)


class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # There can be many ninjas to one dojo
    dojo = models.ForeignKey(Dojo, related_name = "ninjas")
    
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

