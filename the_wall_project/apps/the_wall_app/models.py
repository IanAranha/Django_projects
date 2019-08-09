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
            'user': None
        }
        try:
            validate_email(postData['email'])
        except ValidationError:
            result['status'] = False
            result['errors'].append('Please enter valid email')
        if result['status'] == True:
            this_user=self.filter(email=postData['email'])
            if len(this_user) < 1:
                result['status'] = False
                result['errors'].append("Email has not been registered. Please <a href='/register'>register</a> now")
            else:
                if bcrypt.checkpw(postData['password'].encode(), this_user[0].password.encode()):
                    result['user'] = this_user[0]
                else:
                    result['status'] = False
                    result['errors'].append('Incorrect password')
        return result

    def userCreator(self, postData):
        user=self.create(
            first_name=postData['first_name'],
            last_name=postData['last_name'],
            email=postData['email'],
            password=bcrypt.hashpw(postData['password'].encode(),bcrypt.gensalt()),
        )
        return user

    def userValidation(self, postData):
        result={
            'status': True,
            'errors': []
        }
        if len(postData['first_name']) < 1:
            result['status']=False
            result['errors'].append('First name cannot be blank')
        elif len(postData['first_name']) < 2:
            result['status']=False
            result['errors'].append('First name must contain 2 or more characters') 
        elif not postData['first_name'].isalpha():
            result['status']=False
            result['errors'].append('First name can contain only letters')
        if len(postData['last_name']) < 1:
            result['status']=False
            result['errors'].append('Last name cannot be blank')
        elif len(postData['last_name']) < 2:
            result['status']=False
            result['errors'].append('Last name must contain 2 or more characters') 
        elif not postData['last_name'].isalpha():
            result['status']=False
            result['errors'].append('Last name can contain only letters')
        try:
            validate_email(postData['email'])
        except ValidationError:
            result['status'] = False
            result['errors'].append('Please enter valid email')
        if len(self.filter(email=postData['email'])) > 0:
            result['status'] = False
            result['errors'].append("Email already registered. Please <a href='/login'>log-in</a>")
        if len(postData['password']) < 1:
            result['status']=False
            result['errors'].append('Password cannot be blank')
        elif len(postData['password']) < 8:
            result['status']=False
            result['errors'].append('Password must contain at least 8 characters')
        if postData['password'] != postData['c_password']:
            result['status']=False
            result['errors'].append('Passwords do not match')
        if len(postData['c_password']) < 1:
            result['status']=False
            result['errors'].append('Please confirm password')
        return result
        

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

class MessageManager(models.Manager):

    def messageCreator(self, postData):
        message=self.create(
            message=postData['message'],
            user=User.objects.get(id=postData['id'])
        )
        return message

    def postMessage(self, postData):
        result = {
            'status' : True,
        }
        if len(postData['message']) < 1:
            result['status']=False
        return result   

class Message(models.Model):
    message=models.TextField(max_length=2000)
    user=models.ForeignKey(User, related_name='messages')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=MessageManager()




class CommentManager(models.Manager):
    
    def postComment(self, postData):
        result = {
            'status' : True,
        }
        if len(postData['comment']) < 1:
            result['status']=False
        return result

class Comment(models.Model):
    comment=models.TextField(max_length=1000)
    user=models.ForeignKey(User, related_name='u_comments')
    message=models.ForeignKey(Message, related_name='m_comments')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=CommentManager()
