from django.urls import path,include
from encdec import views
app_name="encdec"
urlpatterns=[
    path("",views.Home,name="home"),
    path("encryption",views.encryption,name="encryption"),
    path("encryption/<int:id>",views.encryptFile,name="encryptFile"),
    path("encryption/File:<int:id>",views.sendEncryptedFiles,name="sendEncryptedFiles"),
    path("decryption",views.decryption,name="decryption"),
    path("decryption/<int:id>",views.decryptFile,name="decryptFile"),
    path("decryption/<int:id>/sent",views.sendDecryptedFile,name="sendDecryptedFile"),

    path("reEncryption",views.reEncryption,name="reEncryption"),
    path("reEncryption/<int:id>",views.reEncryptFile,name="reEncryptFile"),
    path("reEncryption/File:<int:id>",views.sendReEncryptedFiles,name="sendReEncryptedFiles"),
    
    
]