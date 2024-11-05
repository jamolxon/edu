from django.views.generic import DetailView, View
from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView

from common.models import Attendance, Group


class AttendanceView(ListView):
    model = Group
    queryset = model.objects.all()
    template_name = "attendance/index.html"


class GroupListView(ListView):
    model = Group
    template_name = "attendance/group.html"
    context_object_name = "objects"
    queryset = model.objects.all().order_by("-id").filter()
    paginate_by = 10


    def get_queryset(self):
        object_list = self.queryset
        search = self.request.GET.get("search", None)
        if search:
            object_list = object_list.filter(
                    Q(name__icontains=search))

        return object_list
 
