from django.shortcuts import render,get_object_or_404
from appAdmin.models import cloudTransaction,DUCTransaction,DODUTransaction
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def Home(request):
    pageTitle = 'Cloud'
    context={'pageTitle':pageTitle}
    return render(request,'cloud/Home.html',context)

def uploadedFiles(request):
    ctData=cloudTransaction.objects.all()
    context={'ctData':ctData}
    return render(request,'cloud/uploadedFiles.html',context)

def userRequest(request):
    ducData=DUCTransaction.objects.all()
    print(ducData)
    for ducD in ducData:
        status=ducD.status
    context={'ducData':ducData,'status':status}
    return render(request,'cloud/userRequest.html',context)

    # for ducd in ducData:
    #     owner_name=ducd.owner_name
    #     user_name=ducd.user_name
    #     ducAttributes=ducd.attributes
    #     file_name=ducd.file_name

    # if request.method=='POST' or None:
    #     print('I am in post')
    #     if 'verifyBtn' in request.POST:
    #         print('I am inside post')
    #         cloudData=cloudTransaction.objects.filter(owner_name=owner_name,file_name=file_name)
    #         for duc in cloudData:
    #             attributes=duc.attributes
    #             policy=duc.policies
    #             enc_file=duc.enc_file
    #             print(attributes)
    #             print(policy)
    #         if ducAttributes == attributes:
    #             print('True')
    #         if policy in ducAttributes:
    #             status="Verified"
    #             ducStatus=DUCTransaction.objects.filter(owner_name=owner_name,file_name=file_name,user_name=user_name).update(status=status,enc_file=enc_file)
    #             print('updated')
    #         else:
    #             status="Not Verified"
    #             ducStatus=DUCTransaction.objects.filter(owner_name=owner_name,file_name=file_name,user_name=user_name).update(status=status,enc_file=enc_file)
    #             print('updated')


    #         context={'ducData':ducData}
    #         return render(request,'userRequest.html',context)

    #     if 'sendFileBtn' in request.POST:
    #         status="File Sent"
    #         ducStatus=DUCTransaction.objects.filter(owner_name=owner_name,file_name=file_name,user_name=user_name).update(status=status)
    #         print('File Sent')
    #         context={'ducData':ducData}
    #         return render(request,'userRequest.html',context)

    # else:
    #     print('I am in get')
    #     context={'ducData':ducData}
    #     return render(request,'userRequest.html',context)

def verifyAttributes(request,id):
    ducData=get_object_or_404(DUCTransaction,pk=id)
    owner_name=ducData.owner_name
    user_name=ducData.user_name
    ducAttributes=ducData.attributes
    print('da--',ducAttributes)
    file_name=ducData.file_name
    if request.method=='POST':
        cloudData=cloudTransaction.objects.filter(owner_name=owner_name,file_name=file_name)
        for duc in cloudData:
            attributes=duc.attributes
            policy=duc.policies
            enc_file=duc.enc_file
            print(attributes)
            print(policy)
            if policy in ducAttributes:
                status="Verified"
                ducStatus=DUCTransaction.objects.filter(pk=id).update(status=status,enc_file=enc_file)
                # print(' verified updated')
                # context={'attributes':attributes,'ducAttributes':ducAttributes,'policy':policy,'status':status}
                # return render(request,'cloud/userRequest.html',context)
                return HttpResponseRedirect(reverse('cloud:userRequest'))
            else:
                status="Not Verified"
                ducStatus=DUCTransaction.objects.filter(pk=id).update(status=status)
                print('not verified updated')
                context={'status':status}
                return render(request,'cloud/userRequest.html',context)
                # return HttpResponseRedirect(reverse('cloud:userRequest'))
    else:
        # ducData=get_object_or_404(DUCTransaction,pk=id)
        # ducAttributes=ducData.attributes
        # print('da--',ducAttributes)
        context={}
        return HttpResponseRedirect(reverse('cloud:userRequest'))


def sendUserFile(request,id):
    duc=get_object_or_404(DUCTransaction,pk=id)
    file_name=duc.file_name
    cdCounts=cloudTransaction.objects.filter(file_name=file_name)
    for cdCount in cdCounts:
        # print(cdCount)
        count=cdCount.downloadCount
        print('cc-',count)
    downloadCount=count+1
    print('dc--',downloadCount)
    status="File Sent to User"

    ducStatus=DUCTransaction.objects.filter(pk=id).update(status=status)
    cStatus=cloudTransaction.objects.filter(file_name=file_name).update(downloadCount=downloadCount)
    print('csta--',cStatus)
    print('File Sent')
    context={}
    return HttpResponseRedirect(reverse('cloud:userRequest'))
    # return render(request,'cloud/userRequest.html',context)