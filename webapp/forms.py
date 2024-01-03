from django import forms

class ResourceUploadForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    resource_file = forms.FileField()
