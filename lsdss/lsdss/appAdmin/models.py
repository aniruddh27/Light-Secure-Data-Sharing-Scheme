from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import base64

modules=(('Owner','Owner'),('User','User'),('tpa','tpa'),('admin','admin'),('espdsp','espdsp'),('cloud','cloud'))

class register(models.Model):
    user=models.OneToOneField(User,unique=True,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10)
    city = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    module = models.CharField(max_length=20, choices=modules)
    strdate = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class DOTATransaction(models.Model):
    owner_name=models.CharField(max_length=30)
    attributes=models.ForeignKey(register,on_delete=models.CASCADE)
    pub_key=models.CharField(max_length=300)
    # _pub_key=models.CharField(max_length=300)

    # def set_data(self, data):
    #     self._pub_key = base64.encodestring(data)

    # def get_data(self):
    #     return base64.decodestring(self._pub_key)

    # pub_key = property(get_data, set_data)
    status=models.CharField(max_length=20)

    def __str__(self):
        return self.owner_name


class ownerFileUpload(models.Model):
    owner_name=models.CharField(max_length=30,null=True,blank=True)
    file_name=models.CharField(max_length=30)
    owner_file=models.FileField(upload_to='media')
    file_status=models.CharField(max_length=30)
    file_upload_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name

class DOESPTransaction(models.Model):
    # owner=models.ForeignKey(ownerFileUpload,on_delete=models.CASCADE)
    owner_name=models.CharField(max_length=30)
    file_name=models.CharField(max_length=30)
    file_path=models.CharField(max_length=100)
    pub_key=models.CharField(max_length=300)
    status=models.CharField(max_length=30)
    enc_file=models.CharField(max_length=100)
    reEnc_file=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.file_name

class cloudTransaction(models.Model):
    owner_name=models.CharField(max_length=30)
    file_name=models.CharField(max_length=30)
    enc_file=models.CharField(max_length=100)
    pub_key=models.CharField(max_length=300)
    status=models.CharField(max_length=30)
    attributes=models.CharField(max_length=500)
    policies=models.CharField(max_length=500)
    downloadCount=models.PositiveIntegerField()

    def __str__(self):
        return self.file_name

#Owner and User Transaction
class DODUTransaction(models.Model):
    owner_name=models.CharField(max_length=30)
    file_name=models.CharField(max_length=30)
    attributes=models.CharField(max_length=500)
    user_list=models.CharField(max_length=500)
    status=models.CharField(max_length=30)
    
    def __str__(self):
        return self.owner_name

# User Transaction
class DUTATransaction(models.Model):
    user_name=models.CharField(max_length=30)
    attributes=models.ForeignKey(register,on_delete=models.CASCADE)
    pub_key=models.CharField(max_length=300)
    status=models.CharField(max_length=20)

    def __str__(self):
        return self.user_name

class DUCTransaction(models.Model):
    owner_name=models.CharField(max_length=30)
    user_name=models.CharField(max_length=30)
    pub_key=models.CharField(max_length=300)
    attributes=models.CharField(max_length=500)
    status=models.CharField(max_length=30)
    file_name=models.CharField(max_length=30,null=True,blank=True)
    enc_file=models.CharField(max_length=300)
    

    def __str__(self):
        return self.user_name

class DUCDECTransaction(models.Model):
    owner_name=models.CharField(max_length=30)
    user_name=models.CharField(max_length=30)
    pub_key=models.CharField(max_length=300)
    status=models.CharField(max_length=30)
    file_name=models.CharField(max_length=30)
    enc_file=models.CharField(max_length=300)
    dec_file=models.CharField(max_length=300)

    def __str__(self):
        return self.user_name