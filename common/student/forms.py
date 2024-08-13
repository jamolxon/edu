from django import forms

from common.models import Student
from helpers.widgets import CheckboxWidget


class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Student
        fields = (
                "full_name", 
                "gender", 
                "birth_date",
                "phone_number",
                "parent_number", 
                "group", 
                "date_created",
                "date_updated",
                )

        widgets = {
                "full_name": forms.TextInput(
                    attrs={"class": "form-control", "language": "all"}
                    ),

                "gender": forms.TextInput(
                    attrs={"class": "form-control", "language": "all"}
                    ),

                "product": forms.Select(
                    attrs={"class": "form-control", "id": "kt_select2_1", "language": "all"}
                    ),

                "plan": forms.Select(
                    attrs={"class": "form-control", "id": "kt_select2_3", "language": "all"}
                    ),
                "percentage": forms.TextInput(
                    attrs={"class": "form-control", "language": "all"}
                    ),
                "is_active": CheckboxWidget(attrs={"language": "all"}),
                }
