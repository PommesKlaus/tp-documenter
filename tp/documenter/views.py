from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.


class CompanyView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'documenter/companies.html', context={})


class CompanyDetailView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('SHOW SINGLE COMPANY DETAILS')


class DealingView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello World {0}'.format(kwargs['id']))