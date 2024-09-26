from django.urls import path
from django.contrib.auth.decorators import login_required

from common.group.views import GroupCreateView, GroupDeleteView, GroupListView, GroupUpdateView

app_name = "group"

urlpatterns = [
        path("", login_required(GroupListView.as_view()), name="group-list"), 
        path("<int:pk>/", login_required(GroupUpdateView.as_view()), name="group-update"), 
        path("create/", login_required(GroupCreateView.as_view()), name="group-create"), 
        path("delete/<int:pk>/", login_required(GroupDeleteView.as_view()), name="group-delete"), 
       ]