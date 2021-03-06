"""tp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^company/$', CompanyView.as_view(), name='company-view'),
    url(r'^company/(?P<id>\d+)/$', CompanyDetailView.as_view(), name='company-detail-view'),
    url(r'^dealing/(?P<id>[a-z0-9-]{36})/$', DealingView.as_view(), name='dealing-view'),
]
