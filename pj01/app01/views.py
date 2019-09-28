from django.shortcuts import render,HttpResponse
from django.http import HttpRequest
from django.template import *
from app01 import models
# Create your views here.
def index1(request,month,year):
    print(request.GET)
    print("year",year)
    print("month",month)
    return HttpResponse("year:{} month:{}".format(year,month))

def index3(request,year,age,name):
    print(request.GET)
    print("year",year)
    print("name",name)
    print("age",age)

    return HttpResponse(year)


def index2(request):
    print(request.GET)
    aa = request.GET.get("aa")
    print(aa)
    # return HttpResponse(aa)
    return render(request,"index.html",locals())

def index(request,a,b):
    print(request.GET)
    print(a)
    print(b)
    return HttpResponse(a+"  "+b)


def index4(request):
    # print(request)
    value6 = '<a href="#">跳转</a>'
    value8 = 'http://www.baidu.com/?a=1&b=3'

    value1 = 123
    persion = models.Person.objects.get(pk='1')
    print('one =',persion)
    return render(request,"index.html",locals())


def register(request):
    print("post ",request.POST)
    print("get ",request.GET)

    return HttpResponse("ok111")