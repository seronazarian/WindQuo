from django import forms

from basic import models

class FileForm(forms.Form):
    pdf_file = forms.FileField(widget=forms.FileInput)


class UserRegisterForm(forms.ModelForm):

    class Meta:
        model = models.User
        fields = ['username', 'first_name', 'last_name', 'email']
