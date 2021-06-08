from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from main.resources import StudentResource
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Дополнительная информация'


class UserAdmin(UserAdmin):
    inlines = (UserInline,)

@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):
    fields = ('name', )
    list_display = ('name', )
    list_filter = ('name', )


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    fields = ('name', 'salary', )
    list_display = ('name', 'salary', )
    list_filter = ('name', 'salary', )

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ('user', 'name', 'surname', 'middle_name', 'date_of_birth', 'number', 'group', )
    list_display = ('user','name', 'surname', 'middle_name', 'date_of_birth', 'number', 'group', )
    list_filter = ('user','name', 'surname', 'middle_name', 'date_of_birth', 'number', 'group', )


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    fields = ('fk_student', 'fk_discipline', 'fk_homework_check', )
    list_display = ('fk_student', 'fk_discipline', 'fk_homework_check', )
    list_filter = ('fk_student', 'fk_discipline', 'fk_homework_check', )

@admin.register(Distribution)
class DistributionAdmin(admin.ModelAdmin):
    fields = ('fk_discipline', 'fk_employee', 'fk_group_name', )
    list_display = ('fk_discipline', 'fk_employee', 'fk_group_name', )
    list_filter = ('fk_discipline', 'fk_employee', 'fk_group_name', )

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    fields = ('fk_student', 'fk_discipline', 'date_of_visit', 'presence', )
    list_display = ('date_of_visit', 'presence', )
    list_filter = ('date_of_visit', 'presence', )


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    fields = ('fk_employee', 'title', 'description','presence', 'file', 'date_of_deliviri', 'appointment_date', 'fk_group', )
    list_display = ('title', 'description', 'presence','file', 'date_of_deliviri', 'appointment_date', )
    list_filter = ('title', 'description', 'presence', 'file', 'date_of_deliviri', 'appointment_date', )

@admin.register(Homework_check)
class Homework_checkAdmin(admin.ModelAdmin):
    fields = ('assessment', 'fk_employee', 'fk_homework', 'fk_student', )
    list_display = ('assessment', )
    list_filter = ('assessment', )

@admin.register(Group_name)
class Group_nameAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'course', 'fk_discipline', )
    list_display = ('name', 'description', 'course', )
    list_filter = ('name', 'description', 'course', )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


resource_class = StudentResource

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fields = ('title', 'post','image', 'date', )
    list_display = ('title', 'post','image', 'date', )
    list_filter = ('title', 'post','image', 'date', )
