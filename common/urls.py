from django.urls import path, include
from django.contrib.auth.decorators import login_required

from common.views import HomeView

urlpatterns = [
        path("", login_required(HomeView.as_view()), name="home"),
        path("student/", include("common.student.urls")),
        path("mentor/", include("common.mentor.urls")),
        path("group/", include("common.group.urls")),
        path("attendance/", include("common.attendance.urls")),
        path("task/", include("common.task.urls")),
        path("homework/", include("common.homework.urls")),

        ]
