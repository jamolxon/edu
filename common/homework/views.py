from django.views.generic import ListView

from common.models import Homework, Group


class HomeworkDetailView(ListView):
    model = Group
    queryset = model.objects.all()
    template_name = "homework/detail.html"

class HomeworkListView(ListView):
    model = Group
    template_name = "homework/list.html"
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
 
