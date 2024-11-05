from rest_framework import serializers

from common import models


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ("id", "first_name", "last_name")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = ("id", "name", "day_type")


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Attendance
        fields = ("id", "group", "student", "attendance_date", "type")


class AttendanceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Attendance
        fields = ("id", "student", "attendance_date", "type")
