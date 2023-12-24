from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.



class AIcontact(models.Model):
    name = models.CharField(max_length=100)
    question = models.TextField()
    answer = models.BigIntegerField(default=0)
    context = models.TextField()
    
    def __str__(self):
        return str(self.id)
    
    
class SendToCCC(models.Model):
    ip = models.CharField(max_length=100)
    red = models.IntegerField( default=0, validators=[MinValueValidator(0), MaxValueValidator(255)])
    green = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(255)])
    blue = models.IntegerField( default=0, validators=[MinValueValidator(0), MaxValueValidator(255)])
    token = models.CharField(max_length=100)
    def __str__(self):
        return str(self.id)