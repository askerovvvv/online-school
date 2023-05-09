from django.contrib import admin

from teacher.models import TeacherInformation



@admin.action(description="Selected users approved to be teacher")
def make_teacher(modeladmin, request, queryset):
    queryset.update(status="a")


class TeacherAdmin(admin.ModelAdmin):
    list_display = ["user", "status"]
    # ordering = ["title"]
    actions = [make_teacher]


admin.site.register(TeacherInformation, TeacherAdmin)


