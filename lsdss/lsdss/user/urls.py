from django.urls import path,include
from user import views
app_name="user"
urlpatterns=[
    path("",views.Home,name="home"),
    path("viewFiles",views.ViewFiles,name="viewFiles"),
    path("manageKey",views.keyManagement,name="keyManagement"),
    path("cryptography",views.Cryptography,name="cryptography"),
    path("cloudFiles",views.cloudFiles,name="cloudFiles"),
    path("ownerNotification",views.ownerNotification,name="ownerNotification"),
    path("decryptFile/<int:id>",views.sendFiletoDecryption,name="sendFiletoDecryption"),
    path("decryptedFile/",views.decryptedFile,name="decryptedFile"),
    # path("decryptedFile/<int:id>",views.viewDecryptedFile,name="viewDecryptedFile"),
]