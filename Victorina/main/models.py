from django.db import models

class Question(models.Model):
    question = models.CharField(max_length= 500)
    v1 = models.CharField(max_length= 500)
    v2 = models.CharField(max_length= 500)
    v3= models.CharField(max_length= 500)
    v4 = models.CharField(max_length= 500)
    
    
    CR = [
        ('1', v1),
        ('2', v2),
        ('3', v3),
        ('4', v4),
    ]
    
    correct = models.CharField(max_length=500, choises = CR)