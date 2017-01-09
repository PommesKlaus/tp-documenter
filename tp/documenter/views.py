from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .models import Company

# Create your views here.


class CompanyView(View):

    def get(self, request, *args, **kwargs):
        c = Company.objects.all()
        return render(request, 'documenter/companies.html', context={'companies': c})


class CompanyDetailView(View):

    def get(self, request, *args, **kwargs):
        c = Company.objects.get(pk=self.kwargs['id'])
        return render(request, 'documenter/company_detail.html', context={'company': c})


class DealingView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello World {0}'.format(kwargs['id']))