from django.urls import path,include
from cloud import views
app_name="cloud"
urlpatterns=[
    path("",views.Home,name="home"),
    path("uploadedFiles",views.uploadedFiles,name="uploadedFiles"),
    path('userRequest',views.userRequest,name='userRequest'),
    path('userRequest/<int:id>',views.verifyAttributes,name='verifyAttributes'),
    path('userRequest/<int:id>/send',views.sendUserFile,name='sendUserFile'),
    # path("manageKey",views.keyManagement,name="keyManagement"),
    # path("cryptography",views.Cryptography,name="cryptography"),

]