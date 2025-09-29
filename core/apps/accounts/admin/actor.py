from django.contrib import admin
from unfold.admin import ModelAdmin
from core.apps.accounts.models import ActorprofileModel
from django.utils.html import format_html



@admin.register(ActorprofileModel)
class ActorprofileAdmin(ModelAdmin):
    list_display = (
        "id",
        "avatar_tag",
        "full_name",
        "get_username", 
        "get_phone",
        "age",
        "gender",
    )


    def avatar_tag(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" style="width:70px; height:70px; object-fit:cover; border-radius:50%;" />', obj.avatar.url)
        return "-"
    
    def get_username(self, obj):
            return obj.user.username
    get_username.short_description = 'Username'
    get_username.admin_order_field = 'user__username' 

    # User modeli phone
    def get_phone(self, obj):
        return obj.user.phone  
    get_phone.short_description = 'Phone'
    get_phone.admin_order_field = 'user__phone'

    search_fields = ("full_name", "gender", "user__username", "user__phone")
    list_filter = ("gender", )