from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.accounts.models import DirectorModel

from django.utils.html import format_html


@admin.register(DirectorModel)
class DirectorAdmin(ModelAdmin):
    list_display = (
        "id",
        "avatar_tag",
        "get_username",
        "get_first_name",
        "get_last_name",
        "age",
    )


    def avatar_tag(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" style="width:70px; height:70px; object-fit:cover; border-radius:50%;" />', obj.avatar.url)
        return "-"
    
    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'
    get_username.admin_order_field = 'user__username' 
    
    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'Ism'
    get_first_name.admin_order_field = 'user__first_name' 
    
    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'Familya'
    get_last_name.admin_order_field = 'user__last_name' 