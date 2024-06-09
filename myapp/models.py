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
    accept = models.BooleanField(default=False) 
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class MultipleOfThreeField(models.IntegerField):
    def pre_save(self, model_instance, add):
        if add:
            max_value = Schedule.objects.all().aggregate(models.Max('schedule_id'))['schedule_id__max']
            if max_value is None:
                max_value = 0
            return max_value + 1
        else:
            return getattr(model_instance, self.attname)

class Schedule(models.Model):
    # schedule_id = models.AutoField(primary_key=True)
    schedule_id = MultipleOfThreeField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.CharField(max_length=20)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
