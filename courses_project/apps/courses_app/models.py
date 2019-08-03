from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def basicValidator(self, postData):
        errors={}
        if len(postData['name']) < 1:
            errors['name'] = 'Please enter a course name!'
        if len(postData['desc']) < 1:
            errors['desc'] = 'Please enter a course description.'
        return errors

class Course(models.Model):
    name=models.CharField(max_length=255)
    desc=models.TextField(max_length=2000)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=CourseManager()