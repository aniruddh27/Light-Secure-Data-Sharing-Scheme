
# Create your views here.
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from appAdmin.models import register,DUTATransaction,cloudTransaction,DODUTransaction,DUCTransaction,DUCDECTransaction
from appAdmin.forms import DUCTransactionForm
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def Home(request):
    username=request.session['username']
    request.session['username']=username

    context={}
    return render(request,"user/home.html",context)


def keyManagement(request):
    username=request.session['username']
    print(username)

    user_attributes_list=[]
    users=User.objects.filter(username=username)
    for user in users:
        user_attributes=register.objects.filter(user=user.id)
        for usr in user_attributes:
            user_attributes_list.append(usr.user.username)
            user_attributes_list.append(usr.user.email)
            user_attributes_list.append(usr.mobile)
        #     print(usr.user.username,usr.user.first_name,usr.user.last_name,usr.mobile)
            print("uattr-",user_attributes_list)
    status="No Key Requested"
    pub_Key=""
    duta_trans=DUTATransaction.objects.filter(user_name=username)
    if duta_trans is not None:
        for duta in duta_trans:
            status=duta.status
            pub_Key=duta.pub_key

    context={'user_attributes':user_attributes,'status':status,'pub_Key':pub_Key}
    # return render(request,"owner/managekey.html",context)
    if request.method=='POST':
        # dotaTransaction=DOTATransaction()
        status="Key Requested"
        user_name=username
        attributes=user_attributes_list
        status=status
        pub_Key=pub_Key
        duta=DUTATransaction(user_name=username,attributes=register.objects.get(user=user.id),status=status,pub_key=pub_Key)
        duta.save()
        duta_trans=DUTATransaction.objects.filter(user_name=user_name)
        for duta in duta_trans:
            status=duta.status
            pub_Key=duta.pub_key
            print('duta--',duta.status)
        print("attr-",attributes)
        print('sta-',status)
        context={'duta_trans':duta_trans,'user_attributes':user_attributes,'status':status,'pub_Key':pub_Key}
        return render(request,"user/managekey.html",context)
    else:
        status=status
        return render(request,"user/managekey.html",context)
    # return render(request,"user/managekey.html",context)

def Cryptography(request):
    username=request.session['username']
    if request.method=='POST':
        print('i m in post')
        ducdatas=DUCTransaction.objects.filter(user_name=username)
        for ducdata in ducdatas:
            file_name = ducdata.file_name
        print(file_name)
        context={}
        return render(request,"user/cryptography.html",context)
    else:
        print('i m in get')
        context={}
        return render(request,"user/cryptography.html",context)


def ownerNotification(request):
    username=request.session['username']
    print(username)
    form=DUCTransactionForm()
    doduDatas=DODUTransaction.objects.all()
    dutaDatas= DUTATransaction.objects.filter(user_name=username)

    if request.method=='POST':
        print('I m in post')
        doduDatas=DODUTransaction.objects.all()
        dutaDatas= DUTATransaction.objects.filter(user_name=username)
        attributeValue=request.POST.get('attributes')
        status="File Requested to Cloud"
        print('duta',dutaDatas)
        print('do--',doduDatas)
        for dodu in doduDatas:
            file_name = dodu.file_name
            owner_name=dodu.owner_name
        for dutaData in dutaDatas:
            user_name=dutaData.user_name
            pub_key=dutaData.pub_key
            print('user_name',dutaData.user_name)
        form=DUCTransactionForm(request.POST or None)
        if form.is_valid():
            duc=DUCTransaction(owner_name=owner_name,user_name=user_name,pub_key=pub_key,attributes=attributeValue,status=status,file_name=file_name)
            duc.save()
            print('Requested to Cloud')
            context={'username':username,'form':form}
            return render(request,'user/home.html',context)
        else:
            print('I m invalid')
            context={'username':username,'doduDatas':doduDatas,'dutaDatas':dutaDatas,'form':form}
            return render(request,'user/ownernotification.html',context)
    else:
        print('I m in get')
        context={'username':username,'doduDatas':doduDatas,'dutaDatas':dutaDatas,'form':form}
        return render(request,'user/ownernotification.html',context)

def ViewFiles(request):
    username=request.session['username']
    ducfiles=DUCTransaction.objects.filter(user_name=username)
    # ducfiles=DUCTransaction.objects.all()
    context={'ducfiles':ducfiles}
    return render(request,"user/viewFile.html",context)

    # ducdecData=DUCDECTransaction.objects.all()
    # for ducdec in ducdecData:
    #     status=ducdec.status
    #     dec_file=ducdec.dec_file
    #     # dec_file=ducdec.dec_file
    # # print(dec_file)
    # ducfiles = DUCTransaction.objects.all()
    # # context={'ducfiles':ducfiles,'status':status}
    # # username=request.session['username']
    # if request.method=='POST':
    #     ducdatas=DUCTransaction.objects.filter(user_name=username)
    #     for ducdata in ducdatas:
    #         file_name = ducdata.file_name
    #     print(file_name)
    #     context={'ducfiles':ducfiles}
    #     # context={'ducdecData':ducdecData}
    #     # return render(request,"user/viewFile.html",context)
    #     return HttpResponseRedirect(reverse('user:viewFiles'))
    # else:
    #     context={'ducfiles':ducfiles,'status':status}
    #     return render(request,"user/viewFile.html",context)
    #     # if dec_file is None:
    #     # else:
    #     #     context={'ducfiles':ducfiles,'status':status,'dec_file':dec_file}
    #     #     return render(request,"user/viewFile.html",context)


def sendFiletoDecryption(request,id):
    ducData = get_object_or_404(DUCTransaction,pk=id)
    owner_name=ducData.owner_name
    user_name=ducData.user_name
    pub_key=ducData.pub_key
    file_name=ducData.file_name
    enc_file=ducData.enc_file
    status="File Sent for Decryption"
    ducdec=DUCDECTransaction(owner_name=owner_name,user_name=user_name,pub_key=pub_key,file_name=file_name,enc_file=enc_file,status=status)
    ducdec.save()
    ducData=get_object_or_404(DUCTransaction,pk=id)
    ducData=DUCTransaction.objects.filter(pk=id).update(status=status)
    print("File sent for decryption")
    context={}
    # return render(request,"user/viewFile.html",context)
    return HttpResponseRedirect(reverse('user:viewFiles'))

def decryptedFile(request):
    username=request.session['username']
    # ducfiles=DUCTransaction.objects.filter(user_name=username)
    dudecs=DUCDECTransaction.objects.filter(user_name=username)
    print(dudecs)
    context={'dudecs':dudecs}
    return render(request,'user/decryptedFile.html',context)

# def viewDecryptedFile(request,id):
#     dudecs=get_object_or_404(DUCDECTransaction,pk=id)
#     print(dudecs.dec_file)
#     context={}
#     return HttpResponseRedirect(reverse('user:decryptedFile'))


def cloudFiles(request):
    ducFiles=cloudTransaction.objects.all()
    context={'ducFiles':ducFiles}
    return render(request,'user/cloudFiles.html',context)