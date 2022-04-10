from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm

    list_display = ('username', 'display_name',
                    'group', 'is_admin', 'is_active')
    list_filter = ('group', 'is_admin', 'is_active')
    fieldsets = (
        ('ログイン情報', {'fields': ('username', 'password')}),
        ('ユーザ情報', {
         'fields': ('display_name', 'group',  'email')}),
        ('管理者権限', {'fields': ('is_admin', 'is_active',)}),
    )

    add_fieldsets = (
        ('ログイン情報', {'fields': ('username', 'password1', 'password2')}),
        ('ユーザ情報', {
         'fields': ('display_name',  'email')}),
        ('管理者権限', {'fields': ('group', 'is_admin',)}),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
