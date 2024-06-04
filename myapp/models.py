from django.db import models

# Create your models here.
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.CharField(max_length=20)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.CharField(max_length=20)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
