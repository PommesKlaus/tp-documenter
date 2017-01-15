import uuid
import datetime

from django.db import models

from .settings.countries import ISO31661a2

# Create your models here.

class CompanyCategory(models.Model):
    name = models.CharField(max_length=120)
    template_json = models.TextField()

    def __str__(self):
        return self.name


class Company(models.Model):
    shortname = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(CompanyCategory)
    country = models.CharField(max_length=2, choices=ISO31661a2)
    data_json = models.TextField(default='{}')
    begin = models.DateField(default=datetime.date.today())
    end = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class DealingCategory(models.Model):
    name = models.CharField(max_length=120)
    template_json = models.TextField(default='{}')

    def __str__(self):
        return self.name


class Dealing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(DealingCategory)
    title = models.CharField(max_length=255)
    begin = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    beneficiary = models.ManyToManyField(Company, related_name='dealing_as_beneficiary')
    supplier = models.ManyToManyField(Company, related_name='dealing_as_supplier')
    template_json = models.TextField(default='{}')
    data_json = models.TextField(default='{}')
    createdAt = models.DateTimeField(auto_now_add=True)
    lastModified = models.DateTimeField(auto_now=True)
    closed = models.BooleanField(default=False)
    external_visible = models.BooleanField(default=False)

    def __str__(self):
        return self.title
