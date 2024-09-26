from django.db.models import Q
from django.views.generic import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin

from helpers.views import CreateView, DeleteView, UpdateView
from common.models import Teacher
from common.mentor.forms import TeacherForm



class MentorListView(ListView):
    model = Teacher
    template_name = "mentor/list.html"
    context_object_name = "objects"
    queryset = model.objects.all().order_by("-id")
    paginate_by = 10


    def get_queryset(self):
        object_list = self.queryset
        search = self.request.GET.get("search", None)
        if search:
            object_list = object_list.filter(
                    Q(full_name__icontains=search))

        return object_list


class MentorCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = "mentor/create.html"
    context_object_name = "object"
    success_url = "mentor:mentor-list"
    success_create_url = "mentor:mentor-create"
    # permission_required = 'product.add_product'



class MentorUpdateView(UpdateView):
    model = Teacher
    template_name = "mentor/update.html"
    form_class = TeacherForm
    context_object_name = "object"
    success_url = "mentor:mentor-list"
    success_update_url = "mentor:mentor-update"
    # permission_required = 'product.change_loanplan'


class MentorDeleteView(DeleteView):
    model = Teacher
    success_url = "mentor:mentor-list"
    # permission_required = 'product.delete_product'
