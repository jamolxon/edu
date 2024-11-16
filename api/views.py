from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from common import models
from api import serializers


class StudentListAPIView(generics.ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentListSerializer
    lookup_field = "pk"

    def filter_queryset(self, queryset):
        queryset = models.Student.objects.filter(group_id=self.kwargs["pk"]).order_by("-id")
        return queryset


class GroupAPIView(generics.RetrieveAPIView):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer
    lookup_field = "pk"


class AttendanceCreateView(generics.CreateAPIView):
    queryset = models.Attendance.objects.all()
    serializer_class = serializers.AttendanceSerializer


class AttendanceListView(generics.ListAPIView):
    queryset = models.Attendance.objects.all()
    serializer_class = serializers.AttendanceListSerializer
    lookup_field = "pk"

    def filter_queryset(self, queryset):
        return queryset.filter(group_id=self.kwargs["pk"])


class HomeworkListView(generics.ListAPIView):
    queryset = models.Homework.objects.all()
    serializer_class = serializers.HomeworkListSerializer
    lookup_field = "pk"

    def filter_queryset(self, queryset):
        return queryset.filter(group_id=self.kwargs["pk"]).order_by("-id")


class HomeworkCreateView(generics.CreateAPIView):
    queryset = models.Homework.objects.all()
    serializer_class = serializers.HomeworkSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


