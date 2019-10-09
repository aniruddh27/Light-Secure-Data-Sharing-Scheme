from django.contrib import admin
from appAdmin.models import register,DOTATransaction, ownerFileUpload,DOESPTransaction,cloudTransaction,DUTATransaction,DODUTransaction,DUCTransaction,DUCDECTransaction
# Register your models here.
admin.site.register(register)
admin.site.register(DOTATransaction)
admin.site.register(ownerFileUpload)
admin.site.register(DOESPTransaction)
admin.site.register(cloudTransaction)
admin.site.register(DUTATransaction)
admin.site.register(DODUTransaction)
admin.site.register(DUCTransaction)
admin.site.register(DUCDECTransaction)