from django.shortcuts import render,get_object_or_404,render_to_response,redirect
from appAdmin.models import register,DOTATransaction,ownerFileUpload,DOESPTransaction,cloudTransaction,DODUTransaction
from django.contrib.auth.models import User
from appAdmin.forms import ownerFileUploadForm,cloudFileUploadForm
from django.http import HttpResponseRedirect ,HttpResponse
from django.urls import reverse
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
# from .models import ModelWithFileField
# Create your views here.
def Home(request):
    username=request.session['username']
    request.session['username']=username

    context={}
    return render(request,"owner/home.html",context)

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
    dota_trans=DOTATransaction.objects.filter(owner_name=username)
    if dota_trans is not None:
        for dota in dota_trans:
            status=dota.status
            pub_Key=dota.pub_key

    context={'user_attributes':user_attributes,'status':status,'pub_Key':pub_Key}
    # return render(request,"owner/managekey.html",context)
    if request.method=='POST':
        # dotaTransaction=DOTATransaction()
        status="Key Requested"
        owner_name=username
        attributes=user_attributes_list
        status=status
        pub_Key=pub_Key
        dota=DOTATransaction(owner_name=username,attributes=register.objects.get(user=user.id),status=status,pub_key=pub_Key)
        dota.save()
        dota_trans=DOTATransaction.objects.filter(owner_name=owner_name)
        for dota in dota_trans:
            status=dota.status
            pub_Key=dota.pub_key
            print('dota--',dota.status)
        print("attr-",attributes)
        print('sta-',status)
        context={'dota_trans':dota_trans,'user_attributes':user_attributes,'status':status,'pub_Key':pub_Key}
        return render(request,"owner/managekey.html",context)
    else:
        status=status
        return render(request,"owner/managekey.html",context)


def cryptography(request):
    userFile=""
    status=""
    username=request.session['username']
    ufiles=ownerFileUpload.objects.filter(owner_name=username)
    for ufile in ufiles:
        userFile=ufile.owner_file.url
        status=ufile.file_status
    print(status)
    doespData=DOESPTransaction.objects.filter(owner_name=username)
    context={'doespData':doespData,'userFile':userFile,'status':status}
    return render(request,"owner/cryptography.html",context)

def uploadFile(request):
    username=request.session['username']
    print(username)
    uploaded=False
    form=ownerFileUploadForm()
    doespData=DOESPTransaction.objects.filter(owner_name=username)
    for doesp in doespData:
        status=doesp.status
        print(status)
    context={'form':form }
    if request.method=='POST':
        if 'uploadFileBtn' in request.POST:
            print('I m upload...')
            form=ownerFileUploadForm(request.POST or None,request.FILES)
            if form.is_valid():
                owner_name=username
                ofname=request.POST.get('file_name')
                ofile=request.FILES.get('owner_file')
                fs = FileSystemStorage()
                filename = fs.save(ofile.name, ofile)
                uploaded_file_url = fs.url(filename)
                ofileName=ofile.name
                print(ofileName)
                file_status=""
                fuForm=ownerFileUpload(owner_name=username,file_name=ofname,owner_file=ofileName,file_status=file_status)
                fuForm.save()
                print('uploaded')
                uploaded=True
                files=ownerFileUpload.objects.all().filter(owner_name=username)
                context={'form':form,'uploaded':uploaded,'files':files,'uploaded_file_url':uploaded_file_url}
                # return render(request,"owner/uploadFile.html",context)
                return HttpResponseRedirect(reverse('owner:uploadFile'))
            else:
                print("Form invalid")
                print(form.errors)
                context={'form':form}
                return render(request,"owner/uploadFile.html",context)
        else:
            print('I m upload...get')
            context={'uploaded_file_url':uploaded_file_url}
            return render(request,"owner/uploadFile.html",context)


    else:
        files=ownerFileUpload.objects.all().filter(owner_name=username)
        context={'form':form,'files':files}
        return render(request,"owner/uploadFile.html",context)

