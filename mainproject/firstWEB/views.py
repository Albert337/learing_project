from django.shortcuts import render
from firstWEB.models import *
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def CalPage(request):
    return render(request,'cal.html')

def Cal(request):  ###实际上进行计算
    if request.POST:
        value_a,value_b=request.POST["valueA"],request.POST["valueB"]
        result=int(value_a)+int(value_b)
        # print(value_a,value_b)

        ###开始写入sql-lite数据库
        cal.objects.create(value_a=value_a,value_b=value_b,result=result)
        return render(request,'result.html',context={"data":result})
    else:
        return HttpResponse("please visit us with POST")

def CalList(request):
    datas=cal.objects.all()
    # for data in datas:
    #     print(data.value_a,data.value_b,data.result)
    return render(request,'list.html',context={"datas":datas})

def DelData(request):
    cal.objects.all().delete()
    return HttpResponse('data deleted')