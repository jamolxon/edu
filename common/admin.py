from django.contrib import admin

from common import models



@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")



admin.site.register(models.Group)
admin.site.register(models.Teacher)
admin.site.register(models.Attendance)
admin.site.register(models.Task)



@admin.register(models.BaseUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "username")
    search_fields = ("full_name", "email")
    list_filter = ("role", "created_at")
    filter_horizontal = ("user_permissions",)

    fieldsets = (
        (
            "Authentication Info",
            {"fields": ("password",)},
        ),
        (
            "Personal info",
            {
                "fields": (
                    "role",
                    "full_name",
                    "username",
                    "image",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )

