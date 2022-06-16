from django.db import models
from django.contrib.auth.models import User

# Create your models here.


    
class College(models.Model):
    name = models.CharField(max_length=200)
   
    
    def __str__(self):
        return self.name
 


class Repository(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, default="")
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True)
    docfile = models.FileField(upload_to= 
    'document/%d/%m/%Y', default='DEFAULT VALUE',null = True, )
    description = models.TextField(null=True, blank=True)
    authors = models.ManyToManyField(User, related_name='authors',blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated','-created']
    
    def __str__(self):
        return self.title
    



    
    
    
    
