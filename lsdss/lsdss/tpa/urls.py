from django.urls import path,include
from tpa import views
app_name="tpa"
urlpatterns=[
    path("",views.Home,name="home"),
    path("ownerkey/",views.ownerKey,name="ownerkey"),
    path("ownerkey/<int:id>",views.generatePubKey,name="generatePubKey"),
    path("ownerkey/<int:id>/sent",views.sendPubKey,name="sendPubKey"),
    path("userkey",views.userKey,name="userkey"),
    path("userkey/<int:id>",views.generateUserPubKey,name="generateUserPubKey"),
    path("userkey/<int:id>/sent",views.sendUserPubKey,name="sendUserPubKey"),
    path("ownerUploadedFiles",views.ownerUploadedFiles,name="ownerUploadedFiles"),
]