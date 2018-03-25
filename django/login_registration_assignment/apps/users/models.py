from __future__ import unicode_literals

from django.db import models

# the "re" module will let us perform some regular expression operations
import re
# Check for Valid Email format
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# NAME_REGEX Check letters only, at least 2 characters /^[a-zA-Z]{2,}$/
NAME_REGEX = re.compile(r'^[a-zA-Z]{2,}$')
# PASSWORD_REGEX at least 8 characters /^.{8,}$/
PASSWORD_REGEX = re.compile(r'^.{8,}$')

# Bcrypt hashing
import bcrypt

class UserManager(models.Manager):
    def reg_validator(self, postData):

        errors = {}

        #validate first name
        if len(postData['first_name']) < 1:
            errors["first name reg"] = "You must enter your first name"
        elif not NAME_REGEX.match(postData['first_name']):
            errors["first name reg"] = "Invalid characters or not at least 2 characters in first name"

        #validate last name
        if len(postData['last_name']) < 1:
            errors["last name reg"] = "You must enter your last name"
        elif not NAME_REGEX.match(postData['last_name']):
            errors["last name reg"] = "Invalid characters or not at least 2 characters in last name"

        #validate email
        if len(postData['email']) < 1:
            errors["email reg"] = "You must enter an email address"
        elif not EMAIL_REGEX.match(postData['email']):
            errors["email reg"] = "Invalid email address"
        elif self.filter(email = postData['email']):
            errors["email reg"] = "Email address already in use"

        #validate password
        if len(postData['password']) < 1:
            errors["password reg"] = "You must enter a password"
        elif not PASSWORD_REGEX.match(postData['password']):
             errors["password reg"] = "Passwords must be 8 characters or more"

        #validate confirm_password
        if len(postData['confirm_password']) < 1:
            errors["confirm password reg"] = "You must confirm password"
        elif postData['confirm_password'] != postData['password']:
            errors["confirm password reg"] = "Password and Confirm Password must match"
   
        return errors

    #login form validator
    def login_validator(self, postData):

        errors = {}

        #validate email
        if len(postData['email']) < 1:
            errors["email login"] = "You must enter an email address"
            return errors
        if not self.filter(email = postData['email']):
            errors["email login"] = "Email address does not exist"
            return errors

        #validate password
        if len(postData['password']) < 1:
            errors["password login"] = "You must enter your password"
        elif not bcrypt.checkpw(postData['password'].encode(), self.get(email = postData['email']).password.encode()):
             errors["password login"] = "Incorrect email/password combination"

        return errors

    # create a user 
    def create_user(self, clean_data):
        hashed_pw = bcrypt.hashpw(clean_data["password"].encode(), bcrypt.gensalt())
        # hash1 = bcrypt.hashpw('test'.encode(), bcrypt.gensalt())
        return self.create(
            first_name=clean_data["first_name"], 
            last_name=clean_data["last_name"], 
            email=clean_data["email"], 
            password=hashed_pw
        )

       
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # *************************

    # Connect an instance of UserManager to our User model overwriting the old hidden objects key with a new one with extra properties
    objects = UserManager()
    # *************************
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
