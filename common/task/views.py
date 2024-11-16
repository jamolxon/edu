from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin

from helpers.views import CreateView, DeleteView, UpdateView
from common.models import Task, Homework
from common.task.forms import TaskForm


class TaskListView(ListView):
    model = Task
    template_name = "task/list.html"
    context_object_name = "objects"
    queryset = model.objects.all().order_by("-date")
    paginate_by = 10

    def get_queryset(self):
        object_list = self.queryset
        search = self.request.GET.get("search", None)
        if search:
            object_list = object_list.filter(
                    Q(name__icontains=search))

        return object_list


class StudentTaskListView(ListView):
    model = Task
    template_name = "task/student.html"
    context_object_name = "objects"
    queryset = model.objects.all().order_by("-date")
    paginate_by = 10

    def get_queryset(self):
        return self.queryset.filter(group_id=self.request.user.students.first().group.id)

    def get_context_data(self, **kwargs):
        context = super(StudentTaskListView, self).get_context_data(**kwargs)
        context['homework'] = Homework.objects.all()
        return context



class TaskDetailView(DetailView):
    model = Task
    template_name = "task/detail.html"
    queryset = model.objects.all()
    pk_url_kwarg = "pk"
    context_object_name = "object"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task/create.html"
    context_object_name = "object"
    success_url = "task:task-list"
    success_create_url = "task:task-create"
# permission_required = 'product.add_product'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "task/update.html"
    form_class = TaskForm
    context_object_name = "object"
    success_url = "task:task-list"
    success_update_url = "task:task-update"
    # permission_required = 'product.change_loanplan'


class TaskDeleteView(DeleteView):
    model = Task
    success_url = "task:task-list"
    # permission_required = 'product.delete_product'
