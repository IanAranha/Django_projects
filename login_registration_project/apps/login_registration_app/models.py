from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import bcrypt   
# Create your models here.

class UserManager(models.Manager):
    def loginValidation(self, postData):
        result={
            'status': True,
            'errors': [],
            'user' : None
        }
        user = self.filter(email=postData['email'])
        if len(user) < 1:
            result['status'] = False
            result['errors'].append("Email not registered. Please register first.")
        else:
            if bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
                result['user'] = user[0]
            else:
                result['status'] = False
                result['errors'].append('Password incorrect!')
        return result

    def userCreater(self, postData):
        user = self.create(
                    first_name=postData['first_name'],
                    last_name=postData['last_name'],
                    email=postData['email'],
                    password=bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
                )
        return user

    def userValidation(self, postData):
        result={
            'status': True,
            'errors' : []
        }
        if len(postData['first_name']) < 1:
            result['status'] = False
            result['errors'].append('Please enter first name')
        if len(postData['last_name']) < 1:
            result['status'] = False
            result['errors'].append('Please enter last name')
        try:
            validate_email(postData['email'])
        except ValidationError:
            result['status'] = False
            result['errors'].append('Please enter valid email')
        if len(postData['password']) < 1:
            result['status'] = False
            result['errors'].append('Please enter password')
        if len(postData['password']) < 8:
            result['status'] = False
            result['errors'].append('Password must have at least 8 characters')
        if len(postData['c_password']) < 1:
            result['status'] = False
            result['errors'].append('Please confirm password!')
        if postData['password'] != postData['c_password']:
            result['status'] = False
            result['errors'].append('Passwords do not match')
        if len(self.filter(email=postData['email'])) > 0:
            result['status'] = False
            result['errors'].append('Email in use! Please log in or register')
        return result 

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()
