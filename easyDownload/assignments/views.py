from django.shortcuts import render, redirect
from .forms import AssignmentsForm
from django.contrib import messages
from .models import assignmentFiles
import os
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def def_home(request):

    assigments = assignmentFiles.objects.all()
    return render(request, template_name='home.html', context={'assigments': assigments})


@login_required
def home(request):

    if request.method == 'POST':
        assignment_form = AssignmentsForm(request.POST, request.FILES)

        if assignment_form.is_valid():
            post = assignment_form.save(commit=False)
            assignment_form.save()
            messages.success(request, message=f'You have posted items successfully \n {assignment_form.errors}')
            return redirect('/')
        else:
            messages.error(request, f'Please correct the error below. \n {assignment_form.errors}')
    else:
        assignment_form = AssignmentsForm()
        assigments = assignmentFiles.objects.all()

    return render(request, template_name="home.html", context={'assignment_form': assignment_form,
                                                                "assignments": assigments
                                                                })
