from django.contrib import admin

from course.models import *

# @admin.register(Course)
# class Course(admin.ModelAdmin):
#     list_display = ('id', )
#     list_display_links = ('id', )

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Saved)

