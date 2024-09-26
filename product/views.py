from django.views import View
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render
from django.db.models.functions import Coalesce
from django.db.models import F, FloatField, IntegerField, Subquery
from django.contrib.auth.mixins import PermissionRequiredMixin

from helpers.views import CreateView, DeleteView, UpdateView
from product.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "product/list.html"
    context_object_name = "objects"
    queryset = model.objects.all()

    def get_queryset(self):
        object_list = self.queryset
        search = self.request.GET.get("search", None)
        if search:
            object_list = object_list.filter(
                    name__icontains=search
                    )

        return object_list


