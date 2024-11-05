from django.urls import path

from api import views


urlpatterns = [
        path("group/<int:pk>/students/", views.StudentListAPIView.as_view(), name="group-students"),
        path("group/<int:pk>/", views.GroupAPIView.as_view(), name="group-detail"),
        path("group/attendance/create/", views.AttendanceCreateView.as_view(), name="attendance-create"),
        path("group/<int:pk>/attendance/", views.AttendanceListView.as_view(), name="attendance-list")
        ]
