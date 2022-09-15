from django import forms


class VidClipUploadForm(forms.Form):
    query = forms.CharField(max_length=1000)
    vid = forms.FileField()
