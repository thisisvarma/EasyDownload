from re import T
from django.db import models

# Create your models here.
class professor(models.Model):

    prof_full_name = models.CharField(max_length=250)
    email_id = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.prof_full_name


class department_details(models.Model):

    department_name = models.CharField(max_length=50, null=True, blank=True)
    department_code = models.CharField(max_length=5, null=True, blank=True)
    department_description = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.department_name

class subjects(models.Model):
    
    department_name = models.ForeignKey(department_details, on_delete=models.CASCADE, null=True, blank=True)
    subject_name = models.CharField(max_length=250, blank=True, null=True)
    subject_description = models.CharField(max_length=500, blank=True, null=True)
    prof_full_name = models.ForeignKey(professor, related_name="Professor", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.subject_name


class assignmentFiles(models.Model):

    assignment_name = models.CharField(max_length=250, blank=True, null=True)
    subject_name = models.ForeignKey(subjects, related_name="subject", on_delete=models.CASCADE, blank=True, null=True)
    assignment_file = models.FileField(upload_to="files", null=True, blank=True)

    def __str__(self):
        return self.assignment_name