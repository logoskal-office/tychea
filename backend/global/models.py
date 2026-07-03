from django.db import models

class ClientInfo(models.Model):
    name = models.CharField(max_length=200)
    name_solo = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    phone_number_2 = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField()
    email_2 = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=200)
    building = models.CharField(max_length=200, null=True, blank=True)
    logo = models.ImageField(upload_to='clients/logos/', null=True, blank=True)

    def __str__(self):
        return self.name
