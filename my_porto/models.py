from django.db import models

# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=500)
    profile = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    phone = models.CharField(max_length=500)
    description = models.TextField()

class service(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)

class work(models.Model):
    title=models.CharField(max_length=500)
    image=models.ImageField(upload_to='image/')
    type = models.CharField(max_length=500)
    date = models.DateField()

class contact(models.Model):
    name= models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    subject = models.CharField(max_length=500)
    message = models.TextField(max_length=500)

    def __str__(self):
                return self.name