from django.contrib import admin

# Register your models here.
from .models import subjects, assignmentFiles, professor, department_details
# Register your models here.


class profAdmin(admin.ModelAdmin):
    list_display = ['prof_full_name', 'email_id']


class subjectsAdmin(admin.ModelAdmin):
    list_display = ['subject_name', 'prof_full_name']


class assignmentFilesAdmin(admin.ModelAdmin):
    list_display = ['assignment_name', 'subject_name']


class department_detailsAdmin(admin.ModelAdmin):
    list_display = ['department_code', 'department_name']


admin.site.register(subjects, subjectsAdmin)
admin.site.register(assignmentFiles, assignmentFilesAdmin)
admin.site.register(professor, profAdmin)
admin.site.register(department_details, department_detailsAdmin)