from django import forms

class CreateReport(forms.Form):
    title = forms.CharField()
    timestamp = forms.TimeField()
    description = forms.Textarea()
    lat = forms.FloatField()
    lng = forms.FloatField()
    uploadfile = forms.FileField()
