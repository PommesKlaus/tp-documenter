from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.db.models import Q
from django.db.models import Count, Case, When

from .models import Company, Dealing, DealingCategory

# Create your views here.


class CompanyView(View):

    def get(self, request, *args, **kwargs):
        c = Company.objects.all()
        return render(request, 'documenter/companies.html', context={'companies': c})


class CompanyDetailView(View):

    def get(self, request, *args, **kwargs):
        company = Company.objects.get(pk=self.kwargs['id'])
        categories = DealingCategory.objects.annotate(
            num_dealings=Count(Case(
                When(Q(dealing__beneficiary=company) | Q(dealing__supplier=company), then=1),
            ))
        )
        # categories = DealingCategory.objects.annotate(num_dealings=Count('dealing'))
        dealing_list = Dealing.objects.filter(Q(beneficiary=company) | Q(supplier=company))






        return render(request, 'documenter/company_detail.html', context={
            'company': company,
            'categories': categories,
            'dealing_list': dealing_list
        })


class DealingView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello World {0}'.format(kwargs['id']))