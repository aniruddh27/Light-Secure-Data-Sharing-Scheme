from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from appAdmin.models import DOTATransaction,cloudTransaction,DUTATransaction
import random
from cryptography.fernet import Fernet
# Create your views here.
def Home(request):
    context={}
    return render(request,"tpa/home.html",context)

def ownerKey(request):
    dotaData=DOTATransaction.objects.all()
    context={'dotaData':dotaData}
    return render(request,"tpa/ownerkey.html",context)
    # owner_id=User.objects
    # dotaData=DOTATransaction.objects.all()
    # for dota in dotaData:
    #     print("id----",dota.attributes.user.username)
    #     for dota in dotaData:
    #         # generatePubKey(dota.id)
    #         status=dota.status
    #         keys=dota.pub_key
    # context={'dotaData':dotaData,'status':status,'keys':keys}
    # if request.method=='POST':
    #     if '_generateKeyBtn' in request.POST:
    #         print(request.POST.get('id'))
    #         # keys=generateOwnerPubKey(dota.id)
    #         # keys=generatePubKey()
    #         # status="Key Generated"
    #         # dotaUpdate=DOTATransaction.objects.filter(id=dota.id).update(pub_key=keys,status=status)
    #         # print("generated")
    #         # dotaData=DOTATransaction.objects.all()
    #         # for dota in dotaData:
    #         #     keys=generateOwnerPubKey(dota.id)
    #         #     # keys=generatePubKey()
    #         #     status="Key Generated"
    #         #     dotaUpdate=DOTATransaction.objects.filter(id=dota.id).update(pub_key=keys,status=status)
    #         #     print("generated")
    #         #     dotaData=DOTATransaction.objects.all()
    #         context={'dotaData':dotaData,'status':status,'keys':keys}
    #         return render(request,"tpa/ownerkey.html",context)
    #     elif '_sendKeyBtn' in request.POST:
            
    #         for dota in dotaData:
    #             status="Key Sent"
    #             dotaUpdate=DOTATransaction.objects.filter(id=dota.id).update(status=status)
    #             print("Updated")
    #             dotaData=DOTATransaction.objects.all()
    #         context={'dotaData':dotaData,'status':status,'keys':keys}
    #         return render(request,"tpa/ownerkey.html",context)
    #     return render(request,"tpa/ownerkey.html",context)

    # else:
    #     print("I am else here")
    #     # context={'dotaData':dotaData,'status':status,'key':key}
    #     return render(request,"tpa/ownerkey.html",context)

def userKey(request):
    dutaData=DUTATransaction.objects.all()
    context={'dutaData':dutaData}
    return render(request,"tpa/userkey.html",context)

    # dutaData=DUTATransaction.objects.all()
    # for duta in dutaData:
    #     print("id----",duta.attributes.user.username)
    #     for duta in dutaData:
    #         # generatePubKey(duta.id)
    #         status=duta.status
    #         keys=duta.pub_key
    # context={'dutaData':dutaData,'status':status,'keys':keys}
    # if request.method=='POST':
    #     if '_generateKeyBtn' in request.POST:
    #         keys=generatePubKey()
    #         status="Key Generated"
    #         dutaUpdate=DUTATransaction.objects.filter(id=duta.id).update(pub_key=keys,status=status)
    #         print("generated")
    #         dutaData=DUTATransaction.objects.all()
    #         for duta in dutaData:
    #             keys=generateUserPubKey(duta.id)
    #             # keys=generatePubKey()
    #             status="Key Generated"
    #             dutaUpdate=DUTATransaction.objects.filter(id=duta.id).update(pub_key=keys,status=status)
    #             print("generated")
    #             dutaData=DUTATransaction.objects.all()
    #         context={'dutaData':dutaData,'status':status,'keys':keys}
    #         return render(request,"tpa/userkey.html",context)
    #     elif '_sendKeyBtn' in request.POST:
            
    #         for duta in dutaData:
    #             status="Key Sent"
    #             dutaUpdate=DUTATransaction.objects.filter(id=duta.id).update(status=status)
    #             print("Updated")
    #             dutaData=DUTATransaction.objects.all()
    #         context={'dutaData':dutaData,'status':status,'keys':keys}
    #         return render(request,"tpa/userkey.html",context)
    #     return render(request,"tpa/userkey.html",context)

    # else:
    #     print("I am else here")
    #     # context={'dutaData':dutaData,'status':status,'key':key}
    #     return render(request,"tpa/userkey.html",context)



# Generate public key for owner
# def generateOwnerPubKey(owner_id):
#     dotaData=DOTATransaction.objects.get(id=owner_id)
#     attributes=dotaData.attributes.user.username+dotaData.attributes.user.email+dotaData.attributes.mobile
#     key=''.join(random.sample(attributes,len(attributes)))
#     key=key[0:32]
#     print("g",attributes)
#     print("g",key)
#     return key
    
# Generate public key for user
# def generateUserPubKey(user_id):
#     dutaData=DUTATransaction.objects.get(id=user_id)
#     attributes=dutaData.attributes.user.username+dutaData.attributes.user.email+dutaData.attributes.mobile
#     key=''.join(random.sample(attributes,len(attributes)))
#     key=key[0:32]
#     print("g",attributes)
#     print("g",key)
#     return key


#Generate public key
def generatePubKey(request,id):
    if request.method=='POST':
        print(id)
        dota=get_object_or_404(DOTATransaction,pk=id)
        status="Key Generated"
        key = Fernet.generate_key()
        print(key)
        dotaData=DOTATransaction.objects.filter(pk=id).update(pub_key=key,status=status)
        context={}
        return HttpResponseRedirect(reverse("tpa:ownerkey"))
    else:
        context={}
        return render(request,"tpa/ownerkey.html",context)

#send public key
def sendPubKey(request,id):
    if request.method=='POST':
        print(id)
        dota=get_object_or_404(DOTATransaction,pk=id)
        status="Key Sent"
        dotaData=DOTATransaction.objects.filter(pk=id).update(status=status)
        context={}
        return HttpResponseRedirect(reverse("tpa:ownerkey"))
    else:
        context={}
        return render(request,"tpa/ownerkey.html",context)


#Generate User public key
def generateUserPubKey(request,id):
    if request.method=='POST':
        print(id)
        dota=get_object_or_404(DUTATransaction,pk=id)
        status="Key Generated"
        key = Fernet.generate_key()
        print(key)
        dotaData=DUTATransaction.objects.filter(pk=id).update(pub_key=key,status=status)
        context={}
        return HttpResponseRedirect(reverse("tpa:userkey"))
    else:
        context={}
        return render(request,"tpa/userkey.html",context)

#send User public key
def sendUserPubKey(request,id):
    if request.method=='POST':
        print(id)
        dota=get_object_or_404(DUTATransaction,pk=id)
        status="Key Sent to User"
        dotaData=DUTATransaction.objects.filter(pk=id).update(status=status)
        context={}
        return HttpResponseRedirect(reverse("tpa:userkey"))
    else:
        context={}
        return render(request,"tpa/userkey.html",context)

def ownerUploadedFiles(request):
    ctData=cloudTransaction.objects.all()
    context={'ctData':ctData}
    return render(request,'tpa/ownerUploadedFiles.html',context)