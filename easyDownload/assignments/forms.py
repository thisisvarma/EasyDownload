from .models import assignmentFiles
from django import forms

class AssignmentsForm(forms.ModelForm):
    class Meta:
        model = assignmentFiles
        fields = "__all__"
