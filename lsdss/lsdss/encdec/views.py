from django.shortcuts import render,get_object_or_404
from appAdmin.models import DOESPTransaction,DUCDECTransaction,DUCTransaction
from django.http import HttpResponseRedirect
from django.urls import reverse
import base64
import hashlib
import os,random,struct,sys
from cryptography.fernet import Fernet
from django.core.files.storage import FileSystemStorage


# Create your views here.
def Home(request):
    context={}
    return render(request,"enc_dec/home.html",context)

def encryption(request):
    doespData=DOESPTransaction.objects.all()
    context={'doespData':doespData}
    return render(request,"enc_dec/encryption.html",context)

def encryptFile(request,id):
    if request.method=='POST':
        doespData=get_object_or_404(DOESPTransaction,pk=id)
        print(doespData.file_name)
        print(doespData.file_path)
        input_file='/home/lsdss/lsdss/'+ doespData.file_path
        i1=input_file.split('/')
        i1=str(i1[5])
        i2=i1.split('.')
        # print(i[2])
        key = Fernet.generate_key()
        print(input_file)
        print(key)
        with open(input_file, 'rb') as f:
            data = f.read()
        print(data)
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
        print('enc--',encrypted)
        output_file=(str(i2[0])+'.encrypted')
        print(output_file)
        with open(output_file, 'wb+') as of:
            of.write(encrypted)

            fs = FileSystemStorage()
            filename = fs.save(output_file, of)
            encrypted_file_url = fs.url(filename)
        print(encrypted_file_url)


        status="File Encrypted"
        enc_file=encrypted_file_url
        doespUpdate=DOESPTransaction.objects.filter(id=id).update(status=status,enc_file=enc_file)
        doespData=get_object_or_404(DOESPTransaction,pk=id)
        context={'doespData':doespData}
        return HttpResponseRedirect(reverse("encdec:encryption"))
    else:
        return HttpResponseRedirect(reverse("encdec:encryption"))
    # doespData=get_object_or_404(DOESPTransaction,id=id)
    # owner_key=doespData.pub_key
    # print(owner_key)
    # key1= owner_key.encode("utf8")
    # print(len(key1))
    # key= '0123456789abcdef'
    # in_filename = doespData.file_path
    # out_filename = None
    # chunksize = 64*1024
    # aesEnc=AESEncryption(key.encode("utf8"),in_filename,out_filename,chunksize)
    # context={}
    # return HttpResponseRedirect(reverse("encdec:encryption"))
    # return render(request,"enc_dec/encryption.html",context)

def sendEncryptedFiles(request,id):
    if request.method=='POST':
        doespData=get_object_or_404(DOESPTransaction,pk=id)
        print('status-->',doespData.status)
        if doespData.status=="File Encrypted":
            status="File Sent to Owner"

        doespUpdate=DOESPTransaction.objects.filter(id=id).update(status=status)
        doespData=get_object_or_404(DOESPTransaction,pk=id)
        context={'doespData':doespData}
        return HttpResponseRedirect(reverse("encdec:encryption"))
    else:
        return HttpResponseRedirect(reverse("encdec:encryption"))


def decryption(request):
    ducdecData=DUCDECTransaction.objects.all()
    context={'ducdecData':ducdecData}
    return render(request,"enc_dec/decryption.html",context)
    # return HttpResponseRedirect(reverse("encdec:decryption"))

def decryptFile(request,id):
    print(id)
    ducdecData=get_object_or_404(DUCDECTransaction,pk=id)
    print(ducdecData.id)
    encFile=ducdecData.enc_file
    print(encFile)
    doesps=DOESPTransaction.objects.filter(enc_file=encFile)
    for doesp in doesps:
        decFile= doesp.file_path

    print(doesp.file_path)
    d1=decFile.split('/')
    vl = '/'
    # decFile1=d1
    decFile1=d1[1] + vl +d1[2]
    # print(decFile)
    status="File Decrypted"
    ducdecuData=DUCDECTransaction.objects.filter(pk=id).update(dec_file=decFile1,status=status)
    ducdatas=DUCTransaction.objects.filter(pk=id).update(status=status)
    context={}
    # return render(request,"enc_dec/decryption.html",context)
    return HttpResponseRedirect(reverse("encdec:decryption"))

