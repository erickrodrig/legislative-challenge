from django import forms
from django.core.validators import FileExtensionValidator


class UploadFile(forms.Form):
    file = forms.FileField(
        label="",
        validators=[FileExtensionValidator(allowed_extensions=["csv"])],
        widget=forms.ClearableFileInput(attrs={"class": "form-control w-25 ms-auto me-auto mb-3"}),
    )
