from django.shortcuts import render
from . import models
from port.models import Code
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


def index(request):###首页
    return render(request,'port/index.html')



def code(request):###展示代码列表
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

def editcode(request,code_id):####跳转到修改或编辑新代码页面
    if str(code_id) == '0':
        return render(request,'port/editcode.html')
    code = models.Code.objects.get(pk=code_id)
    return render(request,'port/editcode.html',{'code':code})

def codedetail(request,code_id):###显示具体的代码详情
    code = models.Code.objects.get(pk=code_id)
    return render(request,'port/codedetail.html',{'code':code})

def editaction(request):###修改和编辑新的代码
    name = request.POST.get('name','NAME')
    discribe = request.POST.get('discribe','DISCRIBE')
    content = request.POST.get('content','CONTENT')
    code_id = request.POST.get('code_id','0')
    if code_id == '0':
        models.Code.objects.create(name=name,discribe=discribe,content=content)
        codes = models.Code.objects.all()
        paginator = Paginator(codes, 10)
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        return render(request, 'port/code.html', {'codes': contacts})
    code = models.Code.objects.get(pk=code_id)
    code.name = name
    code.discribe = discribe
    code.content = content
    code.save()
    codes = models.Code.objects.all()
    paginator = Paginator(codes, 10)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'port/code.html', {'codes': contacts})


def search_name(request):####按名称搜索代码
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

def codedelete(request,code_id):###删除脚步
    code = models.Code.objects.get(pk=code_id)
    code.delete()
    codes = Code.objects.all()
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
