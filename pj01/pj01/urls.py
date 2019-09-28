"""pj01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from app01 import views,urls



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index.html/(\d+)/(\w+)', views.index),
    url(r'^index1.html/(?P<year>\d{4})/(?P<month>\d{2})', views.index1 ),
    url(r'^index2.html$', views.index2),
    url(r'^index3.html/(?P<year>\d+)', views.index3 ,{"name":"qweqwe","age":12}),

    url(r'^app01', include("app01.urls")),
]


