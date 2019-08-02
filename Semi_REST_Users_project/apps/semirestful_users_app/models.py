from django.db import models
import re

# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basicValidator(self, postData):
        errors={}
        if len(postData['first_name']) < 1:
            errors['first_name'] = 'First name cannot be blank'
        if len(postData['last_name']) < 1:
            errors['last_name'] = 'Last name cannot be blank'
        if len(postData['email']) < 1:
            errors['email'] = 'Email cannot be blank'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Email not valid'
        return errors

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()