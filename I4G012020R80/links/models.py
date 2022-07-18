from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from .managers import ActiveLinkManager

# Create your models here.
class Link(models.Model):
    target_url = models.URLField( max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length= 20, unique=True, blank= True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Date_created = models.DateTimeField( auto_now=True)
    objects = models.Manager()

    public = ActiveLinkManager()
    active = models.BooleanField()
    