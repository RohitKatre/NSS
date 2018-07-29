from django import forms
from .models import *



def get_events():
    # you place some logic here
    events = Evenet.objects.all()
    return events

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "event", "more_detail"]


# class EvenetForm(forms.ModelForm):
#     pass
#
#     class Meta:
#         model

