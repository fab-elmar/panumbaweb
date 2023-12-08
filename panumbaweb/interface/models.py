from django.db import models

# Create your models here.



class AIcontact(models.Model):
    name = models.CharField(max_length=100)
    question = models.TextField()
    answer = models.IntegerField(default=0)
    context = models.TextField()
    
    def __str__(self):
        return str(self.id)