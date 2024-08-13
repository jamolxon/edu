from logging import log
from django.urls import path
from django.contrib.auth.decorators import login_required

from common.student.views import StudentListView

app_name = "student"

urlpatterns = [
        path("", login_required(StudentListView.as_view()), name="student-list"), 
       ]
