from django import forms

class CreateReport(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    lat = forms.FloatField()
    lng = forms.FloatField()
    uploadfile = forms.ImageField(required=False)
