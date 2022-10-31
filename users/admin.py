from django.contrib import admin

from .models import UserData


# Register your models here.

class AdminUserData(admin.ModelAdmin):
    list_display = ('id', 'username', 'surname', 'lastname', 'picture', 'status')
    list_display_links = ('id', 'username', 'surname', 'lastname', 'status')
    search_fields = ('username', 'status')


admin.site.register(UserData, AdminUserData)