def uploadedFileDelete(request,id):
    username=request.session['username']
    selected_file=get_object_or_404(ownerFileUpload,pk=id)
    selected_file.delete()
    print('deleted')
    files=ownerFileUpload.objects.all().filter(owner_name=username)
    context={'files':files}
    return render(request,"owner/uploadFile.html",context)

# Uploaded to cloud
def uploadedFile(request):
    username=request.session['username']
    status="File Uploaded"
    cloudData=cloudTransaction.objects.filter(owner_name=username,status = status)
    print(cloudData)
    uType="User"
    userList=[]
    curStatus=''
    # context={'doespData':doespData}
    users=register.objects.filter(module=uType)
    owner_name=username
    usersList=''
    if request.method=="POST":

        cloudData=cloudTransaction.objects.filter(owner_name=owner_name,status = status)
        for cdata in cloudData:
            file_name=cdata.file_name
            attributes=cdata.attributes
        userListMembers=request.POST.getlist('userCheckbox')
        userList.append(userListMembers)
        userListData=",".join(str(user) for user in userList)
        status="Data Shared"
        print(userListData)
        dodudata=DODUTransaction(owner_name=owner_name,file_name=file_name,attributes=attributes,user_list=userListData,status=status)
        dodudata.save()
        context={'users':users,'cloudData':cloudData}
        return render(request,"owner/uploadedFile.html",context)
    else:
        status="Data Shared"
        dodudatas=DODUTransaction.objects.filter(owner_name=owner_name,status = status)
        for dodudata in dodudatas:
            curStatus=dodudata.status
            usersList=dodudata.user_list
            print(curStatus)
            # users=str(usersList).split(',')
            print(usersList)
            # for u in users:
            #     print(u)
        context={'users':users,'cloudData':cloudData,'curStatus':curStatus,'usersList':usersList}
        return render(request,"owner/uploadedFile.html",context)


def sendFiletoEncryption(request,id):
    username=request.session['username']
    dotaData=DOTATransaction.objects.filter(owner_name=username)
    for dota in dotaData:
        pub_key=dota.pub_key
    selected_file=get_object_or_404(ownerFileUpload,pk=id)
    owner_name=username
    file_name=selected_file.file_name
    file_path=selected_file.owner_file.url
    status="File to Encrypt"
    form=DOESPTransaction()
    context={'form':form}
    enc_file=""
    if request.method=="POST":
        status="File sent for Encryption"
        form=DOESPTransaction(owner_name=owner_name,file_name=file_name,file_path=file_path,pub_key=pub_key,status=status,enc_file=enc_file)
        form.save()
        print('form sent')
        file_status=status
        doespUpdate=ownerFileUpload.objects.filter(id=id).update(file_status=status)
        print("status updated")
        context={'form':form,'status':status,'file_status':file_status}
        # return render(request,"owner/cryptography.html",context)
        return HttpResponseRedirect(reverse('owner:uploadFile'))
    else:
        # form=DOESPTransaction()
        print('invalid form')
        # print(form.errors)
        files=ownerFileUpload.objects.all().filter(owner_name=username)
        context={'files':files,'form':form,'status':status}
        return render(request,"owner/uploadFile.html",context)

def uploadFiletoCloud(request,id):
    # attributes=[]
    # policies=[]
    form=cloudFileUploadForm()
    doespData=get_object_or_404(DOESPTransaction,pk=id)
    context={'doespData':doespData,'form':form}
    if request.method=="POST":
        form=cloudFileUploadForm(request.POST or None)
        print(request.POST.get('attributes'))
        print(request.POST.get('policies'))
        if form.is_valid():
            attributes=request.POST.get('attributes')
            policies=request.POST.get('policies')
            owner_name=doespData.owner_name
            file_name=doespData.file_name
            enc_file=doespData.enc_file
            pub_key=doespData.pub_key
            downloadCount=0
            status="File Uploaded"
            attributes=attributes
            policies=policies
            print('attr',attributes)
            print('policy',policies)
            form=cloudTransaction(owner_name=owner_name,file_name=file_name,enc_file=enc_file,pub_key=pub_key,status=status,attributes=attributes,policies=policies,downloadCount=downloadCount)

            form.save()
            doespUpdate=DOESPTransaction.objects.filter(id=id).update(status=status)
            print('form sent')
            context={'form':form}
            return HttpResponseRedirect(reverse("owner:cryptography"))
            # return render(request,"owner/uploadCloud.html",context)
        else:
            print("Invalid Form")
            print(form.errors)
            context={'form':form}
            return render(request,"owner/uploadCloud.html",context)
    else:
        doespData=get_object_or_404(DOESPTransaction,pk=id)

        context={'doespData':doespData,'form':form}
        return render(request,"owner/uploadCloud.html",context)
        # return HttpResponseRedirect(reverse("owner:uploadFiletoCloud"))

