from django.shortcuts import render
from . import models
from port.models import Code
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


def index(request):
    return render(request,'port/index.html')

def porttest(request):
    return render(request,'port/porttest.html')

def code(request):
    codes = models.Code.objects.all()
    paginator = Paginator(codes,10)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request,'port/code.html',{'codes':contacts})

def editcode(request,code_id):
    if str(code_id) == '0':
        return render(request,'port/editcode.html')
    code = models.Code.objects.get(pk=code_id)
    return render(request,'port/editcode.html',{'code':code})

def codedetail(request,code_id):
    code = models.Code.objects.get(pk=code_id)
    return render(request,'port/codedetail.html',{'code':code})

def search_name(request):
    search_name = request.GET.get('name','')
    codes = Code.objects.filter(name__contains=search_name)
    paginator = Paginator(codes, 10)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'port/code.html', {'codes': contacts})
# Create your views here.
