from django.urls import path
from .views import new_user_registration, login_request, logout_request
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register', new_user_registration, name='register'),
    path('login', login_request, name='login'),
    path('logout', logout_request, name='logout'),
    # path(r'^download/(?P<path>.*)$')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)