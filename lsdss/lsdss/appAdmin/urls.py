from django.urls import path,include
from appAdmin import views
app_name="adminApp"
urlpatterns=[
    path("",views.registerData,name="register"),
    path("appAdmin",views.adminApp,name="adminHome"),
    path("appAdmin/users",views.usersList,name="users"),
    path("appAdmin/owners",views.ownersList,name="owners"),
    path("appAdmin/deleteAllData",views.deleteAllData,name="deleteAllData"),
]