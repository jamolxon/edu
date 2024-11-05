from rest_framework import generics
from rest_framework import permissions

from common import models
from api import serializers


class StudentListAPIView(generics.ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentListSerializer
    lookup_field = "pk"

    def filter_queryset(self, queryset):
        queryset = models.Student.objects.filter(group_id=self.kwargs["pk"])
        return queryset


class GroupAPIView(generics.RetrieveAPIView):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer
    lookup_field = "pk"


class AttendanceCreateView(generics.CreateAPIView):
    queryset = models.Attendance.objects.all()
    serializer_class = serializers.AttendanceSerializer


class AttendanceListView(generics.ListAPIView):
    queryset = models.Attendance.objects.all().order_by("-id")
    serializer_class = serializers.AttendanceListSerializer
    lookup_field = "pk"

    def filter_queryset(self, queryset):
        return queryset.filter(group_id=self.kwargs["pk"])
