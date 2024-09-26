from django.urls import path
from django.contrib.auth.decorators import login_required

from common.mentor.views import MentorCreateView, MentorDeleteView, MentorListView, MentorUpdateView

app_name = "mentor"

urlpatterns = [
        path("", login_required(MentorListView.as_view()), name="mentor-list"), 
        path("<int:pk>/", login_required(MentorUpdateView.as_view()), name="mentor-update"), 
        path("create/", login_required(MentorCreateView.as_view()), name="mentor-create"), 
        path("delete/<int:pk>/", login_required(MentorDeleteView.as_view()), name="mentor-delete"), 
       ]