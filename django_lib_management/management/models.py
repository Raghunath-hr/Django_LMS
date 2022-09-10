from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
# Create your models here.
class CustomUser(AbstractUser):
	email = models.CharField(_('email address'), max_length=200, unique=True)

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    class Meta:
        swappable = 'AUTH_USER_MODEL'

class Book(models.Model):
    catchoice= [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biography'),
        ('history', 'History'),
        ('novel', 'Novel'),
        ('fantasy', 'Fantasy'),
        ('thriller', 'Thriller'),
        ('romance', 'Romance'),
        ('scifi','Sci-Fi')
        ]
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    category=models.CharField(max_length=100,choices=catchoice,default='entertainment')
    def __str__(self):
        return str(self.name)