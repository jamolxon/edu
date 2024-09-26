from django.urls import path, include
from django.contrib.auth.decorators import login_required



from common.views import AttendanceListView, AttendanceView, HomeView

urlpatterns = [
        path("", login_required(HomeView.as_view()), name="home"),
        path("student/", include("common.student.urls")),
        path("attendance/", AttendanceView.as_view(), name="attendance"),
        path("attendance-list/", AttendanceListView.as_view(), name="attendance-list")

        ]