def showUserList(request):
    uType="User"
    users=register.objects.filter(module=uType)
    if request.method=="POST":
        userList=request.POST.getlist('userCheckbox')
        print(userList)
        context={'users':users}
        return render(request,"owner/userList.html",context)
    else:
        context={'users':users}
        return render(request,"owner/userList.html",context)


# Revocation of file
def revocationNotification(request):
    username=request.session['username']
    ctDatas=cloudTransaction.objects.filter(owner_name=username)
    for ctData in ctDatas:
        context={'ctDatas':ctDatas,'count':ctData.downloadCount}
        return render(request,'owner/revocationNotification.html',context)
        # if ctData.downloadCount >= 3:
        # else:
        #     context={'ctDatas':ctDatas,'count':ctData.downloadCount}
        #     return render(request,'owner/revocationNotification.html',context)


def revocation(request,id):
    if request.method=='POST':
        print('i m in revoke post')
        ct=get_object_or_404(cloudTransaction,pk=id)
        file_name=ct.file_name
        pub_key=ct.pub_key
        policies=request.POST.get('policies')
        print(policies)
        status='File Sent for Re-Encryption'
        ctStatus=cloudTransaction.objects.filter(pk=id).update(policies=policies,status=status)
        doesp=DOESPTransaction.objects.filter(file_name=file_name,pub_key=pub_key).update(status=status)
        print('cts--',ctStatus)
        print('doesp--',doesp)
        context={}
        return redirect('owner:revocationNotification')
        # return render(request,'owner/revocationNotification.html',context)
    else:
        ctData=get_object_or_404(cloudTransaction,pk=id)
        context={'ctData':ctData}
        return render(request,'owner/revocationNotification.html',context)

def reEncryptedFile(request):
    username=request.session['username']
    doespData=DOESPTransaction.objects.filter(owner_name=username)
    context={'doespData':doespData}
    return render(request,'owner/reEncryptedFile.html',context)

def uploadREFiletoCloud(request,id):
    doespData=get_object_or_404(DOESPTransaction,pk=id)
    cts=cloudTransaction.objects.filter(file_name=doespData.file_name,enc_file=doespData.enc_file,pub_key=doespData.pub_key)
    for ct in cts:
        attributes=ct.attributes
        policies=ct.policies
    if request.method=="POST":
        print('I m in post print')
        attributes=attributes
        policies=policies
        owner_name=doespData.owner_name
        file_name=doespData.file_name
        enc_file=doespData.enc_file
        pub_key=doespData.pub_key
        downloadCount=0
        status="File Uploaded"
        form=cloudTransaction.objects.update(owner_name=owner_name,file_name=file_name,enc_file=enc_file,pub_key=pub_key,status=status,attributes=attributes,policies=policies,downloadCount=downloadCount)
        doespUpdate=DOESPTransaction.objects.filter(id=id).update(status=status)
        print('form sent')
        context={}
        return HttpResponseRedirect(reverse("owner:reEncryptedFile"))
        # return render(request,"owner/uploadCloud.html",context)
    else:
        doespData=get_object_or_404(DOESPTransaction,pk=id)
        context={'doespData':doespData,}
        return render(request,"owner/uploadedFile.html",context)
        # return HttpResponseRedirect(reverse("owner:uploadFiletoCloud"))