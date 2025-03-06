from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=50, blank=False, null=False)
    short_description=models.CharField(max_length=100, blank=False,null=False)
    description =models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    date=models.DateField(default=now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True )
    

    def __str__(self):
        return self.title