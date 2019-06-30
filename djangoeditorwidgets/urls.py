from django.urls import include, path, re_path
from django.contrib.admin.views.decorators import staff_member_required

from . import views


app_name = 'djangoeditorwidgets'

urlpatterns = [
    # path('manager/',
    #      staff_member_required(views.IndexView.as_view()), name="index"),
    # path('manager/path',
    #      staff_member_required(views.IndexView.as_view(api=True)), name="api"),

    # path('manager/search',
    #      staff_member_required(views.IndexView.as_view(search=True)), name="search"),

    # path('manager/upload/',
    #      staff_member_required(views.FileUploadView.as_view()), name="upload"),
]
