from django.db import models

# Create your models here.

class Victim(models.Model):
    victim_name = models.CharField(max_length=100)
    victim_email = models.CharField(max_length=100)
    victim_address = models.CharField(max_length=100)
    contact_subject = models.CharField(max_length=100)
    victim_message = models.TextField()


    def __str__(self):
        return self.victim_name

class Client(models.Model):
     first_name = models.CharField(max_length=100)
     last_name = models.CharField(max_length=100)
     email_address = models.CharField(max_length=100)
     telephone_number = models.CharField(max_length=15)

     def __str__(self):
         return self.first_name