def sendDecryptedFile(request,id):
    print("Send me")
    ducdecData=get_object_or_404(DUCDECTransaction,pk=id)
    print(ducdecData)
    status="Decrypted File Sent"
    ducdecuData=DUCDECTransaction.objects.filter(pk=id).update(status=status)
    ducdatas=DUCTransaction.objects.filter(pk=id).update(status=status)
    print(ducdecData)
    context={}
    # return render(request,"enc_dec/decryption.html",context)
    return HttpResponseRedirect(reverse("encdec:decryption"))


def AESEncryption(key,in_filename,out_filename,chunksize):
    if not out_filename:
        out_filename = in_filename + '.enc'
    iv=(16 * '\x00').encode("utf8")
    # iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(12)).encode("utf8")
    print('iv---',len(iv))
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += bytes(16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))

 # key = '0123456789abcdef'
    # IV = 16 * '\x00'           # Initialization vector: discussed later
    # mode = AES.MODE_CBC
    # encryptor = AES.new(key.encode("utf8"), mode, IV=IV.encode("utf8"))

    # text = 'j' * 64 + 'i' * 128
    # ciphertext = encryptor.encrypt(text.encode("utf8"))
    # print(key)
    # print('text-------',text)
    # print('ciphertext-------',ciphertext)


# Revocation
# Re encryption

def reEncryption(request):
    # status='File Sent for Re-Encryption'
    # doespData=DOESPTransaction.objects.filter(status=status)
    doespData=DOESPTransaction.objects.all()
    context={'doespData':doespData}
    return render(request,'enc_dec/reEncryption.html',context)

def reEncryptFile(request,id):
    if request.method=='POST':
        doespData=get_object_or_404(DOESPTransaction,pk=id)
        print(doespData.file_name)
        print(doespData.enc_file)
        # input_file=doespData.enc_file
        # inp=input_file.split('/')
        # i1=str(inp[2])
        input_file='/home/lsdss/lsdss/'+ doespData.enc_file
        i1=input_file.split('/')
        i1=str(i1[5])
        i2=i1.split('.')
        # print(i[2])
        key = Fernet.generate_key()
        print(input_file)
        print(key)
        with open(input_file, 'rb') as f:
            data = f.read()
        print(data)
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
        print('enc--',encrypted)
        output_file=('(re)'+str(i2[0])+'.encrypted')
        print(output_file)
        with open(output_file, 'wb+') as of:
            of.write(encrypted)

            fs = FileSystemStorage()
            filename = fs.save(output_file, of)
            encrypted_file_url = fs.url(filename)
        print(encrypted_file_url)


        status="File Re-encrypted"
        reEnc_file=encrypted_file_url
        doespUpdate=DOESPTransaction.objects.filter(id=id).update(status=status,reEnc_file=reEnc_file)
        doespData=get_object_or_404(DOESPTransaction,pk=id)
        context={'doespData':doespData}
        return HttpResponseRedirect(reverse("encdec:reEncryption"))
    else:
        return HttpResponseRedirect(reverse("encdec:reEncryption"))

def sendReEncryptedFiles(request,id):
    if request.method=='POST':
        doespData=get_object_or_404(DOESPTransaction,pk=id)
        print('status-->',doespData.status)
        if doespData.status=="File Re-encrypted":
            status="Re-Encrypted File Sent to Owner"

        doespUpdate=DOESPTransaction.objects.filter(id=id).update(status=status)
        doespData=get_object_or_404(DOESPTransaction,pk=id)
        context={'doespData':doespData}
        return HttpResponseRedirect(reverse("encdec:reEncryption"))
    else:
        return HttpResponseRedirect(reverse("encdec:ReEncryption"))

