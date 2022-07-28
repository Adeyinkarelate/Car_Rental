from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField('User Name',max_length=200)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    
    
    
    def __Str__(self):
        return self.name