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


class HomeworkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Homework
        fields = ("id", "student", "homework_date", "type")


class HomeworkSerializer(serializers.Serializer):
    group = serializers.CharField()
    student = serializers.CharField()
    homework_date = serializers.DateField()
    type = serializers.CharField()

    def create(self, validated_data):
        homework = models.Homework.objects.create(
            group_id=validated_data["group"],
            student_id=validated_data["student"],
            homework_date=validated_data["homework_date"],
            type=validated_data["type"],
        )
        return homework
