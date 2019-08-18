from django.contrib import admin

from .models import UserInfo,UserFace,UserSkin
# Register your models here.
admin.site.register(UserSkin)
admin.site.register(UserFace)
admin.site.register(UserInfo)