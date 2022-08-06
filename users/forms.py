from django import forms
class courses(forms.Form):
   course_code = forms.CharField(required=False)
   course_slot = forms.CharField(required=False)
   