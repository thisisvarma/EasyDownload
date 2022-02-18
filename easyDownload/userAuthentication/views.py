from django.shortcuts import render, redirect
from .forms import NewRegistration
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

# Create your views here.
def new_user_registration(request):

    if request.method == 'POST':
        form = NewRegistration(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, message='Account - {} has been created'.format(username))
            return redirect(login_request)
    else:
        form = NewRegistration()

    return render(request=request, template_name='registration.html', context={'form': form})


def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        next_value = request.POST.get('next')
        print(f'next_value is {next_value}')
        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, message=f'your login attempt is successful')

                if next_value == "":
                    return redirect("/")
                else:
                    return redirect(f'{next_value}')
            else:
                messages.error(request, message=f'invalid username/password')

    else:
        form = AuthenticationForm()
    return render(request, template_name='login.html', context={
        'form': form
        })

def logout_request(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.!')
    return redirect('login')






# def download(request, path):
#     file_path = os.path.join(settings.MEDIA_ROOT, path)
#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as fh:
#             response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
#             response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
#             return response
#     raise Http404
