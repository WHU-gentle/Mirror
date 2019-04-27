from django.db import models

# Create your models here.
class User(models.Model):
    '''用户'''
    
    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)
    gender = (('mail','男'),('femail','女'),)
    sex = models.CharField(max_length=32, choices=gender, default='女')
    email = models.EmailField(unique=True)
    height = models.FloatField()
    weight = models.FloatField()

    def __str__(self):
        return self.name


