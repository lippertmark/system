from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Goods(models.Model):
    name = models.CharField(max_length=255, default=None)
    info = models.TextField(default=None)
    cost = models.IntegerField(default=0)
    count_in_stock = models.IntegerField(default=100000000)
    count_sold = models.IntegerField(default=0)
    image = models.ImageField(upload_to='way_to_budy/images/goods', default=None, null=None)
    file = models.FileField(upload_to='way_to_budy/files', default=None, null=None)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    age = models.IntegerField(default=None)
    email = models.EmailField(default=None)

    '''date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)'''

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class Form(models.Model):
    ind = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    info = models.TextField()


class Question(models.Model):
    ind = models.ForeignKey(Form, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, choices=[('choose', 'choose'), ('answer', 'answer')])
    question = models.CharField(max_length=255)
    text = models.TextField(default='')

    def __str__(self):
        return self.question

# Create your models here.
