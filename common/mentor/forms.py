from django import forms

from common.models import Teacher
from helpers.widgets import DateWidget, CkeditorWidget


class TeacherForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = Teacher
        fields = (
                "full_name",
                "user", 
                "description",
                "is_active", 
                "image",

                )
        widgets = {
                "full_name": forms.TextInput(
                    attrs={"class": "form-control", }
                    ),
                "user": forms.Select(
                    attrs={"class": "form-control", "id": "kt_select2_3", }
                    ),
                
                "description": forms.TextInput(
                    attrs={"class": "form-control", }
                    ),

                "is_top": forms.CheckboxInput(
                    attrs={"class": "form-control", }
                    ),

                'image': forms.ClearableFileInput(),


               
               


                }