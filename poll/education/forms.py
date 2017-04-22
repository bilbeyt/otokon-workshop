from django import forms
from education.models import LectureDay

class PollForm(forms.Form):
    code = forms.CharField(max_length=4, required=True)

    
