from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True) 
    phone = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='contacts_photos/', blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name

