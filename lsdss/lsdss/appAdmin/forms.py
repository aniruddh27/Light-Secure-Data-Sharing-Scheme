from appAdmin.models import register, ownerFileUpload,cloudTransaction,DUCTransaction
from django.contrib.auth.models import User
from django import forms

class registerForm(forms.ModelForm):

    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.widgets.PasswordInput)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    # address=forms.CharField(max_length=200,widget=forms.Textarea)

    class Meta:
        model = register
        fields=['username','password','first_name','last_name','city','email','mobile','address','module']


class ownerFileUploadForm(forms.ModelForm):

    class Meta:
        model=ownerFileUpload
        fields=['file_name','owner_file']


class cloudFileUploadForm(forms.ModelForm):

    class Meta:
        model=cloudTransaction
        fields=['attributes','policies']

class DUCTransactionForm(forms.ModelForm):

    class Meta:
        model=DUCTransaction
        fields=['attributes']