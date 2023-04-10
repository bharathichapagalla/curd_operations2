from django.db import models

# Create your models here.
class dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100,unique=True,null=False)
    dloc=models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return str(self.deptno)


class emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100,unique=True)
    jod=models.CharField(max_length=100)
    mgr=models.IntegerField()
    hiredate=models.DateField()
    sal=models.IntegerField(null=True)
    comm=models.IntegerField(null=False)
    deptno=models.ForeignKey(dept,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.empno)

