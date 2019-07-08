from django.urls import include, path, re_path
from django.contrib.admin.views.decorators import staff_member_required

from . import views


app_name = 'djangoeditorwidgets'

urlpatterns = [
    path('uploads/', staff_member_required(views.FileUploadView.as_view())),
]
