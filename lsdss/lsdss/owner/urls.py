from django.urls import path,include
from owner import views
from django.conf import settings
from django.conf.urls.static import static
app_name="owner"
urlpatterns=[
    path("",views.Home,name="home"),
    path("manageKey",views.keyManagement,name="keyManagement"),
    path("cryptography",views.cryptography,name="cryptography"),
    path("uploadFile",views.uploadFile,name="uploadFile"),
    path("deleteFile/<int:id>",views.uploadedFileDelete,name="uploadedFileDelete"),
    path("encryptFile/<int:id>",views.sendFiletoEncryption,name="sendFiletoEncryption"),
    path("uploadFiletoCloud/<int:id>",views.uploadFiletoCloud,name="uploadFiletoCloud"),
    path("uploadedFile",views.uploadedFile,name="uploadedFile"),
    path("userList",views.showUserList,name="showUserList"),
    path("revocationNotification",views.revocationNotification,name="revocationNotification"),
    path("revocation/<int:id>",views.revocation,name="revocation"),
    # Re-encrypted Files
    path("reEncrypted",views.reEncryptedFile,name="reEncryptedFile"),
    path("uploadREFiletoCloud/<int:id>",views.uploadREFiletoCloud,name="uploadREFiletoCloud"),
]

# if settings.DEBUG:
#     urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
