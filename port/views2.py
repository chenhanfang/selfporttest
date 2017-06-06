from django.shortcuts import render
from . import models
from port.models import Code
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def porttest(request):###接口测试页
    return render(request,'port/porttest.html')