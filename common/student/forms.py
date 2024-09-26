from django import forms

from common.models import Student
from helpers.widgets import DateWidget, CkeditorWidget


class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Student
        fields = (
                "user", 
                "first_name", 
                "last_name", 
                "gender", 
                "birth_date",
                "group", 
                "image",
                "phone_number",
                "parent_number", 
                "balance", 
                "description"
                )

        widgets = {
                "user": forms.Select(
                    attrs={"class": "form-control", "id": "kt_select2_3", "language": "all"}
                    ),
                "first_name": forms.TextInput(
                    attrs={"class": "form-control", "language": "all"}
                    ),
                "last_name": forms.TextInput(
                    attrs={"class": "form-control", "language": "all"}
                    ),

                "group": forms.Select(
                    attrs={"class": "form-control", "id": "kt_select2_1", "language": "all"}
                    ),
                "gender": forms.Select(
                    attrs={"class": "form-control", "id": "kt_select2_4", "language": "all"}
                    ),
                "birth_date": DateWidget(
                    attrs={"class": "form-control", "language": "all", "id": "kt_datetimepicker_3", "data-target": "#kt_datetimepicker_3", "placeholder": "Sanani tanlash" }
                    ),
                "phone_number": forms.TextInput(
                    attrs={"class": "form-control", "language": "all"}
                    ),
                "parent_number": forms.TextInput(
                    attrs={"class": "form-control", "language": "all"}
                    ),
                "balance": forms.TextInput(
                    attrs={"class": "form-control", "language": "all"}
                    ),
                
                'description': forms.Textarea(attrs={"class": "form-control", "language": "all", 'cols': 35, 'rows': 8}),
                'image': forms.ClearableFileInput(),


                }
