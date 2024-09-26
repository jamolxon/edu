from django.db.models import Q
from django.views.generic import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin

from helpers.views import CreateView, DeleteView, UpdateView
from common.models import Student
from common.student.forms import StudentForm



class StudentListView(ListView):
    model = Student
    template_name = "student/list.html"
    context_object_name = "objects"
    queryset = model.objects.all().order_by("-id")
    paginate_by = 10


    def get_queryset(self):
        object_list = self.queryset
        search = self.request.GET.get("search", None)
        if search:
            object_list = object_list.filter(
                    Q(first_name__icontains=search) | Q(last_name__icontains=search))

        return object_list


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student/create.html"
    context_object_name = "object"
    success_url = "student:student-list"
    success_create_url = "student:student-create"
    # permission_required = 'product.add_product'



class StudentUpdateView(UpdateView):
    model = Student
    template_name = "student/update.html"
    form_class = StudentForm
    context_object_name = "object"
    success_url = "student:student-list"
    success_update_url = "student:student-update"
    # permission_required = 'product.change_loanplan'


class StudentDeleteView(DeleteView):
    model = Student
    success_url = "student:student-list"
    # permission_required = 'product.delete_product'
