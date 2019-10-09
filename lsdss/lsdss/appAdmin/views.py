from django.shortcuts import render
from appAdmin.forms import registerForm
from appAdmin.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def registerData(request):
    form=registerForm()
    context={'form':form}
    return render(request,"index.html",context)

def adminApp(request):
    context={}
    return render(request,'admin/adminHome.html',context)

def usersList(request):
    users=register.objects.all().filter(module="User")
    context={'users':users}
    return render(request,'admin/viewUsers.html',context)

def ownersList(request):
    owners=register.objects.all().filter(module="Owner")
    context={'owners':owners}
    return render(request,'admin/viewOwners.html',context)

def deleteAllData(request):
    DOTATransaction.objects.all().delete()
    ownerFileUpload.objects.all().delete()
    DOESPTransaction.objects.all().delete()
    cloudTransaction.objects.all().delete()
    DODUTransaction.objects.all().delete()
    DUTATransaction.objects.all().delete()
    DUCTransaction.objects.all().delete()
    DUCDECTransaction.objects.all().delete()
    deleted="deleted"
    context={'deleted':deleted}
    return HttpResponseRedirect(reverse("adminApp:adminHome"))
