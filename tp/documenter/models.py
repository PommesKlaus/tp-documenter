import uuid

from django.db import models

from .settings.countries import ISO31661a2

# Create your models here.

class Company(models.Model):
    shortname = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=2, choices=ISO31661a2)


class Category(models.Model):
    name = models.CharField(max_length=120)
    template_json = models.TextField(default='{}')


class Dealing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=255)
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    beneficiary = models.ManyToManyField(Company, related_name='dealing_as_beneficiary')
    supplier = models.ManyToManyField(Company, related_name='dealing_as_supplier')
    template_json = models.TextField(default='{}')
    data_json = models.TextField(default='{}')
    createdAt = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True)
    closed = models.BooleanField(default=False)
    external_visible = models.BooleanField(default=False)
