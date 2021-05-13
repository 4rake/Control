from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from main.resources import StudentResource
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


class UserAdmin(UserAdmin):
    inlines = (UserInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Access)
admin.site.register(Student)
admin.site.register(Group_name)
admin.site.register(Information)
admin.site.register(Homework_check)
admin.site.register(Homework)
admin.site.register(Position)
admin.site.register(Discipline)
admin.site.register(Diary)




#admin.site.register(Homework)




resource_class = StudentResource
