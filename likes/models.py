from django.db import models
from django.contrib.auth.models import User

class Campaign(models.Model):
    user = models.ForeignKey(User)

    link = models.CharField(max_length=255L, null=False, db_index=True) 
    title = models.CharField(max_length=1000L)
    category = models.CharField(max_length=255L, null=False, db_index=True)
    image = models.ImageField("Ad Image", upload_to="images/ads", blank=True, null=True)
    description = models.CharField(max_length=1000L)
    keywords = models.CharField(max_length=255L, null=False, db_index=True)
    bid = models.DecimalField(max_digits=6, decimal_places=2)
    budget = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True, blank=True)


class Post(models.Model):
    user = models.ForeignKey(User)

    url = models.CharField(max_length=255L, null=False, db_index=True)
    title = models.CharField(max_length=1000L)
    image = models.TextField(max_length=1000L, null=True, default=None)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True, blank=True)
