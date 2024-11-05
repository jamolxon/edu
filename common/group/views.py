from django.db.models import Q
from django.views.generic import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin

from helpers.views import CreateView, DeleteView, UpdateView
from common.models import Group, Student
from common.group.forms import GroupForm



class GroupListView(ListView):
    model = Group
    template_name = "group/list.html"
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
    

class GroupStudentListView(ListView):
    model = Group
    template_name = "group/detail.html"
    context_object_name = "objects"
    queryset = model.objects.all().order_by("-id")
    paginate_by = 10


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] =  Student.objects.filter(group_id=self.kwargs["group_id"])
        return context


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = "group/create.html"
    context_object_name = "object"
    success_url = "group:group-list"
    success_create_url = "group:group-create"
    # permission_required = 'product.add_product'



class GroupUpdateView(UpdateView):
    model = Group
    template_name = "group/update.html"
    form_class = GroupForm
    context_object_name = "object"
    success_url = "group:group-list"
    success_update_url = "group:group-update"
    # permission_required = 'product.change_loanplan'


class GroupDeleteView(DeleteView):
    model = Group
    success_url = "group:group-list"
    # permission_required = 'product.delete_product'
