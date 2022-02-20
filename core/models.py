from django.db import models
import random

def gen_pk():
    num = random.randint(1000,99999)
    
    return "A{}".format(num)

class Name(models.Model):

    def __str__(self):
        return self.id
        
    id = models.CharField(default=gen_pk, primary_key=True,max_length=255, unique=True,editable=False)
    name = models.CharField(max_length=40)