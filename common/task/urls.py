from django.urls import path

from common.task import views

app_name = "task"


urlpatterns = [
        path("", views.TaskListView.as_view(), name="task-list"),
        path("student/", views.StudentTaskListView.as_view(), name="student-task-list"),
        path("create/", views.TaskCreateView.as_view(), name="task-create"),
        path("update/<int:pk>/", views.TaskUpdateView.as_view(), name="task-update"),
        path("delete/<int:pk>/", views.TaskDeleteView.as_view(), name="task-delete"),
        path("<int:pk>/", views.TaskDetailView.as_view(), name="task-detail"),
        ]
