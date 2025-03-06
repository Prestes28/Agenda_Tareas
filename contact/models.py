from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
    
    name= models.CharField( max_length=50, blank=False, null=False)
    last_name =models.CharField(max_length=50, blank=False, null=False)
    tel1=models.CharField(default='+54',max_length=50,blank=False, null=False)
    tel2=models.CharField(max_length=50,blank=True, null=True)
    company=models.CharField(max_length=50,blank=True, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    def __str__(self):
        return self.name

