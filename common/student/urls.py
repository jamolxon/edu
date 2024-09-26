from django.urls import path
from django.contrib.auth.decorators import login_required

from common.student.views import StudentCreateView, StudentDeleteView, StudentListView, StudentUpdateView

app_name = "student"

urlpatterns = [
        path("", login_required(StudentListView.as_view()), name="student-list"), 
        path("<int:pk>/", login_required(StudentUpdateView.as_view()), name="student-update"), 
        path("create/", login_required(StudentCreateView.as_view()), name="student-create"), 
        path("delete/<int:pk>/", login_required(StudentDeleteView.as_view()), name="student-delete"), 
       ]
