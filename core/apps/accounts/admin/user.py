from django.contrib.auth import admin
from django.utils.translation import gettext_lazy as _
from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm 
from unfold.forms import UserChangeForm
from django.utils.html import format_html




class CustomUserAdmin(admin.UserAdmin, ModelAdmin):
    change_password_form = AdminPasswordChangeForm
    form = UserChangeForm

    list_display = (
        "avatar_tag",
        "first_name",
        "last_name",
        "phone",
        "gender",
        "role",
        "is_active",
        "is_staff",
    )

    autocomplete_fields = ["groups", "user_permissions"]

    fieldsets = (
        (None, {"fields": ("avatar", "phone")}),
        (_("Login info"), {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "gender", "age", "info")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions", "role")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined", "validated_at")}),
    )

    readonly_fields = ("avatar_tag",)

    def avatar_tag(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" style="width:50px; height:50px; object-fit:cover; border-radius:50%;" />', obj.avatar.url)
        return "-"
    avatar_tag.short_description = "Avatar"

    search_fields = ("first_name", "last_name", "phone", "email")
    list_filter = ("role", "gender", "is_active", "is_staff")



class PermissionAdmin(ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class GroupAdmin(ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    autocomplete_fields = ("permissions",)


class SmsConfirmAdmin(ModelAdmin):
    list_display = ["phone", "code", "resend_count", "try_count"]
    search_fields = ["phone", "code"]
