from django.contrib import admin
from django.contrib.auth import get_user_model

from teacher.models import TeacherInformation
from teacher.signals import is_teacher


@admin.action(description="Selected users approved to be teacher")
def make_teacher(modeladmin, request, queryset):
    queryset.update(status="a")
    # a = queryset.values_list('user', flat=True)
    data = queryset.values()
    is_teacher(data, 'approve')


@admin.action(description="Selected users disapproved to be teacher")
def disapprove_teacher(modeladmin, request, queryset):
    queryset.update(status="d")
    # a = queryset.values_list('user', flat=True)
    data = queryset.values()
    is_teacher(data, 'disapprove')


class TeacherAdmin(admin.ModelAdmin):
    list_display = ["user", "status"]
    # ordering = ["title"]
    actions = [make_teacher, disapprove_teacher]


admin.site.register(TeacherInformation, TeacherAdmin)


