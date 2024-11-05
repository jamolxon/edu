from django.urls import path

from common.attendance.views import AttendanceView
from common.attendance.views import GroupListView

app_name = "attendance"


urlpatterns = [
        path("", AttendanceView.as_view(), name="attendance-list"),
        path("group/", GroupListView.as_view(), name="group-list")
        ]


