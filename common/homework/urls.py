from django.urls import path

from common.homework import views

app_name = "homework"


urlpatterns = [
        path("", views.HomeworkDetailView.as_view(), name="homework-detail"),
        path("group/", views.HomeworkListView.as_view(), name="homework-list"),
        ]
