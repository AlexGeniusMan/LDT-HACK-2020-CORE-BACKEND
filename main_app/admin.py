from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

from .models import *


class GradeAdmin(admin.ModelAdmin):
    filter_horizontal = [
        'grades',
    ]

    def __str__(self):
        return "%s.%s" % (self.model._meta.app_label, self.__class__.__name__)
        # return 'Teachers'


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('last_name', 'first_name', 'middle_name',
                                         'email', 'date_of_birth', 'school')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'last_name', 'first_name',
                       'middle_name', 'groups', 'date_of_birth', 'school'),
        }),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Sprint)
admin.site.register(Task)
admin.site.register(TaskDetail)
admin.site.register(Test)
