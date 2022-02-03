from django.contrib import admin
from .models import subjects, assignmentFiles, professor
# Register your models here.


class profAdmin(admin.ModelAdmin):
    list_display = ['prof_full_name', 'email_id']


class subjectsAdmin(admin.ModelAdmin):
    list_display = ['subject_name', 'prof_full_name']


class assignmentFilesAdmin(admin.ModelAdmin):
    list_display = ['assignment_name', 'subject_name']


admin.site.register(subjects, subjectsAdmin)
admin.site.register(assignmentFiles, assignmentFilesAdmin)
admin.site.register(professor, profAdmin)