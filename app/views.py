from django.shortcuts import render
from app.models import *
# Create your views here.
def naresh(request):
    dt=dept.objects.all()
    dt=dept.objects.filter(dloc='new york')
    d={'keys':dt}
    return render(request,'ash.html',d)
def vamsi(request):
    ep=emp.objects.all()
    ep=emp.objects.filter(hiredate__day='20')
    ep=emp.objects.filter(deptno='20')
    ep=emp.objects.filter(ename__startswith='a')
    ep=emp.objects.filter(jod='salesman')
    ep=emp.objects.filter(sal__gte='1000')

    d={'keys1':ep}
    return render(request,'chitti.html',d)    