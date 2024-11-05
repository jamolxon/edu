from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator
from django.conf import settings
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import AbstractUser

from django_resized import ResizedImageField

from common.manager import UserManager


class RoleChoices(models.TextChoices):
    student = "student", _("Student")
    parent = "parent", _("Parent")
    teacher = "teacher", _("Teacher")
    staff = "staff", _("Moderator")
    superuser = "superuser", _("Superuser")


class DayChoices(models.TextChoices):
    mwf = "mwf", _("Monday, Wednesday, Friday")
    tts = "tts", _("Tuesday, Thursday, Saturday")


class BaseUser(AbstractUser):
    full_name = models.CharField(_("full name"), max_length=256)
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(_("username"), max_length=256, unique=True, help_text=_(
        "Majburiy! 5 yoki undan ko'p bo'lgan belgi. Faqat harflar, raqamlar va @/./+/-/_."
        ), null=True, validators=[username_validator, MinLengthValidator(5)])
    bio = models.TextField(_("bio"), blank=True, null=True)
    image = ResizedImageField(
            size=[500, 500],
            crop=["middle", "center"],
            verbose_name=_("image"),
            quality=90,
            upload_to="user/%Y/%m",
            blank=True,
            null=True,
            )
    role = models.CharField(
            _("user role"),
            max_length=12,
            choices=RoleChoices.choices
            )

    created_at = models.DateTimeField(_("date created"), auto_now_add=True, null=True)
    updated_at = models.DateTimeField(_("date updated"), auto_now=True)

    USERNAME_FIELD = "username"
    first_name = None
    last_name = None
    REQUIRED_FIELDS = ["full_name"]

    objects = UserManager()


    def __str__(self):
        return f"{self.full_name}"

    class Meta:
        db_table = "user"
        verbose_name = _("user")
        verbose_name_plural = _("users")


class Teacher(models.Model):
    full_name = models.CharField(_("full name"), max_length=256)
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            related_name="teachers",
            on_delete=models.CASCADE,
            verbose_name=_("user"),
            null=True
            )

    description = models.TextField(_("description"), blank=True, null=True)
    image = ResizedImageField(size=[500, 500], crop=["middle", "center"], quality=100, null=True, verbose_name=_("image"), upload_to="teacher/%Y/%m")
    is_active = models.BooleanField(_("teacher is active"), default=True)

    date_created = models.DateField(_("date created"), default=timezone.now)
    date_updated = models.DateTimeField(_("date updated"), auto_now=True)

    def __str__(self):
        return f"{self.full_name}"

    class Meta:
        db_table = "teacher"
        verbose_name = _("teacher")
        verbose_name_plural = _("teachers")


class Group(models.Model):
    name = models.CharField(_("name"), max_length=256)
    teacher = models.ForeignKey(
            Teacher,
            related_name="groups",
            on_delete=models.CASCADE,
            verbose_name=_("teacher"),
            null=True
            )
    description = models.TextField(_("description"), blank=True, null=True)
    day_type = models.CharField(_("day type"), choices=DayChoices.choices, null=True)
    start_date = models.DateField(_("start date"))
    end_date = models.DateField(_("end date"))
    duration = models.IntegerField(_("duration"), default=12)

    date_created = models.DateField(_("date created"), default=timezone.now)
    date_updated = models.DateTimeField(_("date updated"), auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "group"
        verbose_name = _("group")
        verbose_name_plural = _("groups")


class Student(models.Model):
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            related_name="students",
            on_delete=models.CASCADE,
            verbose_name=_("user"),
            null=True
            )

    first_name = models.CharField(_("first name"), max_length=256)
    last_name = models.CharField(_("last name"), max_length=256)
    gender = models.CharField(_("gender"), max_length=100, choices=[('Male', 'Male'),('Female', 'Female')], blank=True, null= True)
    image = ResizedImageField(size=[500, 500], crop=["middle", "center"], quality=100, null=True, verbose_name=_("image"), upload_to="student/%Y/%m")
    birth_date = models.DateField(_("birth date"))
    phone_number = models.CharField(_("phone number"), max_length=250, blank=True, null= True)
    parent_number = models.CharField(_("parent number"), max_length=250, blank=True, null= True)
    group = models.ForeignKey(
            Group,
            related_name="students",
            on_delete=models.CASCADE,
            verbose_name=_("group"),
            null=True
            )

    description = models.TextField(_("description"), blank=True, null=True)
    balance = models.IntegerField(_("balance"), default=0)

    date_created = models.DateField(_("date created"), default=timezone.now)
    date_updated = models.DateTimeField(_("date updated"), auto_now=True)

    class Meta:
        db_table = "student"
        verbose_name = _("student")
        verbose_name_plural = _("students")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Lesson(models.Model):
    name = models.CharField(_("name"), max_length=256)
    group = models.ForeignKey(Group,on_delete=models.CASCADE, related_name="lessons", verbose_name=_("group"))
    description = models.TextField(_("description"))
    date = models.DateField(_("date"))

    class Meta:
        db_table = "lesson"
        verbose_name = _("lesson")
        verbose_name_plural = _("lessons")

    def __str__(self):
        return f"{self.name} - {self.date}"



class Attendance(models.Model):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name="attendences", verbose_name=_("group"))
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="attendences", verbose_name=_("student"))
    attendance_date = models.DateField(_("attendence_date"))
    type = models.CharField(max_length=250, choices = [('present','Present'), ('absent','Absent')], verbose_name=_("attendence type"))

    class Meta:
        db_table = "attendance"
        verbose_name = _("attendance")
        verbose_name_plural = _("attendences")

    def __str__(self):
        return f"{self.group.name}"

