from django.db import models

# Create your models here.
class Account_info(models.Model):
    username = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.username}"