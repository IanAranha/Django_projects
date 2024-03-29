from __future__ import unicode_literals
from django.db import models

# Create your models here.
class BlogManager(models.Manager):
    def basicValidator(self, postData):
        errors={}
        if len(postData['name']) < 5:
            errors['name'] = 'Blog name should be at least 5 characters'
        if len(postData['desc']) < 10:
            errors['desc'] = 'Blog desc should be at least 10 characters'
        return errors

class Blog(models.Model):
    name=models.CharField(max_length=255)
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    # ONE TO MANY RELATIONSHIP KEY
    blog = models.ForeignKey(Blog, related_name='comments')
    objects=BlogManager()

class Admin(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    # MANY TO MANY RELATIONSHIP KEY
    blogs=models.ManyToManyField(Blog, related_name='admins')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)