from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
# Create your models here.
class Add_recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    title = models.CharField(max_length=70)
    steps_to_cook = models.TextField()
    description = models.TextField()
    slug = AutoSlugField(populate_from='title', unique=True, null=True, default=None, unique_for_date=models.DateField())

    def __str__(self):
        return f"{self.user} {self.title}"

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    query_or_problem = models.TextField()

    def __str__(self):
        return f"{self.name} {self.subject}"
    

    
