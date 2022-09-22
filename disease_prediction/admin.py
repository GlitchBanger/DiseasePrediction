from django.contrib import admin
from .models import LoginDetails, UserData, Records

# Register your models here.
admin.site.register(LoginDetails)

admin.site.register(UserData)

admin.site.register(Records)
