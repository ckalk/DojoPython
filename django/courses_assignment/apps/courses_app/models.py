from __future__ import unicode_literals

from django.db import models


class CourseManager(models.Manager):
    def basic_validator(self, postData):

        errors = {}

        if len(postData['name']) < 6:
            errors["name"] = "Course name should be more than 5 characters"

        if len(postData['desc']) < 16:
            errors["desc"] = "Description should be more than 15 characters"
    
        return errors


    def create_course(self, new_name, new_desc):
        course = self.create(name=new_name, desc=new_desc)
        return course
        
class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # *************************

    # Connect an instance of CourseManager to our Course model overwriting the old hidden objects key with a new one with extra properties
    objects = CourseManager()
    # *************************
    def __str__(self):
        return '%s %s' % (self.name, self.desc)