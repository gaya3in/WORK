from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=False,blank=False)

    def __str__(self):
        return self.name

WORK_CHOICES = (
    ("Youtube", "Youtube"),
    ("Instagram", "Instagram"),
    ("Other", "Other")
)
    
class Work(models.Model):
    link = models.TextField(max_length=1000,unique=True)
    type = models.CharField(max_length=100,choices=WORK_CHOICES,default="Youtube")


    def __str__(self):
        return self.link
    
class Artist(models.Model):
    name = models.CharField(max_length=50,unique=True)
    work = models.ManyToManyField(Work)

    
    def __str__(self):
        return self.name
