from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    technology = models.CharField(max_length=50)
    image = models.ImageField(upload_to = "ProjectImages/",null=True)
    
    def __str__(self):
        return self.title
