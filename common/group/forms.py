from django import forms

from common.models import Group
from helpers.widgets import DateWidget, CkeditorWidget


class GroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = Group
        fields = (
                "name",
                "teacher", 
                "description",
                "start_date", 
                "end_date",
                "duration",
                "date_created"

                )
        widgets = {
                "name": forms.TextInput(
                    attrs={"class": "form-control", }
                    ),
                "teacher": forms.Select(
                    attrs={"class": "form-control", "id": "kt_select2_3", }
                    ),
                
                "description": forms.TextInput(
                    attrs={"class": "form-control", }
                    ),

                 "start_date": DateWidget(
                    attrs={"class": "form-control", "id": "kt_datetimepicker_3", "data-target": "#kt_datetimepicker_3", "placeholder": "Sanani tanlash" }
                    ),
                 "end_date": DateWidget(
                    attrs={"class": "form-control", "id": "kt_datetimepicker_2", "data-target": "#kt_datetimepicker_3", "placeholder": "Sanani tanlash" }
                    ),
                "duration": forms.TextInput(
                    attrs={"class": "form-control", }
                    ),
                 "date_created": DateWidget(
                    attrs={"class": "form-control", "id": "kt_datetimepicker_3", "data-target": "#kt_datetimepicker_3", "placeholder": "Sanani tanlash" }
                    ),
 
 
 
               


               
               


                }
