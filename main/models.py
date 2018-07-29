from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Evenet(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    first_name = models.CharField(max_length=120, null=False, blank=False)
    email = models.EmailField(null=False, unique=True, blank=False)
    event = models.ForeignKey(Evenet, null=True, blank=True)
    password = models.CharField(max_length=20, null=True, blank=True)
    more_detail = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.email


class Notification(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    event_date = models.DateField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


PAYMENT_MODE = (
        ('OL', 'Online'),
        ('OF', 'Ofline'),
)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fee = models.DecimalField(decimal_places=2, max_digits=6)
    payment_mode = models.CharField(max_length=2,choices=PAYMENT_MODE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email




