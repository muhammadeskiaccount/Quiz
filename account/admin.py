from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
from .forms import AccountChangeForm, AccountCreationForm


class AccountAdmin(UserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2')}),
    )
    list_display = ('id', 'email', 'first_name', 'last_name', 'image_tag',
                    'is_staff', 'is_active', 'is_superuser', 'date_created', 'date_modified')
    ordering = None
    readonly_fields = ('date_created', 'date_modified')
    list_filter = ('date_created', 'is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'image', 'bio')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important date', {'fields': ('date_modified', 'date_created')}),
    )
    search_fields = ('email', 'first_name', 'last_name')


admin.site.register(Account, AccountAdmin)

#
# from django.contrib import admin
# from .models import Account
#
#
# @admin.register(Account)
# class AccountAdmin(admin.ModelAdmin):
#     list_display = ['id', 'first_name', 'last_name', 'image', 'bio']
