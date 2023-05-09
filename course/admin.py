from django.contrib import admin

from course.models import *



@admin.register(Course)
class Course(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    list_display_links = ('id', 'title', 'category')
    search_fields = ('title', 'id')
    list_filter = ('category', )
    # inlines = (Category2,)

admin.site.register(Category)
admin.site.register(Saved)

