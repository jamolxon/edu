from django import forms

from common.models import Task
from helpers.widgets import CkeditorWidget, DateWidget


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("group", "name", "date", "content", )

        widgets = {
                "name": forms.TextInput(attrs={"class": "form-control"}),
                "date": DateWidget(attrs={"class": "form-control"}),
                "group": forms.Select(attrs={"class": "form-control","id":"kt_select2_1","required":"true"}),
                "content": CkeditorWidget(),

            }
